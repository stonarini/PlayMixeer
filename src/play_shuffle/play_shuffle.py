from src.play_shuffle.selecciona_cancion_random import inicia_canciones_conocidas


def play_shuffle(libreria):

    assert isinstance(libreria, dict)

    playlist = {}
    selecciona_cancion_random = inicia_canciones_conocidas([])
    for llave_index in range(1, len(libreria)+1):
        playlist[llave_index] = selecciona_cancion_random(libreria)
        print("Seleccionada: " + playlist[llave_index])

    assert isinstance(playlist, dict)

    return playlist
