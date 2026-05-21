"""
Archivo para guardar datos en la clase Main
"""

import pygame

pygame.init()

class Main():
    # Pantalla
    info_pantalla = pygame.display.Info()
    ancho = info_pantalla.current_w
    altura = info_pantalla.current_h

    # FPS
    fps = pygame.time.Clock()

    # Colores
    rojo = "Red"
    verde = "Green"
    azul = "Blue"
    azul_oscuro = "darkblue"
    cian = "cyan"
    negro = "Black"

    # Letras
    fuente_1 = pygame.font.Font("letras/SHPinscher-Regular.otf", 100)
    fuente_2 = pygame.font.Font("letras/SHPinscher-Regular.otf", 50)
    fuente_3 = pygame.font.Font("letras/SHPinscher-Regular.otf", 35)

    # Diccionarios de diccionarios
    unimones_dic = "main"
    unimones = {"main": {}}

    habilidades_dic = "main"
    habilidades = {"main": {}}

    botones_dic = "main"
    botones = {"main": {}}

    imagenes_dic = "main"
    imagenes = {"main": {}}

    textos_dic = "main"
    textos = {"main": {}}

    ventanas_dic = "main"
    ventanas = {"main": {}}

    # Crear diccionario
    def crear_diccionario(dic, dic_sub):
        if dic_sub not in dic:
            dic[dic_sub] = {}

    # Ventanas
    vent_actual = "inicio"
    vent_1 = "inicio"
    vent_2 = "elegir_unimones"
    vent_3 = "elegir_habilidades"
    vent_4 = "estadisticas"
    vent_5 = "configuracion"
    vent_6 = "combate"
    vent_7 = "atacar"
    vent_8 = "sacar"

    # Unimon
    unimon_usr = None
    unimon_npc = None

    # Movimiento
    movimiento_usr = None
    movimiento_npc = None