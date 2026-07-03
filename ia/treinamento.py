import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

DATASET_PATH = "data/datasets/libras_landmarks.csv"
MODEL_PATH = "ia/modelos/libras_model.pkl"
ENCODER_PATH = "ia/modelos/label_encoder.pkl"


def carregar_dataset():
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError("Dataset não encontrado.")

    df = pd.read_csv(DATASET_PATH)

    X = df.drop("label", axis=1)
    y = df["label"]

    return X, y


def treinar():
    print("\n[INFO] Carregando dataset...")

    X, y = carregar_dataset()

    print(f"[INFO] Dataset carregado: {len(X)} amostras")

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_encoded,
        test_size=0.2,
        random_state=42,
        stratify=y_encoded
    )

    print("[INFO] Treinando XGBoost...")

    model = XGBClassifier(
        n_estimators=300,
        max_depth=8,
        learning_rate=0.05,
        subsample=0.9,
        colsample_bytree=0.9,
        objective="multi:softprob",
        eval_metric="mlogloss"
    )

    model.fit(X_train, y_train)

    print("[INFO] Avaliando modelo...")

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"[INFO] Acurácia: {acc * 100:.2f}%")

    os.makedirs("ia/modelos", exist_ok=True)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(encoder, ENCODER_PATH)

    print(f"[INFO] Modelo salvo em: {MODEL_PATH}")
    print(f"[INFO] Encoder salvo em: {ENCODER_PATH}")


if __name__ == "__main__":
    treinar()