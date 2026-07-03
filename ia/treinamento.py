from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATASET_PATH = "data/datasets/libras_landmarks.csv"
MODEL_PATH = "ia/modelos/libras_model.pkl"

def carregar_dataset():

    if not os.path.exists(DATASET_PATH):

        raise FileNotFoundError("Dataset não encontrado. Execute o coletor primeiro.")

    df = pd.read_csv(DATASET_PATH)

    X = df.drop("label", axis=1)

    y = df["label"]

    return X, y

def treinar():

    print("\n[INFO] Carregando dataset...")

    X, y = carregar_dataset()

    print(f"[INFO] Dataset carregado: {len(X)} amostras")

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42

    )

    print("[INFO] Treinando modelo RandomForest...")

    model = RandomForestClassifier(

        n_estimators=150,

        random_state=42

    )

    model.fit(X_train, y_train)

    print("[INFO] Modelo treinado")

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    print(f"[INFO] Acurácia: {acc * 100:.2f}%")

    os.makedirs("ia/modelos", exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print(f"[INFO] Modelo salvo em: {MODEL_PATH}")


if __name__ == "__main__":    treinar()