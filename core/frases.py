import time


class ConstrutorFrases:

    def __init__(self, pausa_frase=3.0):

        self.frase_atual = []

        self.ultima_palavra = ""

        self.ultimo_tempo = time.time()

        self.pausa_frase = pausa_frase

    def adicionar_palavra(self, palavra: str):

        if not palavra:

            return None


        agora = time.time()

        if palavra == self.ultima_palavra:

            self.ultimo_tempo = agora

            return None

        if agora - self.ultimo_tempo > self.pausa_frase:

            frase_final = self.finalizar_frase()

        else:

            frase_final = None

        self.frase_atual.append(palavra)

        self.ultima_palavra = palavra

        self.ultimo_tempo = agora


        return frase_final

    def finalizar_frase(self):

        if not self.frase_atual:

            return None


        frase = " ".join(self.frase_atual)


        self.frase_atual = []

        self.ultima_palavra = ""


        return frase

    def resetar(self):

        self.frase_atual = []

        self.ultima_palavra = ""