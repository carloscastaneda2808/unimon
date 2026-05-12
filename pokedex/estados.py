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
        

    def verificar_es(self, unimon):
        if unimon.estado == "Dormir":
            return Estado.dormir(unimon)

    def dormir(self, unimon, i = None):

        if i == None:
            i = 1

        if randint(1, i) == 1:
            unimon.estado = "Dormido"
            i += 1
            return unimon
        else:
            unimon.estado = None
            i = 1
            return unimon



# contador, probabilidad de contador, 
# redurcir acc, reducir speed, redurcir hp, reducir atk, 
# aumentar (reducir hp), reducir turno, atacarse solo, reducir spa

# estados: paralizado, quemado, envenenado, gravemente envenenado dormido, confundido, congelado, helado