from dataclasses import dataclass
from typing import List, Optional

import cv2
import mediapipe as mp

from config.settings import (
    MAX_HANDS,
    MIN_HAND_DETECTION
)

from core.utils import Landmark

@dataclass
class HandResult:

    encontrou_mao: bool

    landmarks: Optional[List[Landmark]]

    lado: str

    confianca: float

class DetectorMao:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.detector = self.mp_hands.Hands(

            static_image_mode=False,

            max_num_hands=MAX_HANDS,

            min_detection_confidence=MIN_HAND_DETECTION,

            min_tracking_confidence=0.5

        )

        self.drawer = mp.solutions.drawing_utils

    def detectar(self, frame):

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        resultado = self.detector.process(frame_rgb)

        if not resultado.multi_hand_landmarks:

            return HandResult(

                encontrou_mao=False,

                landmarks=None,

                lado="",

                confianca=0.0

            )

        hand_landmarks = resultado.multi_hand_landmarks[0]

        handedness = resultado.multi_handedness[0]

        lado = handedness.classification[0].label

        confianca = handedness.classification[0].score

        landmarks = []

        for ponto in hand_landmarks.landmark:

            landmarks.append(

                Landmark(

                    ponto.x,

                    ponto.y,

                    ponto.z

                )

            )

        return HandResult(

            encontrou_mao=True,

            landmarks=landmarks,

            lado=lado,

            confianca=confianca

        )

    def desenhar(self, frame, resultado):

        if not resultado.encontrou_mao:

            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        processado = self.detector.process(frame_rgb)

        if processado.multi_hand_landmarks:

            for hand in processado.multi_hand_landmarks:

                self.drawer.draw_landmarks(

                    frame,

                    hand,

                    self.mp_hands.HAND_CONNECTIONS

                )