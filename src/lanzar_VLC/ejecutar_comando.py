import subprocess
import time


def ejecutar_comando(comando):
    assert isinstance(comando, list)
    assert len(comando) > 1
    try:
        proceso = subprocess.Popen(comando)
    except OSError:
        print("VLC no esta instalado o no se ha encontrado el fichero")
    except ValueError:
        print("Argumentos invalidos")
    else:
        print("lanzando VLC <3")
        return proceso
    return None


def finalizar_proceso(proceso):
    assert proceso is not None
    palabra_parar = ["stop", "end", "fin", "s", "kill", "finiquitao", "finalizar"]
    time.sleep(0.5)
    while proceso.poll() is None:
        palabra = input("Finalizar el proceso (stop/fin): ").lower()
        if palabra in palabra_parar:
            proceso.terminate()
            break
    print("Ha terminado el programa")
