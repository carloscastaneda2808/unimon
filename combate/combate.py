from combate.equipo import Equipo

class Combate:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    def iniciar_combate(self):
        turno = 0
        

        while True:
            print("Elige tu opcion")
            print("0) Configuracion")
            print("1) Cambiar Unimon") 
            print("2) Habilidades")
            opcion = int(input("opcion:"))
            if opcion == 0:
                print("====Configuracion====")
            if opcion == 1:
                print("====Cambiar====")
            if opcion == 2:
                print("====Habilidades====")
                self.habilidades()

            
            turno += 1

    def cambiar(self):
        print("Elige tu Unimon")
        print(self.equipo1)

    def habilidades(self):
        print("Elige tu habilidad")
        print(self.equipo1)
        
    def __str__(self):
        print(f"")