import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "modelos", "libras_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "modelos", "label_encoder.pkl")


class InferenciaML:

    def __init__(self):
        self.model = None
        self.encoder = None

        if not os.path.exists(MODEL_PATH):
            print("[WARN] Modelo não encontrado. ML desativado.")
            return

        self.model = joblib.load(MODEL_PATH)
        print("[INFO] Modelo ML carregado")

        if os.path.exists(ENCODER_PATH):
            self.encoder = joblib.load(ENCODER_PATH)
            print("[INFO] LabelEncoder carregado")

    def _extract_features(self, landmarks):
        """
        GARANTE 63 FEATURES SEMPRE
        """
        if landmarks is None:
            return None

        features = []
        for lm in landmarks:
            features.extend([lm.x, lm.y, lm.z])

        arr = np.array(features, dtype=np.float32)

        # 🔥 GARANTIA CRÍTICA
        if arr.shape[0] != 63:
            return None

        return arr.reshape(1, -1)

    def prever(self, hand_result):

        if not hand_result or not hand_result.encontrou_mao:
            return {
                "letra": "",
                "confianca": 0.0,
                "metodo": "NO_HAND"
            }

        X = self._extract_features(hand_result.landmarks)

        if X is None:
            return {
                "letra": "",
                "confianca": 0.0,
                "metodo": "INVALID_FEATURES"
            }

        pred = self.model.predict(X)[0]

        # decode label se existir encoder
        if self.encoder:
            try:
                pred = self.encoder.inverse_transform([pred])[0]
            except:
                pass

        confianca = 1.0
        if hasattr(self.model, "predict_proba"):
            try:
                confianca = float(np.max(self.model.predict_proba(X)))
            except:
                pass

        return {
            "letra": str(pred),
            "confianca": confianca,
            "metodo": "ML"
        }