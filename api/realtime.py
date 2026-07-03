from fastapi import FastAPI, WebSocket
import cv2
import base64

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
                continue

            frame = cv2.flip(frame, 1)

            hand_result = detector_mao.detectar(frame)

            letra = ""
            confianca_letra = 0.0

            if hand_result.encontrou_mao:
                resultado = classificador.classificar(hand_result)
                letra = getattr(resultado, "letra", "")
                confianca_letra = float(getattr(resultado, "confianca", 0.0))
                detector_mao.desenhar(frame, hand_result)

            emocao_raw = emocao_engine.detectar(frame)

            if hasattr(emocao_raw, "__dict__"):
                emocao = {
                    "emotion": getattr(emocao_raw, "emotion", "unknown"),
                    "confidence": float(getattr(emocao_raw, "confidence", 0.0))
                }
            else:
                emocao = {
                    "emotion": "unknown",
                    "confidence": 0.0
                }

            _, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
            frame_b64 = base64.b64encode(buffer).decode("utf-8")

            await websocket.send_json({
                "letra": letra,
                "confianca_letra": confianca_letra,
                "emocao": emocao,
                "frame": frame_b64
            })

    except Exception as e:
        print("[WS ERROR]", e)

    finally:
        cap.release()