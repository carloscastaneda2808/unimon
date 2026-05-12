"""
Archivo para los estados
"""
from random import randint
class Estado:
    todos = []

    def __init__(self, nombre, atk, acc, tipo, contador, duracion_dormir, duracion_toxico):
        self.nombre = nombre
        self.atk = atk
        self.acc = acc
        self.tipo = tipo
        self.contador = contador

        if duracion_dormir is None:
            duracion_dormir = 0
        self.duracion_dormir = duracion_dormir

        if duracion_toxico is None:
            duracion_toxico = 0
        self.duracion_toxico = duracion_toxico

    def tipo_estado(self):
        pass
        
    # verifica si el unimon tiene algun estado activo
    def verificar_es(self, unimon):
        if unimon.estado == "Dormir":
            return Estado.dormir(unimon)
        
        elif unimon.estado == "Paralizado":
            return Estado.congelado(unimon)
        
        elif unimon.estado == "Quemado":
            return Estado.quemado(unimon)
        
        elif unimon.estado == "GravementeEnvenenado":
            return Estado.gravemente_envenenado(unimon)

    # aplica el estado de sueño con duracion variable y probabilidad de despertar
    def dormir(self, unimon):
        
        if Estado.duracion_dormir == None:
            Estado.duracion_dormir = 1

        if randint(1, Estado.duracion_dormir) == 1:
            unimon.estado = "Dormido"
            Estado.duracion_dormir += 1
            return unimon
        else:
            unimon.estado = None
            Estado.duracion_dormir = None
            return unimon
    
    # El Congelado tiene un 20% de probabilidad de descongelarse
    def congelado(self, unimon):

        if randint(1, 100) >= 20:
            unimon.estado = "Congelado"
            return unimon
        else:
            unimon.estado = None
            return unimon

    # Quita el 1/16 de vida cada ronda y baja el 50% de daño fisico
    def quemado(self, unimon):

        unimon.hp -= int(unimon.hp_max / 16)
        return unimon

    def envenenado(self, unimon):

        unimon.hp -= int(unimon.hp_max / 6)
        return unimon
    
    def gravemente_envenenado(self, unimon):

        if Estado.duracion_toxico == None:
            Estado.duracion_toxico = 1

        unimon.hp -= int((Estado.duracion_toxico * unimon.hp_max) / 16)
        Estado.duracion_toxico += 1

        if unimon.hp <= 0:
            Estado.duracion_toxico = None

        return unimon
    

# contador, probabilidad de contador, 
# redurcir acc, reducir speed, redurcir hp, reducir atk, 
# aumentar (reducir hp), reducir turno, atacarse solo, reducir spa

# estados: paralizado, quemado, envenenado, gravemente envenenado dormido, confundido, congelado, helado