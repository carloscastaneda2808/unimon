'''
Archivo para leer resources
'''

from copy import deepcopy
from pokedex.unimon import Unimon
from pokedex.habilidad import Habilidad

# Esta función sera para leer y guardar en una variable los datos de unimon.txt
def abrir_unimon():
    with open("resources/unimon.txt", "r", encoding="utf-8") as file:
        # se separa el .txt en lineas
        lineas = file.readlines()
        unimones = []

        # se guarda cada linea como objeto
        for linea in lineas:
            if linea.strip() != "" and not linea.startswith("#"):
                dato = linea.split()

                cadenas = dato[10:]
                objetos = abrir_habilidades()

                # en la variable hb_posbiles se meten las habilidades como objetos
                for i in range(len(cadenas)):
                    for obj in objetos:
                        if cadenas[i] == obj.nombre:
                            cadenas[i] = deepcopy(obj)
                            break

                unimones.append(Unimon(dato[0], dato[1], int(dato[2]), int(dato[3]), int(dato[4]), int(dato[5]), int(dato[6]), int(dato[7]), dato[8], int(dato[9]), cadenas))
    
    return unimones
                
# Esta funcion sera para leer y guardar en una variable los datos de habilidades.txt
def abrir_habilidades():
    with open("resources/habilidad.txt", "r", encoding="utf-8") as file:
        lineas = file.readlines()
        habilidades = []

        for linea in lineas:
            if linea.strip() != "" and not linea.startswith("#"):
                dato = linea.split()
                habilidades.append(Habilidad(dato[0], dato[1], int(dato[2]), int(dato[3]), int(dato[4]), dato[5], dato[6], dato[7]))
    
    return habilidades