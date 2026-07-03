import cv2

from core.camera import Camera
from core.detector_mao import DetectorMao
from core.desenhador import HUD
from core.detector_emocao import DetectorEmocao
from core.classificador_hibrido import ClassificadorHibrido
from core.palavras import ConstrutorPalavras
from core.frases import ConstrutorFrases
from voz.sintetizador import SintetizadorVoz


def main():

    print("\n[INFO] Inicializando Libras-TechMan...\n")

    camera = Camera()
    detector_mao = DetectorMao()
    classificador = ClassificadorHibrido()
    detector_emocao = DetectorEmocao(refresh_rate=10)
    hud = HUD()

    palavras = ConstrutorPalavras()
    frases = ConstrutorFrases()
    voz = SintetizadorVoz()

    print("[INFO] Sistema iniciado com sucesso.\n")

    while True:

        frame = camera.ler()

        if frame is None:
            print("[ERRO] Frame inválido.")
            break

        hand_result = detector_mao.detectar(frame)

        letra = "-"
        metodo = "NONE"
        confianca = 0.0

        if hand_result.encontrou_mao:

            resultado = classificador.classificar(hand_result)

            letra = resultado.letra
            metodo = resultado.metodo
            confianca = resultado.confianca

            detector_mao.desenhar(frame, hand_result)


            palavra_final = palavras.adicionar_letra(letra)

            if palavra_final:

                frase_final = frases.adicionar_palavra(palavra_final)

                if frase_final:

                    voz.falar(frase_final)

        emocao = detector_emocao.detectar(frame)

        frame = hud.desenhar(frame, letra, emocao)

        cv2.putText(

            frame,

            f"MODE: {metodo} | CONF: {confianca:.2f}",

            (20, 170),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.5,

            (180, 180, 180),

            1

        )

        cv2.imshow("Libras-TechMan", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.fechar()
    cv2.destroyAllWindows()

    print("\n[INFO] Sistema finalizado com sucesso.")


if __name__ == "__main__":
    main()