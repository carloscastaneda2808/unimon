"""
Archivo para crear botones
"""

import pygame

from copy import copy

from clase_main import Main
from visual.elemento_ui import ElementoUI
from visual.ventana import Ventana
from visual.texto import Texto

from pokedex.unimon import Unimon
from pokedex.habilidad import Habilidad

class Boton(ElementoUI):

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

    # Funcion para crear objetos
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

    def seleccionar_1(dic, key):
        Main.crear_diccionario(Main.unimones, "usuario")

        if len(Main.unimones["usuario"]) < 6:
            # Crea diccionario para los unimones del usuario
            Unimon.copiar_unimon("usuario", "main", key)
            Main.unimones["usuario"][key].cambiar_back()

            # Crea el diccionario para los botones de la ventana elegir_habilidades
            Main.crear_diccionario(Main.botones, "elegir_habilidades")
            Boton.crear_botones("elegir_habilidades", Main.unimones["usuario"].keys(), Boton.seleccionar_2, None)

            # Se crea en la ventana elegir_habilidades el diccionario de elementos "b"
            Main.ventanas["main"][Main.vent_3].crear_dic_elementos("b", None, None, "elegir_habilidades")
            Boton.botones_ventana(Main.botones["elegir_habilidades"], "main", Main.vent_3, "b")



            # VENTANA DE CADA UNIMON
            unimon = Main.unimones["usuario"][key]

            # Crea la ventana de cada unimon de elegir habilidades
            Main.crear_diccionario(Main.ventanas, "elegir_habilidades")
            Ventana.crear_ventana("elegir_habilidades", f"{key}_elegir_habilidades", {"a": [None, None, "elegir_habilidades", set(), "main", {"atras_5"}]})
            Main.ventanas["elegir_habilidades"][f"{key}_elegir_habilidades"].crear_dic_elementos("b", None, None, f"{key}_elegir_habilidades")

            # Crea los textos para cada unimon
            Main.crear_diccionario(Main.textos, "elegir_habilidades")
            Texto.crear_titulo("elegir_habilidades", f"{key}_elegir_habilidades", key)
            Texto.texto_ventana(f"{key}_elegir_habilidades", "elegir_habilidades", f"{key}_elegir_habilidades", "a")

            # Crea los botones de cada unimon de sus habilidades posibles
            Main.crear_diccionario(Main.botones, f"{key}_elegir_habilidades")
            Boton.crear_botones(f"{key}_elegir_habilidades", unimon.hb_posibles, Boton.seleccionar_3, Boton.deseleccionar_3)
            Boton.botones_ventana(unimon.hb_posibles, "elegir_habilidades", f"{key}_elegir_habilidades", "b")

            # Cambia de color el boton
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.cian)
        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)

    def deseleccionar_1(dic, key):
        boton = Main.botones[dic][key]
        # Verifica si ya habia sido seleccionado
        if boton.fondo_color == Main.cian:
            unimon = Main.unimones["usuario"][key]

            # VENTANA DE ELEGIR HABILIDADES
            # Elimina el unimon del equipo
            Unimon.eliminar_unimon("usuario", key)

            # Elimina los botones
            Boton.eliminar_boton("elegir_habilidades", key)

            # Se elimina el boton de la ventana
            Boton.eliminar_boton_ventana(key, "main", Main.vent_3, "b")



            # VENTANA DE CADA UNIMON
            # Eliminar ventana del unimon
            Ventana.eliminar_ventana("elegir_habilidades", f"{key}_elegir_habilidades")

            # Eliminar texto
            Texto.eliminar_texto("elegir_habilidades", f"{key}_elegir_habilidades")

            # Eliminar los botones del unimon
            Boton.eliminar_botones(f"{key}_elegir_habilidades", unimon.hb_posibles)

            # Cambia de color el boton
            boton.fondo_color = Main.azul

    def seleccionar_2(dic, key):
        Main.ventanas_dic = "elegir_habilidades"
        Main.vent_actual = f"{key}_elegir_habilidades"

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)
        pass

    def seleccionar_3(dic, key):
        unimon_nombre = dic[:-19]
        unimon = Main.unimones["usuario"][unimon_nombre]

        if len(unimon.hb) < 4:
            unimon.hb.add(key)

            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.cian)
        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)

    def deseleccionar_3(dic, key):
        unimon_nombre = dic[:-19]
        unimon = Main.unimones["usuario"][unimon_nombre]

        if key in unimon.hb:
            unimon.hb.remove(key)

        boton = Main.botones[dic][key]
        boton.fondo_color = Main.azul

    def ventana_sacar(dic, key):
        seguir = True
        unimon = list(Main.unimones["usuario"].values())[0]
        num_pasado = len(unimon.hb)

        for unimon in Main.unimones["usuario"].values():
            if len(unimon.hb) != num_pasado or len(unimon.hb) < 1:
                seguir = False
                break
            num_pasado = len(unimon.hb)

        if seguir:
            # Modifica la ventana sacar
            Main.ventanas["main"]["sacar"].crear_dic_elementos("b", None, None, "equipo")
            Main.crear_diccionario(Main.botones, "equipo")
            Boton.crear_botones("equipo", Main.unimones["usuario"].keys(), Boton.seleccionar_4, None)
            Boton.botones_ventana(Main.unimones["usuario"].keys(), "main", "sacar", "b")
            
            # Crea ventanas para cada unimon
            Main.crear_diccionario(Main.ventanas, "equipo")
            Main.crear_diccionario(Main.textos, "equipo")

            for nombre, value in Main.unimones["usuario"].items():
                Ventana.crear_ventana("equipo", nombre, {"a" : [None, None, "equipo", set(), "main", {"atras_4"}]})
                Main.ventanas["equipo"][nombre].crear_dic_elementos("b", None, None, f"{nombre}_equipo")

                Texto.crear_titulo("equipo", nombre, nombre)
                Texto.texto_ventana(nombre, "equipo", nombre, "a")

                Main.crear_diccionario(Main.botones, f"{nombre}_equipo")
                Boton.crear_botones(f"{nombre}_equipo", value.hb, Boton.seleccionar_5, None)
                Boton.botones_ventana(value.hb, "equipo", nombre, "b")

            Main.ventanas_dic = "main"
            Main.vent_actual = copy(Main.vent_8)

            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.azul)
        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)

    def seleccionar_4(dic, key):
        if Main.unimon_usr:
            Unimon.eliminar_unimon_ventana("usuario", Main.unimon_usr, "main", "combate", "a")

        Main.unimon_usr = key
        Unimon.unimon_ventana("usuario", key, "main", "combate", "a")

        Main.ventanas_dic = "main"
        Main.vent_actual = "combate"

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    def seleccionar_5(dic, key):
        Main.movimiento_usr = key

        Main.ventanas_dic = "main"
        Main.vent_actual = "combate"

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    def ventana_atacar(dic, key):
        Main.ventanas_dic = "equipo"
        Main.vent_actual = copy(Main.unimon_usr)

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    # Funciones de los botones
    def ventana_inicio(dic, key):
        Main.ventanas_dic = "main"
        Main.vent_actual = copy(Main.vent_1)

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    def ventana_elegir_unimones(dic, key):
        Main.ventanas_dic = "main"
        Main.vent_actual = copy(Main.vent_2)

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    def ventana_elegir_habilidades(dic, key):
        Main.crear_diccionario(Main.unimones, "usuario")
        if len(Main.unimones["usuario"]) > 0:
            Main.ventanas_dic = "main"
            Main.vent_actual = copy(Main.vent_3)

            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.azul)
        else:
            boton = Main.botones[dic][key]
            boton.cambiar_fondo(Main.rojo)

    def ventana_estadisticas(dic, key):
        Main.ventanas_dic = "main"
        Main.vent_actual = copy(Main.vent_4)

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    def ventana_configuracion(dic, key):
        Main.ventanas_dic = "main"
        Main.vent_actual = copy(Main.vent_5)

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)

    def ventana_combate(dic, key):
        Main.ventanas_dic= "main"
        Main.vent_actual = copy(Main.vent_6)

        boton = Main.botones[dic][key]
        boton.cambiar_fondo(Main.azul)
    
    def ventana_salir(dic, key):
        pygame.quit()
        exit()
