import os
import shutil
from test.libreria import libreria, playlist
import pytest
from src.lanzar_VLC.crear_comando import crear_comando

comando = crear_comando(libreria, playlist)


@pytest.mark.test_VLC_instalado
def test_VLC_instalado():
    assert shutil.which(comando[0])


@pytest.mark.test_lista_valida
def test_lista_valida():
    assert isinstance(comando, list) and len(comando) > 0


@pytest.mark.test_ruta_existente
def test_ruta_existente():
    assert False not in [os.path.exists(ruta) for ruta in comando[1:]]


@pytest.mark.test_ruta_unica
def test_ruta_unica():
    assert len(set(comando)) == len(comando)
