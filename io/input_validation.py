'''
Archivo para validar las entradas
'''

from unimon.pokedex.unimon import Unimon
from random import randint

# esta funcion sera para elegir el unimon, necesita la variable dada por leer_unimon o la variable "todos" de la clase Unimon (nose)
def elegir_unimon_usr(lista_unimon):
    pass

# esta funcion sera para elegir las habilidades, necesita la variable dada por leer_habilidad o la variable "todos" de la clase habilidades (nose)
# tambien necesitara verificar si el pokemon las puede tener, por eso hay una lista despues de las estadisticas de unimon.txt
def elegir_habilidades_usr(unimon):
    pass

# las siguientes dos funciones son lo mismo que las anteriores pero con el npc
def elegir_unimon_npc(lista_unimon):
    pass

def elegir_habilidades_npc(unimon):
    pass

# el usuaria elige la habilidad a utilizar
def elegir_turno_usr(unimon):
    # se guarda la longitud de la lista habilidades porque se repite mucho
    longitud = len(unimon.habilidades)
    # se imprimen las habilidades
    unimon.str_habilidades()
    
    while True:
        try:
            opcion = int(input(f"Elige opción (0-{longitud}): "))

            if opcion < 0 or opcion > longitud:
                raise ValueError("Opción fuera de rango")
            break

        except ValueError as e:
            print(e)
    
    # regresa la habilidad seleccionada
    return unimon.habilidades[opcion]

# el npc elige aleatoriamente
def elegir_turno_npc(unimon):
    return unimon.habilidades[randint(0, len(unimon.habilidades))]