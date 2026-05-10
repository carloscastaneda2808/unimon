'''
Archivo para validar las entradas
'''

from random import randint

from unimon.pokedex.unimon import Unimon
from unimon.pokedex.habilidad import Habilidad

# esta funcion sera para elegir el unimon, necesita la variable dada por abrir_unimon
def elegir_unimon_usr(unimones):
    for i in range(len(unimones)):
        print(f"{i+1}) {unimones[i]}")

    while True:
        try:
            opcion = int(input(f"Elige opción (1-{len(unimones)}): "))

            if opcion < 1 or opcion > len(unimones):
                raise ValueError("Opción fuera de rango")
            break

        except ValueError as e:
            print(e)
    
    return unimones[opcion-1]

# esta funcion es para elegir las habilidades, necesita la variable dada por abrir_habilidad
# tambien necesitara verificar si el pokemon las puede tener, por eso hay una lista despues de las estadisticas de unimon.txt
def elegir_habilidades_usr(unimon, habilidades):
    for i in range(len(unimon.hb_posibles)):
        print(f"{i+1}) {unimon.hb_posibles[i]}")

    # el usuario tiene que escribir una lista
    while True:
        try:
            opciones = list(map(int, input(f"Elige 4 opciones (1-{len(unimon.hb_posibles)}): ").split()))

            if len(opciones) != 4:
                raise ValueError("Numero incorrecto de opciones")
            if len(opciones) != len(set(opciones)):
                raise ValueError("Hay repetidos")
            for opcion in opciones:
                if opcion < 1 or opcion > len(unimon.hb_posibles):
                    raise ValueError(f"Opción {opcion} fuera de rango")
            break
            
        except ValueError as e:
            print(e)

    # va verificando cada opcion
    for opcion in opciones:
        # verifica si la que habilidad se escojio de habilidad.txt, no es lo mas eficiente pero funciona
        for habilidad in habilidades:
            if habilidad.nombre == unimon.hb_posibles[opcion-1]:
                # se va aniadiendo a hb
                unimon.hb.append(habilidad)
                break

    return unimon.hb
    

# las siguientes dos funciones son lo mismo que las anteriores pero con el npc
def elegir_unimon_npc(unimones):
    return unimones[randint(0, len(unimones)-1)]

def elegir_habilidades_npc(unimon, habilidades):
    # se crea una lista igual a la hb_posbiles
    hb_posibles = unimon.hb_posibles.copy()

    while len(unimon.hb) < 4:
        opcion = hb_posibles[randint(0, len(hb_posibles)-1)]

        # verifica si la que habilidad se escojio de habilidad.txt, no es lo mas eficiente pero funciona
        for habilidad in habilidades:
            if habilidad.nombre == opcion:
                # se va aniadiendo a hb
                unimon.hb.append(habilidad)
                break

        # se va eliminando cada elemento que ya se escojio
        hb_posibles.remove(opcion)

    return unimon.hb

# el usuaria elige la habilidad a utilizar
def elegir_turno_usr(unimon):
    # se guarda la longitud de la lista habilidades porque se repite
    l = len(unimon.hb)
    # se imprimen las habilidades
    print(unimon.str_habilidades())
    
    while True:
        try:
            opcion = int(input(f"Elige opción (1-{l}): "))

            if opcion < 1 or opcion > l:
                raise ValueError("Opción fuera de rango")
            break

        except ValueError as e:
            print(e)
    
    # regresa la habilidad seleccionada
    return unimon.hb[opcion-1]

# el npc elige aleatoriamente
def elegir_turno_npc(unimon):
    return unimon.hb[randint(0, len(unimon.hb)-1)]