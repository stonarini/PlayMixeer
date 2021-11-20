import pytest
from src.selecciona_cancion_random import inicia_cache

libreria = {"Cancion1": {}, "Lady gaga": {}, "pesce in mano": {}, "roxxane": {}, "nata vota": {}}



@pytest.mark.test_comprobar_funcion
def test_comprobar_funcion():
    assert callable(inicia_cache())

@pytest.mark.test_cancion_en_libreria
def test_cancion_en_libreria():
    assert inicia_cache()(libreria) in libreria


@pytest.mark.test_cancion_es_cancion
def test_cancion_es_cancion():
    assert isinstance(inicia_cache()(libreria), str)


@pytest.mark.test_salida_random
def test_salida_random():
    selecciona_cancion_random = inicia_cache()
    primera_playlist = [selecciona_cancion_random(libreria) for cancion in libreria]

    selecciona_cancion_random = inicia_cache() # reinicia cache
    segunda_playlist = [selecciona_cancion_random(libreria) for cancion in libreria]

    selecciona_cancion_random = inicia_cache() # reinicia cache
    tercera_playlist = [selecciona_cancion_random(libreria) for cancion in libreria]
    assert primera_playlist != segunda_playlist and primera_playlist != tercera_playlist
