import random
from typing import List


def inicia_cache():
    cache = []

    def selecciona_cancion_random(libreria):
        assert isinstance(libreria, dict)

        nonlocal cache

        canciones_restantes = [cancion for cancion in libreria if cancion not in cache]
        # canciones_restantes = list(set(libreria) - set(cache))
        cancion_seleccionada = random.choice(canciones_restantes)

        cache.append(cancion_seleccionada)

        assert isinstance(cancion_seleccionada, str)
        assert cancion_seleccionada in libreria

        return cancion_seleccionada

    return selecciona_cancion_random
