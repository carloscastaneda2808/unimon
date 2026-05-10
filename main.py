"""
Archivo main
"""

from random import randint
from copy import deepcopy
from unimon.io.lectura import abrir_unimon, abrir_habilidades
from unimon.io.input_validation import elegir_unimon_usr, elegir_habilidades_usr, elegir_unimon_npc, elegir_habilidades_npc, elegir_turno_usr, elegir_turno_npc
from unimon.pokedex.combate import restar_hp, verificar_hp

if __name__ == "__main__":
    # menu principal
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
        
        # inicio de una partida
        elif opcion == 1:
            print("\n===== PARTIDA INICIADA =====")
            # primero se elige el unimon y las habilides
            print("\n===== ELECCION DEL UNIMON =====")
            unimones = abrir_unimon()
            unimon_usr = deepcopy(elegir_unimon_usr(unimones))

            print("\n===== ELECCION DE LAS HABILIDADES =====")
            habilidades = abrir_habilidades()
            elegir_habilidades_usr(unimon_usr, habilidades)

            # el npc elige aleatoriamente
            unimon_npc = deepcopy(elegir_unimon_npc(unimones))
            elegir_habilidades_npc(unimon_npc, habilidades)

            print(f"\nTu elegiste a {unimon_usr.nombre}")
            print(f"NPC eligio a {unimon_npc.nombre}")

            # inicio del combate
            print("\n===== COMBATE =====")
            turno = 1
            while True:
                print(f"\n===== TURNO {turno} =====")
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

                # los unimones combate, solo esta la opcion de ataques de daño
                if opcion2 == 1:
                    # se eligen las habilidades a usar, se les llama turno para no repetir nombres
                    print("\n===== ELECCION DE TURNO =====")
                    turno_usr = elegir_turno_usr(unimon_usr)
                    turno_npc = elegir_turno_npc(unimon_npc)

                    # Verifica todos lo casos para saber quien va primero
                    if unimon_usr.spe > unimon_npc.spe:
                        primero = 1
                    elif unimon_usr.spe < unimon_npc.spe:
                        primero = 2
                    # si tiene igual de velocidad es aleatorio
                    else:
                        primero = randint(1, 2)

                    # la habilidad ataca y verifica si el pokemon se ha debilitado para terminar el combate
                    if primero == 1:
                        restar_hp("Usuario", turno_usr, unimon_usr, unimon_npc)
                        if verificar_hp(unimon_npc):
                            print("GANASTE")
                            break

                        restar_hp("NPC", turno_npc, unimon_npc, unimon_usr)
                        if verificar_hp(unimon_usr):
                            print("PERDISTE")
                            break  
                    else:
                        restar_hp("NPC", turno_npc, unimon_npc, unimon_usr)
                        if verificar_hp(unimon_usr):
                            print("PERDISTE")
                            break

                        restar_hp("Usuario", turno_usr, unimon_usr, unimon_npc)
                        if verificar_hp(unimon_npc):
                            print("GANASTE")
                            break

                # incrementa en uno para saber en que turno esta
                turno += 1
                        
            print("El combate termino...")
            




            



        


            