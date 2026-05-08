import copy

class Equipo:
    def __init__(self, unimon1, unimon2, unimon3):
        self.unimon1 = copy.deepcopy(unimon1)
        self.unimon2 = copy.deepcopy(unimon2)
        self.unimon3 = copy.deepcopy(unimon3)

    def __str__(self):
        return f"{self.unimon1.nombre}\n{self.unimon2.nombre}\n{self.unimon3.nombre}\n"
    
    def str_habilidades(self):
        return f"{self.unimon1.habilidad}\n{self.unimon1.nombre}\n{self.unimon1.nombre}\n"
    

class UnimonHabilidades
        


