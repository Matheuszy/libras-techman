from dataclasses import dataclass

from core.classificador import Classificador
from ia.inferencia import InferenciaML

@dataclass
class HybridResult:

    letra: str

    confianca: float

    metodo: str

class ClassificadorHibrido:

    def __init__(self):

        self.engine_c = Classificador()

        self.engine_ml = InferenciaML()

        print("[INFO] Classificador híbrido inicializado.")

    def classificar(self, hand_result):

        if not hand_result.encontrou_mao:

            return HybridResult(

                letra="",

                confianca=0.0,

                metodo="NONE"

            )

        resultado_c = self.engine_c.classificar(hand_result)

        confianca_c = 0.85 if resultado_c.letra != "?" else 0.0

        resultado_ml = self.engine_ml.prever(hand_result)

        if confianca_c >= 0.85:

            return HybridResult(

                letra=resultado_c.letra,

                confianca=confianca_c,

                metodo="C_ENGINE"

            )

        if resultado_ml["confianca"] > confianca_c:

            return HybridResult(

                letra=resultado_ml["letra"],

                confianca=resultado_ml["confianca"],

                metodo="ML_ENGINE"

            )

        if resultado_c.letra != "?":

            return HybridResult(

                letra=resultado_c.letra,

                confianca=confianca_c,

                metodo="C_FALLBACK"

            )

        return HybridResult(

            letra="",

            confianca=0.0,

            metodo="UNKNOWN"

        )