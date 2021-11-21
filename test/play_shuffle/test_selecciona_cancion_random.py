import pytest
from src.play_shuffle.selecciona_cancion_random import inicia_canciones_conocidas

libreria = {"Aspettando il sole": {}, "Lady gaga": {}, "pesce in mano": {}, "roxxane": {}, "nata vota": {}}


@pytest.mark.test_comprobar_funcion
def test_comprobar_funcion():
    assert callable(inicia_canciones_conocidas([]))


@pytest.mark.test_cancion_en_libreria
def test_cancion_en_libreria():
    assert inicia_canciones_conocidas([])(libreria) in libreria


@pytest.mark.test_cancion_es_cancion
def test_cancion_es_cancion():
    assert isinstance(inicia_canciones_conocidas([])(libreria), str)


@pytest.mark.test_salida_random
def test_salida_random():
    selecciona_cancion_random = inicia_canciones_conocidas([])
    primera_playlist = [selecciona_cancion_random(libreria) for cancion in libreria]

    selecciona_cancion_random = inicia_canciones_conocidas([])  # reinicia canciones_conocidas
    segunda_playlist = [selecciona_cancion_random(libreria) for cancion in libreria]

    selecciona_cancion_random = inicia_canciones_conocidas([])  # reinicia canciones_conocidas
    tercera_playlist = [selecciona_cancion_random(libreria) for cancion in libreria]
    assert primera_playlist != segunda_playlist and primera_playlist != tercera_playlist
