import pytest
from src.play_shuffle import play_shuffle

libreria = {"Cancion1": {}, "Lady gaga": {}, "pesce in mano": {}, "roxxane": {}, "nata vota": {}}


@pytest.mark.test_lista_aleatoria
def test_lista_aleatoria():
    assert play_shuffle(libreria) != play_shuffle(libreria)


@pytest.mark.test_lista_vacia
def test_lista_vacia():
    assert play_shuffle(libreria)


@pytest.mark.test_lista_completa
def test_lista_completa():
    assert len(play_shuffle(libreria)) == len(libreria)
    assert sorted(libreria.keys()) == sorted(play_shuffle(libreria).values())
