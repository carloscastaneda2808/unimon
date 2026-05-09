"""
Archivo main
"""

from random import randint
from unimon.io.lectura import leer_unimon, leer_habilidades
from unimon.io.input_validation import elegir_unimon_usr, elegir_habilidades_usr, elegir_unimon_npc, elegir_habilidades_npc, elegir_turno_usr, elegir_turno_npc
from unimon.pokedex.combate import restar_hp, verificar_hp

if __name__ == "__main__":
    while True:
        print("\n===== MENU =====")
        print("1) Iniciar partida")
        print("0) Salir")

        while True:
            try:
                opcion = int(input("Elige opción (0-1): "))

                if opcion < 0 or opcion > 1:
                    raise ValueError("Opción fuera de rango")
                break

            except ValueError as e:
                print(e)
        
        if opcion == 0:
            print("Cerrando juego...")
            break

        elif opcion == 1:
            print("\n===== PARTIDA INICIADA =====")
            print("Elige el unimon")
            leer_unimon()
            unimon_usr = elegir_unimon_usr()

            print("Elige sus habilidades")
            leer_habilidades()
            elegir_habilidades_usr(unimon_usr)

            unimon_npc = elegir_unimon_npc()
            elegir_habilidades_npc(unimon_npc)

            print("\n==== COMBATE ====")
            while True:
                print("1) Habilidades")
                print("0) salir del combate")

                while True:
                    try:
                        opcion2 = int(input("Elige opción (0-1): "))

                        if opcion2 < 0 or opcion2 > 1:
                            raise ValueError("Opción fuera de rango")
                        break

                    except ValueError as e:
                        print(e)

                if opcion2 == 0:
                    print("TE RENDISTE")
                    break
                if opcion2 == 1:
                    turno_usr = elegir_turno_usr(unimon_usr)
                    turno_npc = elegir_turno_npc(unimon_npc)

                    if unimon_usr.spe > unimon_npc.spe:
                        primero = 1
                    elif unimon_usr.spe < unimon_npc.spe:
                        primero = 2
                    else:
                        primero = randint(1, 2)

                    if primero == 1:
                        restar_hp(turno_usr, unimon_usr, unimon_npc)
                        if verificar_hp(unimon_npc):
                            print("GANASTE")
                            break

                        restar_hp(turno_usr, unimon_npc, unimon_usr)
                        if verificar_hp(unimon_usr):
                            print("PERDISTE")
                            break  
                    else:
                        restar_hp(turno_usr, unimon_npc, unimon_usr)
                        if verificar_hp(unimon_usr):
                            print("PERDISTE")
                            break

                        restar_hp(turno_usr, unimon_usr, unimon_npc)
                        if verificar_hp(unimon_npc):
                            print("GANASTE")
                            break
                        
            print("El combate termino...")
            




            



        


            