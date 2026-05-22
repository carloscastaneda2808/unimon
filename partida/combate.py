"""
Archivo para el combate
"""

from random import randint
from copy import copy

from clase.clase_main import Main
from clase.cadena import Cadena

from partida.estado import Estado
from pokedex.habilidad import Habilidad

from visual.boton import Boton

from ia.npc import NPC

class Combate:
    def combate():
        unimon_usr = Main.unimones[Cadena.usuario][Main.unimon_usr]
        unimon_npc = Main.unimones[Cadena.NPC][Main.unimon_npc]

        # Actualiza los estado de antes
        Estado.estado_antes(unimon_usr)
        Estado.estado_antes(unimon_npc)

        # Verifica reducciones de estadisticas por estados
        Estado.paralizado_speed(unimon_usr)
        Estado.paralizado_speed(unimon_npc)

        Estado.quemado_atk_fisico(unimon_usr)
        Estado.quemado_atk_fisico(unimon_npc)

        if Main.movimiento_usr and Main.movimiento_npc:
            movimiento_usr = Main.habilidades[Cadena.usuario][Main.movimiento_usr]
            movimiento_npc = Main.habilidades[Cadena.NPC][Main.movimiento_npc]

            if unimon_usr.spe > unimon_npc.spe:
                if Combate.verificar_turno(unimon_usr, movimiento_usr):
                    Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                    Combate.animacion_habilidad(Main.movimiento_usr, Cadena.usuario, True)

                if Combate.verificar_turno(unimon_npc, movimiento_npc):
                    Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                    Combate.animacion_habilidad(Main.movimiento_npc, Cadena.NPC, False)

            elif unimon_usr.spe < unimon_npc.spe:
                if Combate.verificar_turno(unimon_npc, movimiento_npc):
                    Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                    Combate.animacion_habilidad(Main.movimiento_npc, Cadena.NPC, True)

                if Combate.verificar_turno(unimon_usr, movimiento_usr):
                    Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                    Combate.animacion_habilidad(Main.movimiento_usr, Cadena.usuario, False)

            else:
                if randint(0, 1):
                    if Combate.verificar_turno(unimon_usr, movimiento_usr):
                        Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                        Combate.animacion_habilidad(Main.movimiento_usr, Cadena.usuario, True)

                    if Combate.verificar_turno(unimon_npc, movimiento_npc):
                        Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                        Combate.animacion_habilidad(Main.movimiento_npc, Cadena.NPC, False)

                else:
                    if Combate.verificar_turno(unimon_npc, movimiento_npc):
                        Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                        Combate.animacion_habilidad(Main.movimiento_npc, Cadena.NPC, True)

                    if Combate.verificar_turno(unimon_usr, movimiento_usr):
                        Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                        Combate.animacion_habilidad(Main.movimiento_usr, Cadena.usuario, False)
        
        elif Main.movimiento_usr:
            movimiento_usr = Main.habilidades[Cadena.usuario][Main.movimiento_usr]

            if Combate.verificar_turno(unimon_usr, movimiento_usr):
                Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                Combate.animacion_habilidad(Main.movimiento_usr, Cadena.usuario, True)
        
        elif Main.movimiento_npc:
            movimiento_npc = Main.habilidades[Cadena.NPC][Main.movimiento_npc]

            if Combate.verificar_turno(unimon_npc, movimiento_npc):
                Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                Combate.animacion_habilidad(Main.movimiento_npc, Cadena.NPC, True)

        # Actualiza los estados de danio
        Estado.estado_danio(unimon_usr)
        Estado.estado_danio(unimon_npc)

        # Animacion
        Combate.animacion_debilitado(unimon_usr)
        Combate.animacion_debilitado(unimon_npc)

        # limpia los ataques
        Main.movimiento_usr = None
        Main.movimiento_npc = None

    def verificar_turno(atacante, habilidad):
        if atacante.verificar_hp():

            if atacante.estado != Cadena.Dormido and atacante.estado != Cadena.Congelado:

                if not Estado.paralizado(atacante):

                    if habilidad.acc >= randint(1, 100):
                        
                        return True
                    
        return False

    def turno(atacante, defensa, habilidad):
        if habilidad.sts != Cadena.Estado:
            danio = 0

            if habilidad.sts == Cadena.Físico:
                danio = (habilidad.poder * atacante.atk_fisico / defensa.df_fisico) // 4 + 2

            if habilidad.sts == Cadena.Especial:
                danio = (habilidad.poder * atacante.atk_especial / defensa.df_especial) // 4 + 2

            if habilidad.tipo == atacante.tipo:
                danio = danio * 1.5

            if Combate.verificar_tipos(habilidad, defensa) == Cadena.muy_efectivo:
                danio *= 2

            elif Combate.verificar_tipos(habilidad, defensa) == Cadena.poco_efectivo:
                danio = danio / 2

            defensa.restar_hp(danio)

        Combate.verificar_estado(defensa, habilidad) 

    def animacion_habilidad(habilidad, jugador, primero):
        value = Main.habilidades[jugador][habilidad]
        Main.timer = 1
        Main.timer_terminar = 200

        if primero:
            value.usando_timer = True
            value.empieza = 0
            value.termina = 60
        else:
            value.usando_timer = True
            value.empieza = 70
            value.termina = 130

        if jugador == Cadena.usuario:
            value.cambiar_front()
        else:
            value.cambiar_back()

        Habilidad.limpiar_habilidad_ventana(Cadena.main, Cadena.combate, jugador)
        Habilidad.habilidad_ventana(jugador, habilidad, Cadena.main, Cadena.combate, jugador)

    def animacion_debilitado(unimon):
        if not unimon.verificar_hp():

            unimon.usando_timer = True
            unimon.empieza = 140
            unimon.termina = 200

    def verificar_partida():
        unimon_usr = Main.unimones[Cadena.usuario][Main.unimon_usr]
        unimon_npc = Main.unimones[Cadena.NPC][Main.unimon_npc]

        # Verificar si queda empate
        if not unimon_usr.verificar_hp() and not unimon_npc.verificar_hp():
            if not Main.unimones[Cadena.usuario] and not Main.unimones[Cadena.NPC]:

                Main.resultado = Cadena.Empate

                # Texto resultado
                Main.textos[Cadena.main][Cadena.resultado].cambiar_texto(Main.resultado)

                # Cambiar ventana
                Main.ventanas_dic = Cadena.main
                Main.vent_actual = Cadena.resultado

        if not unimon_usr.verificar_hp():
            Main.unimones[Cadena.usuario].pop(Main.unimon_usr)

            if Main.unimones[Cadena.usuario]:
                # Cambia de ventana a sacar
                Main.ventanas_dic = Cadena.main
                Main.vent_actual = Cadena.sacar
            
            else:

                Main.resultado = Cadena.Perdiste

                # Texto resultado
                Main.textos[Cadena.main][Cadena.resultado].cambiar_texto(Main.resultado)

                # Cambiar ventana
                Main.ventanas_dic = Cadena.main
                Main.vent_actual = Cadena.resultado


        if not unimon_npc.verificar_hp():
            Main.unimones[Cadena.NPC].pop(Main.unimon_npc)

            if Main.unimones[Cadena.NPC]:
                # Obliga a sacar otro unimon
                NPC.sacar_unimon()
            
            else:

                Main.resultado = Cadena.Ganaste

                # Texto resultado
                Main.textos[Cadena.main][Cadena.resultado].cambiar_texto(Main.resultado)

                # Cambiar ventana
                Main.ventanas_dic = Cadena.main
                Main.vent_actual = Cadena.resultado

    def verificar_tipos(tipo_1, tipo_2):
        
        with open("resources/tipos.txt", "r", encoding = "utf-8") as file:
            lineas = file.readlines()

            for linea in lineas:

                if linea.strip() != "" and not linea.startswith("#"):
                    dato = linea.split()

                    if dato[0] == tipo_1 and dato[1] == tipo_2:
                        if dato[2] == "1":
                            return Cadena.efectivo
                        
                        if dato[2] == "2":
                            return Cadena.muy_efectivo
                        
                        if dato[2] == "0.5":
                            return Cadena.poco_efectivo

    def verificar_estado(unimon, habilidad):
        if habilidad.estado != Cadena.Nada and unimon.estado == Cadena.Nada:
            
            if habilidad.estado_acc >= randint(1, 100):
                unimon.estado = copy(habilidad.estado)