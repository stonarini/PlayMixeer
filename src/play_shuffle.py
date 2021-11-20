from src.selecciona_cancion_random import inicia_cache


def play_shuffle(libreria):
    playlist = {}
    selecciona_cancion_random = inicia_cache()
    for llave_index in range(1, len(libreria)+1):
        playlist[llave_index] = selecciona_cancion_random(libreria)
        print("Seleccionada: " + playlist[llave_index])
    return playlist
