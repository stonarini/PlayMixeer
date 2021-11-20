import pytest
from src.selecciona_cancion_random import inicia_cache

libreria = {"Cancion1": {}, "Lady gaga": {}, "pesce in mano": {}}


@pytest.mark.test_cancion_en_libreria
def test_cancion_en_libreria():
    assert inicia_cache()(libreria) in libreria


@pytest.mark.test_cancion_es_cancion
def test_cancion_es_cancion():
    assert isinstance(inicia_cache()(libreria), str)


@pytest.mark.test_salida_random
def test_salida_random():
    seleccionaCancionRandom = inicia_cache()
    playlist_generada = [seleccionaCancionRandom(libreria), seleccionaCancionRandom(libreria), seleccionaCancionRandom(libreria)]
    assert playlist_generada != libreria.keys()
