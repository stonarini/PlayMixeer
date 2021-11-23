
def imprimir_canciones(playlist):
    assert isinstance(playlist, dict)
    for cancion in sorted(playlist):
        print(cancion, ':', playlist[cancion])
