import subprocess


def ejecutar_comando(comando):
    try:
        proceso = subprocess.Popen(comando)
    except OSError:
        print("VLC no esta instalado o no se ha encontrado el fichero")
    except ValueError:
        print("Argumentos invalidos")
    else:
        print(proceso)
        print("lanzando VLC <3")
        return proceso
    return None


def finalizar_proceso(proceso):
    palabra_parar = ["stop", "end", "fin", "s", "kill", "finiquitao", "finalizar"]
    while proceso.poll() is not None:
        palabra = input("Finalizar el proceso (stop/fin): ").lower()
        if palabra in palabra_parar:
            proceso.terminate()
    print("Ha terminado el programa")
