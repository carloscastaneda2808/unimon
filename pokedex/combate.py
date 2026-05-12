'''
Archivo para el combate
'''

from random import randint

# sirve para ataques de danio solo y escribe un mensaje
def restar_hp(mensaje, habilidad, unimon_atacante, unimon_defensa):
    # verificar la probabilidad (acc)
    if habilidad.acc >= randint(1, 100):
        
        # Evitar el daño de los estados 
        if habilidad.sts == "Nada":
            return None
        
        # Cálcular el daño dependiendo si es Fi
        if habilidad.sts == "Físico":
            danio = (habilidad.poder * unimon_atacante.atk / unimon_defensa.df) // 4 + 2
            if unimon_atacante.estado == "Quemado":
                danio = int(danio / 2)

        if habilidad.sts == "Especial":
            danio = (habilidad.poder * unimon_atacante.spa / unimon_defensa.spd) // 4 + 2

        # verifica si el ataque es del mismo tipo para aplicar bonificacion
        if habilidad.tipo == unimon_atacante.tipo:
            danio = int(danio * 1.2)


        # aplica el multiplicador segun la efectividad entre tipos
        danio *= verifiacar_tipo(unimon_atacante.tipo, unimon_defensa.tipo)

        unimon_defensa.hp -= danio
        habilidad.pp -= 1

        print(f"\nEl {unimon_atacante} de {mensaje} utilizo {habilidad} haciendo {danio} puntos de danio")


    else:
        print(f"\nEl {unimon_atacante} de {mensaje} falló")


# verifica si el unimon esta debilitado y escribe un mensaje, falta poner una variable mensaje como un restar_hp
def verificar_hp(unimon):
    if unimon.hp < 0:
        hp = 0
    else:
        hp = unimon.hp

    print(f"{unimon.nombre} tiene {hp} puntos de HP")
    return unimon.hp <= 0

# devuelve la efectividad del ataque segun los tipos
def verifiacar_tipo(tipo_atk, tipo_def):

    with open("unimon/resources/tipos.txt", "r", encoding="utf-8") as file:
        lineas = file.readlines()

        for linea in lineas:

            if linea.strip() != "":
                dato = linea.split()

                if linea.startswith(tipo_atk) and dato[1] == tipo_def:
                    if dato[2] == "2":
                        print("Es super efectivo")
                    elif dato[2] == "0.5":
                        print("No es muy efectivo")

# [nombre, contador, ]
def verificar_estado(estado):
    if estado[0] <= 0:
