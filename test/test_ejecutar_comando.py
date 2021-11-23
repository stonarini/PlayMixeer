import pytest
from src.lanzar_VLC.ejecutar_comando import ejecutar_comando

comando = ["C:/Program Files/VideoLAN/VLC/vlc.exe", "./biblioteca/Rosexxa.mp3"]


@pytest.mark.test_proceso_valido
def test_proceso_valido():
    proceso = ejecutar_comando(comando)
    assert proceso
    proceso.terminate()
