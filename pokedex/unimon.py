"""
Archivo para crear los unimones
"""

class Unimon:
    todos = []

    def __init__(self, nombre, tipo, hp, atk, df, spe, hb =[]):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spe = spe
        self.hb = hb
        Unimon.todos.append(self)

    def str_stats(self):
        return f"Estadisticas de {self.nombre}\nTipo: {self.tipo}\nHP: {self.hp}\nAtaque: {self.atk}\nDefensa: {self.df}\nVelocidad: {self.spe}"
    
    def str_habilidades(self, longitud):
        cadena = ""
        for i in range(longitud):
           cadena += f"{i}) {self.habilidades[i]}\n"
        
        return cadena

    def __str__(self):
        return f"{self.nombre}"

    


