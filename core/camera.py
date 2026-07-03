import cv2

from config.settings import CAMERA_INDEX

class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        if not self.cap.isOpened():

            raise RuntimeError("Não foi possível abrir a webcam.")

    def ler(self):

        sucesso, frame = self.cap.read()

        if not sucesso:

            return None

        return cv2.flip(frame,1)

    def fechar(self):

        self.cap.release()

    def __enter__(self):

        return self

    def __exit__(self,*args):

        self.fechar()