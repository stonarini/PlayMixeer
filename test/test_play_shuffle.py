import pytest
from src.play_shuffle import play_shuffle
libreria = {}


@pytest.mark.test_lista_aleatoria
def test_lista_aleatoria():
    assert play_shuffle(libreria) != play_shuffle(libreria)


@pytest.mark.test_lista_vacia
def test_lista_vacia():
    assert play_shuffle(libreria)


@pytest.mark.test_lista_completa
def test_lista_completa():
    assert len(play_shuffle(libreria)) == len(libreria)

    # comprobar que estan todas las canciones , preguntando por los nombres de las mismas.
