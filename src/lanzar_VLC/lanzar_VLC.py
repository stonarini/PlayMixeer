
from lanzar_VLC.crear_comando import crear_comando
from lanzar_VLC.ejecutar_comando import ejecutar_comando, finalizar_proceso


def lanzar_VLC(libreria, playlist):
    comando = crear_comando(libreria, playlist)
    proceso = ejecutar_comando(comando)
    if proceso:
        finalizar_proceso(proceso)
