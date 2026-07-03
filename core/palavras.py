import time


class ConstrutorPalavras:

    def __init__(self, tempo_pausa=1.2):

        self.palavra_atual = ""

        self.ultima_letra = ""

        self.ultimo_tempo = time.time()

        self.tempo_pausa = tempo_pausa

    def adicionar_letra(self, letra: str):

        if not letra or letra == "?" or letra == "-":

            return None


        agora = time.time()

        if letra == self.ultima_letra:

            self.ultimo_tempo = agora

            return None

        if agora - self.ultimo_tempo > self.tempo_pausa:

            palavra_final = self.finalizar_palavra()

        else:

            palavra_final = None

        self.palavra_atual += letra

        self.ultima_letra = letra

        self.ultimo_tempo = agora


        return palavra_final

    def finalizar_palavra(self):

        if not self.palavra_atual:

            return None


        palavra = self.palavra_atual


        self.palavra_atual = ""

        self.ultima_letra = ""


        return palavra

    def resetar(self):

        self.palavra_atual = ""

        self.ultima_letra = ""