# Lo que hacemos es pasarle el numero inicial de la playlist.
# Y ponemos el numero a las canciones de la playlist.
def iniciar_playlist(index_disco):
    assert index_disco >= 0
    assert isinstance(index_disco, int)

    def append_cancion(cancion, playlist):
        assert isinstance(playlist, dict)
        assert isinstance(cancion, str)
        assert cancion not in playlist.values()

        nonlocal index_disco
        index_disco += 1
        playlist[index_disco] = cancion

        assert isinstance(playlist, dict)
        assert cancion in playlist.values()

        return index_disco

    return append_cancion
