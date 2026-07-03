from dataclasses import dataclass
from typing import Optional

from deepface import DeepFace

@dataclass
class EmotionResult:

    emocao: str

    confianca: float

class DetectorEmocao:

    def __init__(self, refresh_rate: int = 10):

        self.refresh_rate = refresh_rate

        self.counter = 0

        self.last_result = EmotionResult(

            emocao="neutral",

            confianca=0.0

        )

    def detectar(self, frame):

        self.counter += 1

        if self.counter % self.refresh_rate != 0:

            return self.last_result

        try:

            analysis = DeepFace.analyze(

                img_path=frame,

                actions=['emotion'],

                enforce_detection=False,

                silent=True

            )

            if isinstance(analysis, list):

                analysis = analysis[0]

            emocao = analysis["dominant_emotion"]

            confianca = max(analysis["emotion"].values())

            self.last_result = EmotionResult(

                emocao=emocao,

                confianca=float(confianca)

            )

        except Exception:

            self.last_result = EmotionResult(

                emocao="unknown",

                confianca=0.0

            )

        return self.last_result