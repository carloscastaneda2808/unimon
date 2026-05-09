'''
Archivo para validar las entradas
'''

from unimon.pokedex.unimon import Unimon
from random import randint

def elegir_unimon_usr():
    pass

def elegir_habilidades_usr(unimon):
    pass

def elegir_unimon_npc():
    pass

def elegir_habilidades_npc(unimon):
    pass

def elegir_turno_usr(unimon):
    longitud = len(unimon.habilidades)
    unimon.str_habilidades()
    
    while True:
        try:
            opcion = int(input(f"Elige opción (0-{longitud}): "))

            if opcion < 0 or opcion > longitud:
                raise ValueError("Opción fuera de rango")
            break

        except ValueError as e:
            print(e)
    
    return unimon.habilidades[opcion]

def elegir_turno_npc(unimon):
    return unimon.habilidades[randint(0, len(unimon.habilidades))]