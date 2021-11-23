import sys
import os


def crear_comando(libreria, playlist):
    assert isinstance(libreria, dict)
    assert isinstance(playlist, dict)
    if sys.platform == "win32":
        comando = ["C:/Program Files/VideoLAN/VLC/vlc.exe", "-I", "dummy", "--dummy-quiet", "--gain", "0.05"]
    else:
        comando = ["/usr/bin/cvlc", "-q", "--gain", "0.05"]
    assert isinstance(comando, list)
    for numero_cancion, titulo_cancion in sorted(playlist.items()):
        assert isinstance(titulo_cancion, str)
        assert isinstance(numero_cancion, int)
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
