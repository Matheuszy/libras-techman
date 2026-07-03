import cv2
import time

from config.settings import (
    WINDOW_NAME,
    FONT_SCALE,
    FONT_THICKNESS
)

class HUD:

    def __init__(self):

        self.last_time = time.time()

        self.fps = 0

    def _calcular_fps(self):

        current_time = time.time()

        self.fps = 1 / (current_time - self.last_time + 1e-6)

        self.last_time = current_time

    def desenhar(self, frame, letra, emocao):

        self._calcular_fps()

        cv2.rectangle(

            frame,

            (10, 10),

            (420, 140),

            (0, 0, 0),

            -1

        )

        cv2.putText(

            frame,

            f"LIBRAS: {letra}",

            (20, 45),

            cv2.FONT_HERSHEY_SIMPLEX,

            FONT_SCALE,

            (0, 255, 0),

            FONT_THICKNESS

        )

        cv2.putText(

            frame,

            f"EMOCAO: {emocao.emocao}",

            (20, 80),

            cv2.FONT_HERSHEY_SIMPLEX,

            FONT_SCALE - 0.1,

            (255, 255, 0),

            FONT_THICKNESS - 1

        )

        cv2.putText(

            frame,

            f"FPS: {int(self.fps)}",

            (20, 115),

            cv2.FONT_HERSHEY_SIMPLEX,

            FONT_SCALE - 0.1,

            (0, 200, 255),

            FONT_THICKNESS - 1

        )

        # Status fixo
        cv2.putText(

            frame,

            "MODE: GEOMETRIC (C ENGINE)",

            (20, 135),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.5,

            (200, 200, 200),

            1

        )

        return frame