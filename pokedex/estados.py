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
        

    def dormir(self, nombre, probabilidad):


# contador, probabilidad de contador, 
# redurcir acc, reducir speed, redurcir hp, reducir atk, 
# aumentar (reducir hp), reducir turno, atacarse solo, reducir spa

# estados: paralizado, quemado, envenenado, gravemente envenenado dormido, confundido, congelado, helado