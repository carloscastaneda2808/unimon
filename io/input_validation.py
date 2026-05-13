'''
Archivo para validar las entradas
'''

from random import randint
from copy import deepcopy

"""
EQUIPO
"""
def elegir_equipo_usr(unimones, cantidad):
    for i in range(len(unimones)):
        print(f"{i+1}) {unimones[i]}")

    while True:
        try:
            opciones = list(map(int, input(f"Elige {cantidad} opciones (1-{len(unimones)}): ").split()))

            if len(opciones) != cantidad:
                raise ValueError("Numero incorrecto de opciones")
            if len(opciones) != len(set(opciones)):
                raise ValueError("Hay repetidos")
            for opcion in opciones:
                if opcion < 1 or opcion > len(unimones):
                    raise ValueError(f"Opción {opcion} fuera de rango")
            break
            
        except ValueError as e:
            print(e)

    equipo = []
    for opcion in opciones:
        equipo.append(unimones[opcion-1])

    return equipo

"""
HABILIDADES
"""
def elegir_habilidades_usr(equipo, cantidad):

    # se hace por cada unimon del equipo
    for unimon in equipo:
        print(f"\nElige las habilidades de {unimon}")

        for i in range(len(unimon.hb_posibles)):
            print(f"{i+1}) {unimon.hb_posibles[i]}")

        # el usuario tiene que escribir una lista
        while True:
            try:
                opciones = list(map(int, input(f"Elige {cantidad} opciones (1-{len(unimon.hb_posibles)}): ").split()))

                if len(opciones) != cantidad:
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
            # añiade las habilidades posibles seleccionadas en habilidades
            unimon.hb.append(unimon.hb_posibles[opcion-1])

    return equipo

"""
SACAR UNIMON
"""
def elegir_sacar_usr(equipo):
    if len(equipo) > 0:
        print("\n====  SACAR UNIMON =====")
        for i in range(len(equipo)):
            print(f"{i+1}) {equipo[i]}")

        while True:
            try:
                opcion = int(input(f"Elige opción (1-{len(equipo)}): "))

                if opcion < 1 or opcion > len(equipo):
                    raise ValueError("Opción fuera de rango")
                break

            except ValueError as e:
                print(e)

        # no se usa deepcopy para que esten conectadas las variables
        unimon = equipo[opcion-1]
        print(f"Usuario saco a {unimon}")

        return unimon
    
    return "Todos debilitados"

"""
MOVIMIENTO
"""
# el usuaria elige la habilidad a utilizar
def elegir_movimiento_usr(unimon):
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

"""
CANTIDAD
"""
def cantidad_unimones():
    print("\n===== CANTIDAD DE UNIMONES =====")
    while True:
        try:
            opcion = int(input(f"Elige opción (1-10): "))

            if opcion < 1 or opcion > 10:
                raise ValueError("Opción fuera de rango")
            break

        except ValueError as e:
            print(e)
    
    return opcion

def cantidad_habilidades():
    print("\n===== CANTIDAD DE HABILIDADES =====")
    while True:
        try:
            opcion = int(input(f"Elige opción (1-4): "))

            if opcion < 1 or opcion > 4:
                raise ValueError("Opción fuera de rango")
            break

        except ValueError as e:
            print(e)

    return opcion