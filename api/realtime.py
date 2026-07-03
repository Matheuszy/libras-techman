from fastapi import FastAPI, WebSocket
import cv2
import base64
import asyncio

from core.detector_mao import DetectorMao
from core.classificador_hibrido import ClassificadorHibrido
from core.detector_emocao import DetectorEmocao


app = FastAPI()

detector_mao = DetectorMao()
classificador = ClassificadorHibrido()
emocao_engine = DetectorEmocao()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    cap = cv2.VideoCapture(0)

    try:
        while True:

            ret, frame = cap.read()

            if not ret:
                break

            frame = cv2.flip(frame, 1)

            hand_result = detector_mao.detectar(frame)

            resultado = classificador.classificar(hand_result)

            letra = resultado.get("letra", "-")
            confianca = resultado.get("confianca", 0.0)
            metodo = resultado.get("metodo", "unknown")

            emocao = emocao_engine.detectar(frame)

            _, buffer = cv2.imencode(
                ".jpg",
                frame,
                [int(cv2.IMWRITE_JPEG_QUALITY), 70]
            )

            frame_b64 = base64.b64encode(buffer).decode("utf-8")

            if hasattr(emocao, "to_dict"):
                emocao = emocao.to_dict()

            if not isinstance(emocao, dict):
                emocao = {
                    "emotion": "unknown",
                    "confidence": 0.0
                }

            await websocket.send_json({
                "letra": letra,
                "confianca": confianca,
                "metodo": metodo,
                "emocao": emocao,
                "frame": frame_b64
            })

            await asyncio.sleep(0.01)

    except Exception as e:
        print(f"[WS ERROR] {e}")

    finally:
        cap.release()
        await websocket.close()