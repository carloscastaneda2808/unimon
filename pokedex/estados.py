"""
Archivo para los estados
"""
from random import randint
class Estado:
    todos = []

    def __init__(self, nombre, atk, acc, tipo, contador):
        self.nombre = nombre
        self.atk = atk
        self.acc = acc
        self.tipo = tipo
        self.contador = contador
    
    def tipo_estado(self):
        pass
        
    # verifica si el unimon tiene algun estado activo
    def verificar_es(self, unimon):
        if unimon.estado == "Dormir":
            return Estado.dormir(unimon)
        
        elif unimon.estado == "Paralizado":
            return Estado.paralizado(unimon)

    # aplica el estado de sueño con duracion variable y probabilidad de despertar
    def dormir(self, unimon):
        
        if unimon.duracion == None:
            unimon.duracion = 1

        if randint(1, unimon.duracion) == 1:
            unimon.estado = "Dormido"
            unimon.duracion += 1
            return unimon
        else:
            unimon.estado = None
            unimon.duracion = None
            return unimon
    
    # El Congelado tiene un 20% de probabilidad de descongelarse
    def Congelado(self, unimon):

        if randint(1, 5) != 2:
            unimon.estado = "Congelado"
            return unimon
        else:
            unimon.estado = None
            return unimon

    # Quita el 1/16 de vida cada ronda y baja el 50% de daño fisico
    def Quemado(self, unimon):

        unimon.hp = unimon.hp - int(unimon.hp / 16)
        return unimon



# contador, probabilidad de contador, 
# redurcir acc, reducir speed, redurcir hp, reducir atk, 
# aumentar (reducir hp), reducir turno, atacarse solo, reducir spa

# estados: paralizado, quemado, envenenado, gravemente envenenado dormido, confundido, congelado, helado