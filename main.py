"""
Archivo main
"""

from random import randint
from copy import deepcopy
from unimon.io.lectura import abrir_unimon
from unimon.io.input_validation import elegir_equipo_usr, elegir_habilidades_usr, elegir_sacar_usr, elegir_movimiento_usr, cantidad_unimones, cantidad_habilidades
from unimon.pokedex.combate import restar_hp, verificar_hp, debilitado
from unimon.pokedex.estados import estado_antes, estado_danio, verificar_paralizado
from unimon.ia.npc import cambiar_npc, elegir_equipo_npc, elegir_habilidades_npc, elegir_sacar_npc, elegir_movimiento_npc

if __name__ == "__main__":
    # lo principal para que funcione el codigo
    unimones = abrir_unimon()
    cantidad_uni = 6
    cantidad_hb = 4

    # menu principal
    while True:
        print("\n===== MENU =====")
        print("1) Iniciar partida")
        print("2) Estadisticas")
        print("3) Configuracion")
        print("0) Salir")

        while True:
            try:
                opcion = int(input("Elige opción (0-3): "))

                if opcion < 0 or opcion > 3:
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
            gano = "Nada"
            # primero se elige el unimon y las habilides
            print("\n===== ELECCION DEL UNIMON =====")
            equipo_usr = deepcopy(elegir_equipo_usr(unimones, cantidad_uni))

            print("\n===== ELECCION DE LAS HABILIDADES =====")
            elegir_habilidades_usr(equipo_usr, cantidad_hb)

            # el npc elige aleatoriamente
            equipo_npc = deepcopy(elegir_equipo_npc(unimones, cantidad_uni))
            elegir_habilidades_npc(equipo_npc, cantidad_hb)

            unimon_usr = elegir_sacar_usr(equipo_usr)
            unimon_npc = elegir_sacar_npc(equipo_npc)

            # inicio del combate
            print("\n===== COMBATE =====")
            turno = 1
            while True:
                print(f"\n===== TURNO {turno} =====")
                # verifica vida solo para mostrarla
                verificar_hp("Usuario", unimon_usr)
                print("")
                verificar_hp("NPC", unimon_npc)
                print("")
                print("1) Habilidades")
                print("2) Cambiar Unimon")
                print("0) salir del combate")

                while True:
                    try:
                        opcion2 = int(input("Elige opción (0-2): "))

                        if opcion2 < 0 or opcion2 > 2:
                            raise ValueError("Opción fuera de rango")
                        break

                    except ValueError as e:
                        print(e)

                if opcion2 == 0:
                    print("TE RENDISTE")
                    break

                # verificar si puede cambiar
                if opcion2 == 2 and len(equipo_usr) <= 1:
                    opcion2 = 1
                    print("\nNo puedes cambiar de unimon")

                # se puede cambiar la opcion2 si el NPC decide cambiar de pokemon
                if not len(equipo_npc) <= 1:
                    if cambiar_npc(unimon_npc, unimon_usr):
                        if opcion2 == 1:
                            opcion2 = -1
                        elif opcion2 == 2:
                            opcion2 = -2

                # los unimones combate, solo esta la opcion de ataques de daño
                if opcion2 == 1:
                    # se eligen las habilidades a usar, se les llama turno para no repetir nombres
                    print("\n===== ELECCION DE MOVIMIENTO =====")
                    movimiento_usr = elegir_movimiento_usr(unimon_usr)
                    movimiento_npc = elegir_movimiento_npc(unimon_npc) 

                    # verificar si se misminuira la velocidad
                    verificar_paralizado(unimon_usr)
                    verificar_paralizado(unimon_npc)

                    if unimon_usr.spe > unimon_npc.spe:
                        primero = 1
                    elif unimon_usr.spe < unimon_npc.spe:
                        primero = 2
                    # si tiene igual de velocidad es aleatorio
                    else:
                        primero = randint(1, 2)
                        
                    # la habilidad ataca y verifica si el pokemon se ha debilitado para terminar el combate
                    if primero == 1:

                        # Verifica si el Unimon puede actuar (no está dormido, paralizado ni congelado)
                        print("")
                        if not estado_antes(unimon_usr):
                            restar_hp("Usuario", movimiento_usr, unimon_usr, unimon_npc)
                        else:
                            # notifica al usuario porque no atacó
                            print(f"El {unimon_usr} de Usuario pierde turno por estar {unimon_usr.estado}")

                        seguir = True
                        if verificar_hp("NPC", unimon_npc):
                            seguir = debilitado(unimon_npc, equipo_npc, "NPC")
                            unimon_npc = elegir_sacar_npc(equipo_npc)
                            if unimon_npc == "Todos debilitados":
                                gano = "Usuario"
                                break

                        print("")
                        if not estado_antes(unimon_npc) and seguir:
                            restar_hp("NPC", movimiento_npc, unimon_npc, unimon_usr)
                        else:
                            print(f"El {unimon_npc} de NPC pierde turno por estar {unimon_npc.estado}")

                        if verificar_hp("Usuario", unimon_usr) and seguir:
                            debilitado(unimon_usr, equipo_usr, "Usuario")
                            unimon_usr = elegir_sacar_usr(equipo_usr)
                            if unimon_usr == "Todos debilitados":
                                gano = "NPC"
                                break
                    else:
                        print("")
                        if not estado_antes(unimon_npc):
                            restar_hp("NPC", movimiento_npc, unimon_npc, unimon_usr)
                        else:
                            print(f"El {unimon_npc} de NPC pierde turno por estar {unimon_npc.estado}")

                        seguir = True
                        if verificar_hp("Usuario", unimon_usr):
                            seguir = debilitado(unimon_usr, equipo_usr, "Usuario")
                            unimon_usr = elegir_sacar_usr(equipo_usr)
                            if unimon_usr == "Todos debilitados":
                                gano = "NPC"
                                break

                        print("")
                        if not estado_antes(unimon_usr) and seguir:
                            restar_hp("Usuario", movimiento_usr, unimon_usr, unimon_npc)
                        else:
                            print(f"El {unimon_usr} de Usuario pierde turno por estar {unimon_usr.estado}")

                        if verificar_hp("NPC", unimon_npc) and seguir:
                            debilitado(unimon_npc, equipo_npc, "NPC")
                            unimon_npc = elegir_sacar_npc(equipo_npc)
                            if unimon_npc == "Todos debilitados":
                                gano = "Usuario"
                                break

                # USUARIO CAMBIA
                elif opcion2 == 2:
                    movimiento_npc = elegir_movimiento_npc(unimon_npc)
                    unimon_usr = elegir_sacar_usr(equipo_usr)

                    print("")
                    if not estado_antes(unimon_npc):
                        restar_hp("NPC", movimiento_npc, unimon_npc, unimon_usr)
                    else:
                        print(f"El {unimon_npc} de NPC pierde turno por estar {unimon_npc.estado}")

                    if verificar_hp("Usuario", unimon_usr):
                        debilitado(unimon_usr, equipo_usr, "Usuario")
                        unimon_usr = elegir_sacar_usr(equipo_usr)
                        if unimon_usr == "Todos debilitados":
                            break

                # NPC CAMBIA
                elif opcion2 == -1:
                    # se eligen las habilidades a usar, se les llama turno para no repetir nombres
                    print("\n===== ELECCION DE MOVIMIENTO =====")
                    movimiento_usr = elegir_movimiento_usr(unimon_usr)
                    unimon_npc = elegir_sacar_npc(equipo_npc)

                    # Verifica si el Unimon puede actuar (no está dormido, paralizado ni congelado)
                    print("")
                    if not estado_antes(unimon_usr):
                        restar_hp("Usuario", movimiento_usr, unimon_usr, unimon_npc)
                    else:
                        # notifica al usuario porque no atacó
                        print(f"El {unimon_usr} de Usuario pierde turno por estar {unimon_usr.estado}")

                    if verificar_hp("NPC", unimon_npc):
                        debilitado(unimon_npc, equipo_npc, "NPC")
                        unimon_npc = elegir_sacar_npc(equipo_npc)
                        if unimon_npc == "Todos debilitados":
                            break

                # LOS DOS CAMBIAN
                elif opcion2 == -2:
                    print("\n====  SACAR UNIMON =====")
                    unimon_usr = elegir_sacar_usr(equipo_usr)
                    unimon_npc = elegir_sacar_npc(equipo_npc)

                estado_danio(unimon_usr)
                estado_danio(unimon_npc)

                # verificar si alguien murio por los estados de daño
                if unimon_usr.hp <= 0 and unimon_npc.hp <= 0:
                    debilitado(unimon_usr, equipo_usr, "Usuario")
                    unimon_usr = elegir_sacar_usr(equipo_usr)
                    unimon_npc = elegir_sacar_npc(equipo_npc)
                    if unimon_usr == "Todos debilitados" and unimon_npc == "Todos debilitados":
                        gano = "EMPATE"
                        break

                if unimon_usr.hp <= 0:
                    debilitado(unimon_usr, equipo_usr, "Usuario")
                    unimon_usr = elegir_sacar_usr(equipo_usr)
                    if unimon_usr == "Todos debilitados":
                        gano = "NPC"
                        break
                
                if unimon_npc.hp <= 0:
                    debilitado(unimon_npc, equipo_npc, "NPC")
                    unimon_npc = elegir_sacar_npc(equipo_npc)
                    if unimon_npc == "Todos debilitados":
                        gano = "Usuario"
                        break
                turno += 1
            
            if gano == "Usuario":
                print("GANASTE")    
            elif gano == "NPC":
                print("PERDISTE")
            elif gano == "EMPATE":
                print("EMPATE")

            print("El combate termino...")

        elif opcion == 2:
            while True:
                # poner la opcion de imprimir las stats de unimones y habilidades
                print("\n===== ESTADISTICAS =====")
                print("\n0) salir")

                while True:
                    try:
                        opcion2 = int(input("Elige opción (0-0): "))

                        if opcion2 < 0 or opcion2 > 0:
                            raise ValueError("Opción fuera de rango")
                        break

                    except ValueError as e:
                        print(e)
            
                if opcion2 == 0:
                    print("\nSaliendo de estadisticas...")
                    break
    
        elif opcion == 3:
            while True:
                print("\n===== CONFIGURACION =====")
                print("1) Cambiar cantidad de unimones")
                print("2) Cambiar cantidad de habilidades")
                print("0) Salir")

                while True:
                    try:
                        opcion2 = int(input("Elige opción (0-2): "))

                        if opcion2 < 0 or opcion2 > 2:
                            raise ValueError("Opción fuera de rango")
                        break

                    except ValueError as e:
                        print(e)

                if opcion2 == 0:
                    print("\nSaliendo de configuracion...")
                    break

                if opcion2 == 1:
                    cantidad_uni = cantidad_unimones()

                if opcion2 == 2:
                    cantidad_hb = cantidad_habilidades()





            




            



        


            