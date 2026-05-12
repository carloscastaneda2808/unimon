"""
Archivo para los estados
"""
from random import randint
        
def estado_antes(unimon):
    if unimon.estado == "Dormir":
        return dormir(unimon)
    
    if unimon.estado == "Congelado":
        return congelado(unimon)

def estado_despues(unimon):
    if unimon.estado == "Quemado":
        return quemado(unimon)
    
    if unimon.estado == "Envenenado":
        return envenenado(unimon)
    
    if unimon.estado == "GravementeEnvenenado":
        return gravemente_envenenado(unimon)


# aplica el estado de sueño con duracion variable y probabilidad de despertar
def dormir(unimon):
    if unimon.duracion == 0:
        unimon.duracion = 1

    if randint(1, unimon.duracion) == 1:
        unimon.estado = "Dormido"
        unimon.duracion += 1
    else:
        unimon.estado = "Nada"
        unimon.duracion = 0
    
    return unimon

# El Congelado tiene un 20% de probabilidad de descongelarse
def congelado(unimon):

    if randint(1, 100) >= 20:
        unimon.estado = "Congelado"
    else:
        unimon.estado = "Nada"
        
    return unimon

# Quita el 1/16 de vida cada ronda y baja el 50% de daño fisico
def quemado(unimon):

    unimon.hp -= int(unimon.hp_max / 16)
    return unimon

def envenenado(unimon):

    unimon.hp -= int(unimon.hp_max / 6)
    return unimon

def gravemente_envenenado(unimon):
    if unimon.duracion == 0:
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