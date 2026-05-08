"""
Archivo para hacer las habilidades
"""

class Habilidades:
    todos = []
    
    def __init__(self, nombre, tipo, poder, pp, acc):
        self.nombre = nombre
        self.tipo = tipo
        self.poder = poder
        self.pp = pp
        self.acc = acc
        Habilidades.todos.append(self)