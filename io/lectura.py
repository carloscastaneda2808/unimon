'''
Archivo para leer resources
'''

from unimon.pokedex.unimon import Unimon
from unimon.pokedex.habilidad import Habilidad

# Esta función sera para leer y guardar en una variable los datos de unimon.txt
def abrir_unimon():
    with open("unimon/resources/unimon.txt", "r", encoding="utf-8") as file:
        # se separa el .txt en lineas
        lineas = file.readlines()
        unimones = []

        # se guarda cada linea como objeto
        for linea in lineas:
            if linea.strip() != "":
                dato = linea.split()
                unimones.append(Unimon(dato[0], dato[1], int(dato[2]), int(dato[3]), int(dato[4]), int(dato[5]), dato[6:]))
    
    return unimones
                
# Esta funcion sera para leer y guardar en una variable los datos de habilidades.txt
def abrir_habilidades():
    with open("unimon/resources/habilidad.txt", "r", encoding="utf-8") as file:
        lineas = file.readlines()
        habilidades = []

        for linea in lineas:
            if linea.strip() != "":
                dato = linea.split()
                habilidades.append(Habilidad(dato[0], dato[1], int(dato[2]), int(dato[3]), int(dato[4])))
    
    return habilidades