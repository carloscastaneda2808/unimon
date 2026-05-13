"""
Archivo para los estados
"""
from random import randint
from copy import deepcopy

def efecto(unimon_defensa, habilidad):
    if randint(1, 100) <= int(habilidad.estado_acc):
        unimon_defensa.estado = deepcopy(habilidad.estado)
        
def estado_antes(unimon):
    if unimon.estado == "Dormido":
        return dormdo(unimon)
    
    if unimon.estado == "Congelado":
        return congelado(unimon)
    
    if unimon.estado == "Paralizado":
        return paralizado()
    
    return False

def estado_danio(unimon):
    if unimon.estado == "Quemado":
        return quemado(unimon)
    
    if unimon.estado == "Envenenado":
        return envenenado(unimon)
    
    if unimon.estado == "GravementeEnvenenado":
        return gravemente_envenenado(unimon)


# aplica el estado de sueño con duracion variable y probabilidad de despertar
# modifique esta funcion porque en el pokemon el estado dormido dura entre 1 o 3 turno
# y eso se elige al principio, no cada turno
def dormdo(unimon):

    # se usan numeros negativos para no confundir con duracion de gravemente envenenado
    if unimon.duracion >= 0:
        unimon.duracion = randint(-3, -1)

    if unimon.duracion < 0:
        unimon.estado = "Dormido"
        unimon.duracion += 1
    else:
        unimon.estado = "Nada"
        unimon.duracion = 0
    
    return True

# El Congelado tiene un 20% de probabilidad de descongelarse
def congelado(unimon):

    if randint(1, 100) >= 20:
        unimon.estado = "Congelado"
        return True
    else:
        unimon.estado = "Nada"
        return False

# El Paralizado tiene un 12% de probabilidad de paralizar
def paralizado():

    if randint(1, 100) <= 12:
        return True
    else:
        return False
    
def verificar_paralizado(unimon):
    if unimon.estado == "Paralizado":
        unimon.spe = unimon.spe_max / 2

# Quita el 1/16 de vida cada ronda y baja el 50% de daño fisico
def quemado(unimon):

    unimon.hp -= int(unimon.hp_max / 16)
    return unimon

def envenenado(unimon):

    unimon.hp -= int(unimon.hp_max / 6)
    return unimon

def gravemente_envenenado(unimon):
    if unimon.duracion <= 0:
        unimon.duracion = 1

    unimon.hp -= int((unimon.duracion * unimon.hp_max) / 16)
    unimon.duracion += 1

    if unimon.hp <= 0:
        unimon.duracion = 0

    return unimon


# contador, probabilidad de contador, 
# redurcir acc, reducir speed, redurcir hp, reducir atk, 
# aumentar (reducir hp), reducir turno, atacarse solo, reducir spa

# estados: paralizado, quemado, envenenado, gravemente envenenado dormido, confundido, congelado, helado