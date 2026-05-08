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

    def str_stats(self):
        stats = ''
        stats 
        return (f"{self.nombre}")
    
    def str_unimon(self):
        return self.nombre

    def __str__(self):
        
        return (f"Nombre: {self.nombre}, Tipo: {self.tipo}, Vida: {self.hp}, Ataque: {self.atk}, Defensa: {self.df}, Velocidad: {self.spe}")
        
    def mostrar_todos(cls):
        for pokemon in cls.todos:
            print(pokemon)


