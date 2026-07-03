import pyttsx3


class SintetizadorVoz:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)

        self.engine.setProperty("volume", 1.0)

        print("[INFO] Sintetizador de voz inicializado.")

    def falar(self, texto: str):

        if not texto:

            return

        self.engine.say(texto)

        self.engine.runAndWait()

    def falar_letra(self, letra: str):

        self.falar(f"Letra {letra}")

    def falar_palavra(self, palavra: str):

        self.falar(f"Palavra formada: {palavra}")

    def falar_emocao(self, emocao: str):

        self.falar(f"Emoção detectada: {emocao}")