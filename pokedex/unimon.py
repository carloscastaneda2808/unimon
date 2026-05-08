"""
Archivo para crear los unimones
"""

class Unimon:
    todos = []

    def __init__(self, nombre, tipo, hp, atk, df, spe):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spe = spe
        Unimon.todos.append(self)

    def __str__(self):
        return (f"{self.nombre}, {self.tipo}, {self.hp}, {self.atk}, {self.df}, {self.spe}")

    


