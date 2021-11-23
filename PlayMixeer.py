from src.play_shuffle.play_shuffle import play_shuffle
from src.lanzar_VLC.lanzar_VLC import lanzar_VLC
from src.imprimir_canciones import imprimir_canciones
from libreria import libreria


def PlayMixeer(libreria):
    playlist = play_shuffle(libreria)
    imprimir_canciones(playlist)
    lanzar_VLC(libreria, playlist)


if __name__ == "__main__":
    PlayMixeer(libreria)
