from ia.inferencia import InferenciaML


class ClassificadorHibrido:

    def __init__(self):
        self.ml = InferenciaML()
        print("[INFO] Classificador híbrido inicializado.")

    def classificar(self, hand_result):

        if hand_result is None:
            return {
                "letra": "-",
                "confianca": 0.0,
                "metodo": "NO_INPUT"
            }

        if not hasattr(hand_result, "encontrou_mao") or not hand_result.encontrou_mao:
            return {
                "letra": "-",
                "confianca": 0.0,
                "metodo": "NO_HAND"
            }

        ml_result = self.ml.prever(hand_result)

        if ml_result and ml_result.get("letra"):
            return ml_result

        return {
            "letra": "-",
            "confianca": 0.0,
            "metodo": "FALLBACK"
        }