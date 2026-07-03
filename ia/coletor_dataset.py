import cv2
import csv
import os

from core.camera import Camera
from core.detector_mao import DetectorMao

DATASET_PATH = os.path.join("data", "datasets", "libras_landmarks.csv")


def init_csv():
    os.makedirs(os.path.dirname(DATASET_PATH), exist_ok=True)

    if not os.path.isfile(DATASET_PATH):

        with open(DATASET_PATH, mode="w", newline="") as f:
            writer = csv.writer(f)

            header = ["label"]

            for i in range(21):
                header += [f"x{i}", f"y{i}", f"z{i}"]

            writer.writerow(header)


def salvar_amostra(label, landmarks):

    if not landmarks or len(landmarks) < 21:
        return

    base = landmarks[0]

    row = [label]

    for lm in landmarks:
        row.extend([
            lm.x - base.x,
            lm.y - base.y,
            lm.z - base.z
        ])

    with open(DATASET_PATH, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def coletar():

    camera = Camera()
    detector = DetectorMao()

    print("\n=== COLETOR LIBRAS ===")
    print("A-Z para salvar | Q para sair")

    init_csv()

    total = 0

    while True:

        frame = camera.ler()
        if frame is None:
            break

        result = detector.detectar(frame)
        detector.desenhar(frame, result)

        cv2.imshow("Coletor", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

        if 97 <= key <= 122:

            label = chr(key).upper()

            if result.encontrou_mao:
                salvar_amostra(label, result.landmarks)
                total += 1
                print(f"[OK] {label} salvo | total: {total}")
            else:
                print("[WARN] mão não detectada")


    camera.fechar()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    coletar()