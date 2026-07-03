import cv2
import csv
import os

from core.camera import Camera
from core.detector_mao import DetectorMao

DATASET_PATH = "data/datasets/libras_landmarks.csv"
def init_csv():

    if not os.path.exists("data/datasets"):

        os.makedirs("data/datasets")

    if not os.path.isfile(DATASET_PATH):

        with open(DATASET_PATH, mode="w", newline="") as f:

            writer = csv.writer(f)

            header = ["label"]

            for i in range(21):

                header += [f"x{i}", f"y{i}", f"z{i}"]

            writer.writerow(header)

def salvar_amostra(label, landmarks):

    if landmarks is None:

        return

    row = [label]

    for lm in landmarks:

        row.extend([lm.x, lm.y, lm.z])

    with open(DATASET_PATH, mode="a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(row)

def coletar():

    camera = Camera()

    detector = DetectorMao()

    print("\n====================================")

    print("COLETOR DE DATASET LIBRAS")

    print("Pressione uma tecla de A-Z para salvar")

    print("Pressione Q para sair")

    print("====================================\n")

    init_csv()

    while True:

        frame = camera.ler()

        if frame is None:

            break

        resultado = detector.detectar(frame)

        detector.desenhar(frame, resultado)

        cv2.imshow("Coletor de Dataset", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):

            break

        if 97 <= key <= 122:

            label = chr(key).upper()

            if resultado.encontrou_mao:

                salvar_amostra(label, resultado.landmarks)

                print(f"[OK] Amostra salva: {label}")

            else:

                print("[ERRO] Nenhuma mão detectada")

    camera.fechar()

    cv2.destroyAllWindows()


if __name__ == "__main__":

    coletar()