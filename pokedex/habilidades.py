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

    # imprime las estadisticas de la habilidad
    def str_stats(self):
        return f"Estadisticas de {self.nombre}\nTipo: {self.tipo}\nPoder: {self.poder}\nPP: {self.pp}\nPresicion: {self.acc}"

    # solo imprime el nombre
    def __str__(self):
        return f"{self.nombre}"