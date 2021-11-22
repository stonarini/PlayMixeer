import sys
import os


def crear_comando(libreria, playlist):
    if sys.platform == "win32":
        comando = ["C:/Program File/VideoLAN/VLC/vlc.exe", "-I", "dummy", "--dummy-quiet"]
    else:
        comando = ["/usr/bin/cvlc"]
    for numero_cancion, titulo_cancion in sorted(playlist.items()):
        try:
            ruta_cancion = libreria[titulo_cancion]["location"]
        except KeyError:
            print("tu cancion llamada", titulo_cancion, "esta to perdia")
        else:
            if os.path.exists(ruta_cancion):
                comando.append(ruta_cancion)
            else:
                print("La cancion", titulo_cancion, "no se ha encontrado en", ruta_cancion)
    return comando
