import streamlit as st
import websocket
import json
import base64
import cv2
import numpy as np

st.set_page_config(layout="wide")

st.title("🧠 Libras-TechMan - Real Time Translator")

col_video, col_info = st.columns([3, 1])

ws = websocket.WebSocket()
ws.connect("ws://localhost:8000/ws")

video_placeholder = col_video.empty()
info_placeholder = col_info.empty()

while True:
    try:
        data = json.loads(ws.recv())

        img_bytes = base64.b64decode(data["frame"])
        np_arr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        video_placeholder.image(frame, channels="RGB", use_container_width=True)

        emocao = data.get("emocao", {})

        letra = data.get("letra", "")
        confianca = data.get("confianca_letra", 0)

        emotion_name = emocao.get("emotion", "unknown")
        emotion_conf = emocao.get("confidence", 0)

        with info_placeholder:
            st.markdown("## 📊 Detecção em tempo real")

            st.markdown("### ✋ Letra detectada")
            st.markdown(f"## `{letra if letra else '-'}`")
            st.progress(min(confianca, 1.0))

            st.markdown("---")

            st.markdown("### 🧠 Emoção")

            st.metric("Estado emocional", emotion_name)
            st.progress(min(float(emotion_conf), 1.0))

            st.markdown(
                f"""
                <div style="
                    padding: 10px;
                    border-radius: 10px;
                    background-color: #111;
                    color: white;
                    margin-top: 10px;
                ">
                    <h4>Resumo</h4>
                    <p>Letra: {letra}</p>
                    <p>Emoção: {emotion_name}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    except Exception as e:
        st.error(f"Erro na conexão: {e}")
        break