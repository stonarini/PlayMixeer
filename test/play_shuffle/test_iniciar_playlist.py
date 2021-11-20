import pytest
from src.play_shuffle.iniciar_playlist import iniciar_playlist


@pytest.mark.test_comprobar_funcion
def test_comprobar_funcion():
    assert callable(iniciar_playlist(0))


@pytest.mark.test_playlist_actualizada
def test_playlist_actualizada():
    append_cancion = iniciar_playlist(0)
    playlist = {}
    append_cancion("2055", playlist)
    assert playlist == {1: "2055"}
    append_cancion("pesce in mano", playlist)
    assert playlist == {1: "2055", 2: "pesce in mano"}
    append_cancion("جواد", playlist)
    assert playlist == {1: "2055", 2: "pesce in mano", 3: "جواد"}
