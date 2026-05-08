import copy

class Equipo:
    def __init__(self, unimon1, unimon2, unimon3):
        self.unimon1 = copy.deepcopy(unimon1)
        self.unimon2 = copy.deepcopy(unimon2)
        self.unimon3 = copy.deepcopy(unimon3)
        


