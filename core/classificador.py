import ctypes
from dataclasses import dataclass

from core.utils import Landmark, obter_nome_biblioteca

@dataclass
class ClassificationResult:

    letra: str

    confianca: float

    metodo: str

class Classificador:

    def __init__(self):

        self.lib = ctypes.CDLL(obter_nome_biblioteca())

        self.lib.classificar_libras.argtypes = [ctypes.POINTER(Landmark)]

        self.lib.classificar_libras.restype = ctypes.c_char

    def _converter_landmarks(self, landmarks):

        array_c = (Landmark * 21)()

        for i, lm in enumerate(landmarks):

            array_c[i].x = lm.x

            array_c[i].y = lm.y

            array_c[i].z = lm.z

        return array_c

    def classificar(self, hand_result):

        if not hand_result.encontrou_mao:

            return ClassificationResult(

                letra="",

                confianca=0.0,

                metodo="C_GEOMETRICO"

            )

        array_c = self._converter_landmarks(hand_result.landmarks)

        resultado = self.lib.classificar_libras(array_c)

        letra = resultado.decode("utf-8")

        return ClassificationResult(

            letra=letra,

            confianca=1.0,

            metodo="C_GEOMETRICO"
        )