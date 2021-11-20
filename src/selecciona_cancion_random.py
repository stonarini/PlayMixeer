import random

# si no pasan nada es []


def inicia_cache(canciones_conocidas=[]):
    cache = canciones_conocidas

    def selecciona_cancion_random(libreria):
        nonlocal cache
        canciones_restantes = [cancion for cancion in libreria if cancion not in cache]
        # canciones_restantes = list(set(libreria) - set(cache))
        cancion_seleccionada = random.choice(canciones_restantes)
        cache.append(cancion_seleccionada)
        return cancion_seleccionada
    return selecciona_cancion_random
