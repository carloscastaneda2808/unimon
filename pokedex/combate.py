'''
Archivo para el combate
'''

from random import randint
from copy import deepcopy
from unimon.pokedex.estados import efecto

# sirve para ataques de danio solo y escribe un mensaje
def restar_hp(mensaje, habilidad, unimon_atacante, unimon_defensa):
    # verificar la probabilidad (acc)
    if habilidad.acc >= randint(1, 100):
        danio = 0
        
        # Cálcular el daño dependiendo si es Fisico
        if habilidad.sts == "Físico":
            danio = (habilidad.poder * unimon_atacante.atk / unimon_defensa.df) // 4 + 2

            # verifica si hay quemado
            if unimon_atacante.estado == "Quemado":
                danio = int(danio / 2)

        # Calcula el daño dependiendo si es Especial
        if habilidad.sts == "Especial":
            danio = (habilidad.poder * unimon_atacante.spa / unimon_defensa.spd) // 4 + 2

        # verifica si el ataque es del mismo tipo para aplicar bonificacion
        if habilidad.tipo == unimon_atacante.tipo:
            danio = int(danio * 1.2)

        # aplica el multiplicador segun la efectividad entre tipos
        mensaje2 = None
        if habilidad.sts != "Estado":
            bonificador, mensaje2 = verificar_habilidad_tipo(habilidad.tipo, unimon_defensa.tipo)
            danio *= bonificador

        # se hacen los calculos
        unimon_defensa.hp -= danio
        habilidad.pp -= 1

        print(f"El {unimon_atacante} de {mensaje} utilizo {habilidad} haciendo {danio} puntos de danio")

        if mensaje2 != None:
            print(mensaje2)

        # verifica si se el estado puede afectar al unimon defensa
        if habilidad.estado != "Nada" and unimon_defensa.estado == "Nada":
            unimon_defensa = efecto(unimon_defensa, habilidad)

    else:
        print(f"El {unimon_atacante} de {mensaje} utilizo {habilidad}, pero falló")


# verifica si el unimon esta debilitado y escribe un mensaje, falta poner una variable mensaje como un restar_hp
def verificar_hp(mensaje, unimon):
    if unimon.hp < 0:
        hp = 0
    else:
        hp = unimon.hp

    print(f"El {unimon.nombre} de {mensaje} tiene {hp} puntos de HP")

    if unimon.estado != "Nada":
        print(f"El {unimon.nombre} de {mensaje} esta {unimon.estado}")

    return unimon.hp <= 0

def debilitado(unimon, equipo, mensaje):
    print(f"El {unimon} de {mensaje} esta debilitado")  
    equipo.remove(unimon)
    return False

# devuelve la efectividad del ataque segun los tipos
def verificar_habilidad_tipo(tipo_atk, tipo_def):

    with open("unimon/resources/tipos.txt", "r", encoding="utf-8") as file:
        lineas = file.readlines()

        for linea in lineas:

            if linea.strip() != "" and not linea.startswith("#"):
                dato = linea.split()

                if dato[0] == tipo_atk and dato[1] == tipo_def:
                    if dato[2] == "1":
                        return float(dato[2]), "Es efectivo"

                    if dato[2] == "2":
                        return float(dato[2]), "Es super efectivo"
                    
                    if dato[2] == "0.5":
                        return float(dato[2]), "No es muy efectivo"
                    
    return float(1), "No encontrado"
                    
def verificar_unimon_tipo(tipo_atk, tipo_def):

    with open("unimon/resources/tipos.txt", "r", encoding="utf-8") as file:
        lineas = file.readlines()

        for linea in lineas:

            if linea.strip() != "" and not linea.startswith("#"):
                dato = linea.split()

                if dato[0] == tipo_atk and dato[1] == tipo_def:
                    if dato[2] == "1":
                        return "Es efectivo"

                    if dato[2] == "2":
                        return "Es super efectivo"
                    
                    if dato[2] == "0.5":
                        return "No es muy efectivo"
                    
    return "No encontrado"
