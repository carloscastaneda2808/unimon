"""
Archivo para el combate
"""

from random import randint
from copy import copy

from clase.clase_main import Main
from clase.cadena import Cadena

from partida.estado import Estado

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
            movimiento_usr = Main.habilidades[Cadena.main][Main.movimiento_usr]
            movimiento_npc = Main.habilidades[Cadena.main][Main.movimiento_npc]

            if unimon_usr.spe > unimon_npc.spe:
                if Combate.verificar_turno(unimon_usr, movimiento_usr):
                    Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                    Combate.animacion(movimiento_usr, Cadena.NPC)

                if Combate.verificar_turno(unimon_npc, movimiento_npc):
                    Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                    Combate.animacion(movimiento_npc, Cadena.usuario)

            elif unimon_usr.spe < unimon_npc.spe:
                if Combate.verificar_turno(unimon_npc, movimiento_npc):
                    Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                    Combate.animacion(movimiento_npc, Cadena.usuario)

                if Combate.verificar_turno(unimon_usr, movimiento_usr):
                    Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                    Combate.animacion(movimiento_usr, Cadena.NPC)

            else:
                if randint(0, 1):
                    if Combate.verificar_turno(unimon_usr, movimiento_usr):
                        Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                        Combate.animacion(movimiento_usr, Cadena.NPC)

                    if Combate.verificar_turno(unimon_npc, movimiento_npc):
                        Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                        Combate.animacion(movimiento_npc, Cadena.usuario)

                else:
                    if Combate.verificar_turno(unimon_npc, movimiento_npc):
                        Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                        Combate.animacion(movimiento_npc, Cadena.usuario)

                    if Combate.verificar_turno(unimon_usr, movimiento_usr):
                        Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                        Combate.animacion(movimiento_usr, Cadena.NPC)
        
        elif Main.movimiento_usr:
            movimiento_usr = Main.habilidades[Cadena.main][Main.movimiento_usr]
            if Combate.verificar_turno(unimon_usr, movimiento_usr):
                Combate.turno(unimon_usr, unimon_npc, movimiento_usr)
                Combate.animacion(movimiento_usr, Cadena.NPC)
        
        elif Main.movimiento_npc:
            movimiento_npc = Main.habilidades[Cadena.main][Main.movimiento_npc]
            if Combate.verificar_turno(unimon_npc, movimiento_npc):
                Combate.turno(unimon_npc, unimon_usr, movimiento_npc)
                Combate.animacion(movimiento_npc, Cadena.usuario)

        # Actualiza los estados de danio
        Estado.estado_danio(unimon_usr)
        Estado.estado_danio(unimon_npc)

        # limpia los ataques
        Main.movimiento_usr = None
        Main.movimiento_npc = None

        Combate.verificar_partida(unimon_usr, unimon_npc)

    def verificar_partida(unimon_usr, unimon_npc):

        if not unimon_usr.verificar_hp() and not unimon_npc.verificar_hp():
            if not Main.unimones[Cadena.usuario] and not Main.unimones[Cadena.NPC]:
                # Verificar si queda empate
                Main.ventanas_dic = Cadena.main
                Main.vent_actual = Cadena.inicio

                Main.resultado = Cadena.Empate

        if not unimon_usr.verificar_hp():
            Main.unimones[Cadena.usuario].pop(Main.unimon_usr)

            if Main.unimones[Cadena.usuario]:
                # Cambia de ventana a sacar
                Main.ventanas_dic = Cadena.main
                Main.vent_actual = Cadena.sacar
            
            else:
                Main.ventanas_dic = Cadena.main
                Main.vent_actual = Cadena.inicio

                Main.resultado = Cadena.Perdiste

        if not unimon_npc.verificar_hp():
            Main.unimones[Cadena.NPC].pop(Main.unimon_npc)

            if Main.unimones[Cadena.NPC]:
                # Obliga a sacar otro unimon
                NPC.sacar_unimon()
            
            else:
                Main.ventanas_dic = Cadena.main
                Main.vent_actual = Cadena.inicio

                Main.resultado = Cadena.Ganaste


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

            defensa.restar_vida(danio)

        Combate.verificar_estado(defensa, habilidad) 

    def animacion(habilidad, defensa):
        habilidad.dibujar(Main.screen, defensa)

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