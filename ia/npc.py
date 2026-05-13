"""
Archivo para la IA
"""

from random import randint
from unimon.pokedex.combate import verificar_unimon_tipo
from copy import deepcopy

"""
EQUIPO
"""
def elegir_equipo_npc(unimones, cantidad):
    # se crea una lista igual a unimones y un equipo vacio
    unimones_copy = deepcopy(unimones)
    equipo = []

    while len(equipo) < cantidad:
        opcion = unimones_copy[randint(0, len(unimones_copy)-1)]
        equipo.append(opcion)

        # se va eliminando cada elemento que ya se escojio
        unimones_copy.remove(opcion)

    return equipo

"""
HABILIDADES
"""
def elegir_habilidades_npc(equipo, cantidad):
    for unimon in equipo:
        hb_posibles = unimon.hb_posibles.copy()

        unimon.hb = []
        while len(unimon.hb) < cantidad:
            opcion = hb_posibles[randint(0, len(hb_posibles)-1)]

            # añiade la opcion a habilidades
            unimon.hb.append(opcion)

            # se va eliminando cada elemento que ya se escojio
            hb_posibles.remove(opcion)

    return equipo

"""
SACAR UNIMON
"""
def elegir_sacar_npc(equipo):
    if len(equipo) > 0:
        return equipo[randint(0, len(equipo)-1)]
    
    return "Todos debilitados"

"""
MOVIMIENTO
"""
# el npc elige aleatoriamente
def elegir_movimiento_npc(unimon):
    return unimon.hb[randint(0, len(unimon.hb)-1)]

"""
CAMBIAR
"""
def cambiar_npc(unimon_npc, unimon_usr):
    acc = 10
    if unimon_npc.hp < unimon_npc.hp_max / 4:
        acc += 10

    if verificar_unimon_tipo(unimon_usr.tipo, unimon_npc.tipo) == "Es super efectivo":
        acc += 10

    if verificar_unimon_tipo(unimon_npc.tipo, unimon_usr.tipo) == "No es muy efectivo":
        acc += 10
        
    return acc >= randint(1, 100)