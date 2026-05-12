"""
Archivo para crear los unimones
"""

class Unimon:
    todos = []

    def __init__(self, nombre, tipo, hp, atk, df, spa , spd , spe, estado, duracion, hb_posibles, hb = None):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.hp_max = hp
        
        self.atk = atk
        self.spa  = spa
        self.df = df
        self.spd  = spd 
        self.spe = spe
        self.estado = estado
        self.duracion = duracion

        self.hb_posibles = hb_posibles
        if hb is None:
            hb = []
        self.hb = hb
        
        Unimon.todos.append(self)

    # se imprime el unimon con sus estadisticas
    def str_stats(self):
        return f"\nEstadisticas de {self.nombre}\nTipo: {self.tipo}\nHP: {self.hp}\nAtaque: {self.atk}\nDefensa: {self.df}\nVelocidad: {self.spe}\nPosibles Habilidades: {self.hb_posibles}"
    
    # se imprimen las habilidades, se utiliza en la funcion elegir_turno_usr
    def str_habilidades(self):
        cadena = ""
        for i in range(len(self.hb)):
           cadena += f"{i+1}) {self.hb[i]}\n"
        
        cadena = cadena[0:-1]
        return cadena

    # solo imprime el nombre
    def __str__(self):
        return f"{self.nombre}"
    


