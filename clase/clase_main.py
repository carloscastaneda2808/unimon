"""
Archivo para guardar datos en la clase Main
"""

import pygame

from clase.cadena import Cadena

pygame.init()

class Main():
    # Funciones de los diccionarios
    def crear_diccionario(dic, dic_sub):
        if dic_sub not in dic:
            dic[dic_sub] = {}

    def eliminar_diccionario(dic, dic_sub):
        if dic_sub in dic:
            dic.pop(dic_sub)

    # Reinicio
    def reinicio():
        Main.vent_actual = Cadena.inicio
        Main.vent_anterior = Cadena.inicio
        Main.ventanas_dic_anterior = Cadena.main

        Main.unimones_dic = Cadena.main
        Main.unimones = {Cadena.main: {}}

        Main.habilidades_dic = Cadena.main
        Main.habilidades = {Cadena.main: {}}

        Main.botones_dic = Cadena.main
        Main.botones = {Cadena.main: {}}

        Main.imagenes_dic = Cadena.main
        Main.imagenes = {Cadena.main: {}}

        Main.textos_dic = Cadena.main
        Main.textos = {Cadena.main: {}}

        Main.ventanas_dic = Cadena.main
        Main.ventanas = {Cadena.main: {}}

        Main.unimon_usr = None
        Main.unimon_npc = None
        Main.movimiento_usr = None
        Main.movimiento_npc = None

        Main.combate = False
        Main.turno = 1
        Main.resultado = ""
        Main.timer = 0
        Main.timer_termina = 0

        Main.historial = []
        Main.historial_nuevo = ""

    # Pantalla
    info_pantalla = pygame.display.Info()
    ancho = info_pantalla.current_w
    altura = info_pantalla.current_h
    screen = pygame.display.set_mode((ancho, altura))

    # FPS
    fps = pygame.time.Clock()

    # Colores
    rojo = "Red"
    verde = "Green"
    azul = "Blue"
    azul_oscuro = "darkblue"
    cian = "cyan"
    negro = "Black"
    gris = "gray"
    amarillo = "yellow"

    # Letras
    fuente_1 = pygame.font.Font("letras/SHPinscher-Regular.otf", 100)
    fuente_2 = pygame.font.Font("letras/SHPinscher-Regular.otf", 50)
    fuente_3 = pygame.font.Font("letras/SHPinscher-Regular.otf", 35)

    # Diccionarios de diccionarios
    unimones_dic = Cadena.main
    unimones = {Cadena.main: {}}

    habilidades_dic = Cadena.main
    habilidades = {Cadena.main: {}}

    botones_dic = Cadena.main
    botones = {Cadena.main: {}}

    imagenes_dic = Cadena.main
    imagenes = {Cadena.main: {}}

    textos_dic = Cadena.main
    textos = {Cadena.main: {}}

    ventanas_dic = Cadena.main
    ventanas = {Cadena.main: {}}

    # Ventanas
    vent_actual = Cadena.inicio
    vent_anterior = Cadena.inicio
    ventanas_dic_anterior = Cadena.main

    # Unimones
    unimon_usr = None
    unimon_npc = None

    # Moviminetos
    movimiento_usr = None
    movimiento_npc = None

    # Combate
    combate = False
    turno = 1
    resultado = ""
    timer = 0
    timer_termina = 0

    # Historial
    historial = []
    historial_nuevo = ""
