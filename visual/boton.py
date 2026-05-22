"""
Archivo para crear botones
"""

import pygame

from copy import copy

from clase.clase_main import Main
from clase.cadena import Cadena

from visual.elemento_ui import ElementoUI
from visual.ventana import Ventana
from visual.texto import Texto

from pokedex.unimon import Unimon
from pokedex.habilidad import Habilidad

from ia.npc import NPC

class Boton(ElementoUI):
    reiniciar = False

    def __init__(self, key, fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto, funcion_1, funcion_2, dic):
        # super() invoca a elementos UI
        super().__init__(fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto)
        self.funcion_1 = funcion_1
        self.funcion_2 = funcion_2
        
        # Se guarda en un diccionario
        if dic not in Main.botones:
            Main.botones[dic] = {}
        Main.botones[dic][key] = self




    # Funciones principales
    def collision(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)
    
    def cambiar_fondo(self, nuevo_fondo):
        if self.imagen:
            self.rect_imagen = nuevo_fondo
        elif self.fondo_color != Main.cian:
            self.fondo_color = nuevo_fondo




    # Funcion para crear botones
    def crear_boton(dic, key, texto, x, y, ancho, altura, funcion_1, funcion_2):
        Boton(key, Main.fuente_3, texto, Main.negro, Main.azul, None, x, y, ancho, altura, funcion_1, funcion_2, dic)

    def crear_botones(dic, botones, funcion_1, funcion_2):
        botones_por_filas = 4
        espacio = Main.ancho / (botones_por_filas + 1)

        for i, key in enumerate(botones):

            columna = i % botones_por_filas
            fila = i // botones_por_filas

            x = espacio * (columna + 1)
            y = 230 + fila * 100

            Boton.crear_boton(dic, key, key, x, y, 200, 60, funcion_1, funcion_2)

    def botones_ventana(botones, ventanas_dic, ventana, dic_elementos):
        for boton in botones:

            Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][5].add(boton)

    def eliminar_boton_ventana(boton, ventana_dic, ventana, dic_elementos):
        Main.ventanas[ventana_dic][ventana].dic_elementos[dic_elementos][5].remove(boton)

    def eliminar_boton(dic, key):
        Main.botones[dic].pop(key)

    def eliminar_botones(dic, keys):
        for key in keys:
            Main.botones[dic].pop(key)




    # Funciones para elegir cosas
    def elegir_unimon(dic, key):
        # Crea diccionario para los unimones del usuario
        Main.crear_diccionario(Main.unimones, Cadena.usuario)

        if len(Main.unimones[Cadena.usuario]) < 6:
            # Aniade el unimon al equipo
            Unimon.copiar_unimon(Cadena.usuario, Cadena.main, key)

            # Cambia de color el boton
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.cian)
        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)

    def descartar_unimon(dic, key):
        boton = Main.botones[dic][key]

        # Verifica si ya habia sido seleccionado
        if boton.fondo_color == Main.cian:
            # Elimina el unimon del equipo
            Unimon.eliminar_unimon(Cadena.usuario, key)

            # Cambia de color el boton
            boton.fondo_color = Main.azul

    def unimon_habilidades(dic, key):
        Main.ventanas_dic = Cadena.elegir_habilidades
        Main.vent_actual = key

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)
        pass

    def elegir_habilidades(dic, key):
        unimon = Main.unimones[Cadena.usuario][Main.vent_actual]

        if len(unimon.hb) < 4:
            unimon.hb.add(key)

            # Diccionario de habilidades usuario
            Main.crear_diccionario(Main.habilidades, Cadena.usuario)
            Habilidad.copiar_habilidad(Cadena.usuario, Cadena.main, key)

            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.cian)
        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)

    def descartar_habilidades(dic, key):
        unimon = Main.unimones[Cadena.usuario][Main.vent_actual]

        if key in unimon.hb:
            unimon.hb.remove(key)

            # Diccionario de habilidades usuario
            Habilidad.eliminar_habilidad(Cadena.usuario, key)

        boton = Main.botones[dic][key]
        boton.fondo_color = Main.azul

    def sacar_unimon(dic, key):
        if key != Main.unimon_usr:

            # Visual
            if Main.unimon_usr:
                Unimon.eliminar_unimon_ventana(Main.unimon_usr, Cadena.main, Cadena.combate, Cadena.usuario)

                if Main.unimon_usr in Main.unimones[Cadena.usuario]:
                    # Funcion NPC
                    NPC.elegir_turno()
                    # Combate
                    Main.combate = True

            Main.ventanas[Cadena.main][Cadena.combate].crear_dic_elementos(Cadena.usuario, None, None, None)
            Main.unimon_usr = key
            Unimon.unimon_ventana(Cadena.usuario, key, Cadena.main, Cadena.combate, Cadena.usuario)
            
            Main.textos[Cadena.main][Cadena.unimon_usr].cambiar_texto(Main.unimon_usr)

            Main.ventanas_dic = Cadena.main
            Main.vent_actual = Cadena.combate

            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.azul)

        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)

    def elegir_movimiento(dic, key):
        Main.movimiento_usr = key

        # Funcion NPC
        NPC.elegir_turno()

        # Combate
        Main.combate = True

        Main.ventanas_dic = Cadena.main
        Main.vent_actual = Cadena.combate

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)




    # Funion para cambiar de ventana
    def ventana_sacar(dic, key):

        if not Main.unimon_usr:
            seguir = True
            unimon = list(Main.unimones[Cadena.usuario].values())[0]
            num_pasado = len(unimon.hb)

            for unimon in Main.unimones[Cadena.usuario].values():
                if len(unimon.hb) != num_pasado or len(unimon.hb) < 1:
                    seguir = False
                    break
                num_pasado = len(unimon.hb)

            if seguir:
                # Modifica la ventana sacar
                Main.ventanas[Cadena.main][Cadena.sacar].crear_dic_elementos(Cadena.b, None, None, Cadena.equipo)
                Main.crear_diccionario(Main.botones, Cadena.equipo)
                Boton.crear_botones(Cadena.equipo, Main.unimones[Cadena.usuario].keys(), Boton.sacar_unimon, None)
                Boton.botones_ventana(Main.unimones[Cadena.usuario].keys(), Cadena.main, Cadena.sacar, Cadena.b)
                
                # Crea ventanas para cada unimon
                Main.crear_diccionario(Main.ventanas, Cadena.equipo)
                Main.crear_diccionario(Main.textos, Cadena.equipo)

                for nombre, value in Main.unimones[Cadena.usuario].items():
                    Ventana.crear_ventana(Cadena.equipo, nombre, {Cadena.a : [None, None, Cadena.equipo, set(), Cadena.main, {Cadena.atras_4}]})
                    Main.ventanas[Cadena.equipo][nombre].crear_dic_elementos(Cadena.b, None, None, f"{nombre}_{Cadena.equipo}")

                    Texto.crear_titulo(Cadena.equipo, nombre, nombre)
                    Texto.texto_ventana(nombre, Cadena.equipo, nombre, Cadena.a)

                    Main.crear_diccionario(Main.botones, f"{nombre}_{Cadena.equipo}")
                    Boton.crear_botones(f"{nombre}_{Cadena.equipo}", value.hb, Boton.elegir_movimiento, None)
                    Boton.botones_ventana(value.hb, Cadena.equipo, nombre, Cadena.b)

                # Funcion del NPC
                NPC.elegir_habilidades()
                Main.ventanas[Cadena.main][Cadena.combate].crear_dic_elementos(Cadena.b, None, None, None)
                NPC.sacar_unimon()

                Main.ventanas_dic = Cadena.main
                Main.vent_actual = Cadena.sacar

                boton = Main.botones[dic][key]
                boton.cambiar_fondo(Main.azul)
            else:
                boton = Main.botones[dic][key]
                boton.cambiar_fondo(Main.rojo)

        elif len(Main.unimones[Cadena.usuario]) > 1 and not Main.timer:
            Main.ventanas_dic = Cadena.main
            Main.vent_actual = Cadena.sacar

            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.azul)

        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)

    def ventana_elegir_habilidades(dic, key):
        Main.crear_diccionario(Main.unimones, Cadena.usuario)

        # if Cadena.elegir_habilidades not in Main.botones:
        if len(Main.unimones[Cadena.usuario]) > 0:
            # reinicia la ventana elegir habilidades
            Ventana("elegir_habilidades",
            {"a" : 
             ["main", {"inicio"},
            "main", {"elegir_habilidades"},
            "main", {"atras_2", "seguir_2"}]},
            "main")

            # Modifica la ventana sacar
            Main.ventanas[Cadena.main][Cadena.elegir_habilidades].crear_dic_elementos(Cadena.b, None, None, Cadena.elegir_habilidades)
            Main.crear_diccionario(Main.botones, Cadena.elegir_habilidades)
            Boton.crear_botones(Cadena.elegir_habilidades , Main.unimones[Cadena.usuario].keys(), Boton.unimon_habilidades, None)
            Boton.botones_ventana(Main.unimones[Cadena.usuario].keys(), Cadena.main, Cadena.elegir_habilidades, Cadena.b)

            # Crea ventanas para cada unimon
            Main.crear_diccionario(Main.ventanas, Cadena.elegir_habilidades)
            Main.crear_diccionario(Main.textos, Cadena.elegir_habilidades)

            for nombre, value in Main.unimones[Cadena.usuario].items():
                value.cambiar_back()

                Ventana.crear_ventana(Cadena.elegir_habilidades, nombre, {Cadena.a : [None, None, Cadena.elegir_habilidades, set(), Cadena.main, {Cadena.atras_5}]})
                Main.ventanas[Cadena.elegir_habilidades][nombre].crear_dic_elementos(Cadena.b, None, None, f"{nombre}_{Cadena.elegir_habilidades}")

                Texto.crear_titulo(Cadena.elegir_habilidades, nombre, nombre)
                Texto.texto_ventana(nombre, Cadena.elegir_habilidades, nombre, Cadena.a )

                Main.crear_diccionario(Main.botones, f"{nombre}_{Cadena.elegir_habilidades}")
                Boton.crear_botones(f"{nombre}_{Cadena.elegir_habilidades}", value.hb_posibles, Boton.elegir_habilidades, Boton.descartar_habilidades)
                Boton.botones_ventana(value.hb_posibles, Cadena.elegir_habilidades, nombre, Cadena.b)

            # Funcion del NPC
            NPC.elegir_equipo()

            Main.ventanas_dic = Cadena.main
            Main.vent_actual = Cadena.elegir_habilidades

            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.azul)
        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)
        
        # else:
        #     Main.ventanas_dic = Cadena.main
        #     Main.vent_actual = Cadena.elegir_habilidades

        #     boton = Main.botones[dic][key]
        #     boton.cambiar_fondo(Main.azul)

    def ventana_atacar(dic, key):

        if not Main.timer:
            Main.ventanas_dic = Cadena.equipo
            Main.vent_actual = Main.unimon_usr

            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.azul)
        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)

    def ventana_inicio(dic, key):

        # Reinicio
        Boton.reiniciar = True

    def ventana_elegir_unimones(dic, key):
        Main.ventanas_dic = Cadena.main
        Main.vent_actual = Cadena.elegir_unimones

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    def ventana_estadisticas(dic, key):
        Main.ventanas_dic = Cadena.main
        Main.vent_actual = Cadena.estadisticas

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    def ventana_configuracion(dic, key):
        Main.ventanas_dic = Cadena.main
        Main.vent_actual = Cadena.configuracion

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    def ventana_combate(dic, key):
        Main.ventanas_dic = Cadena.main
        Main.vent_actual = Cadena.combate

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)
    
    def ventana_salir(dic, key):
        pygame.quit()
        exit()
