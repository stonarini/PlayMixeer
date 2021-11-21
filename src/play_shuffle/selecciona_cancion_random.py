import random


def inicia_canciones_conocidas(canciones_conocidas):
    def selecciona_cancion_random(libreria):
        assert isinstance(libreria, dict)

        nonlocal canciones_conocidas

        canciones_restantes = [cancion for cancion in libreria if cancion not in canciones_conocidas]
        # canciones_restantes = list(set(libreria) - set(canciones_conocidas))
        cancion_seleccionada = random.choice(canciones_restantes)

        canciones_conocidas.append(cancion_seleccionada)

        assert isinstance(cancion_seleccionada, str)
        assert cancion_seleccionada in libreria

        return cancion_seleccionada

    return selecciona_cancion_random
