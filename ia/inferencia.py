import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "modelos", "libras_model.pkl")

class InferenciaML:

    def __init__(self):

        self.model = None

        if not os.path.exists(MODEL_PATH):
            print("[WARN] Modelo não encontrado. ML desativado.")
            return

        self.model = joblib.load(MODEL_PATH)

        print("[INFO] Modelo ML carregado com sucesso.")

    def _converter_landmarks(self, landmarks):

        features = []

        for lm in landmarks:
            features.extend([lm.x, lm.y, lm.z])

        return np.array(features).reshape(1, -1)

    def prever(self, hand_result):

        if not hand_result or not hand_result.encontrou_mao:
            return {
                "letra": "",
                "confianca": 0.0,
                "metodo": "ML_OFF"
            }

        if self.model is None:
            return {
                "letra": "",
                "confianca": 0.0,
                "metodo": "ML_DISABLED"
            }

        X = self._converter_landmarks(hand_result.landmarks)

        previsao = self.model.predict(X)[0]

        try:
            proba = self.model.predict_proba(X)
            confianca = float(np.max(proba))
        except:
            confianca = 1.0

        return {
            "letra": str(previsao),
            "confianca": confianca,
            "metodo": "ML"
        }