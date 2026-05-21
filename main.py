"""
Archivo para interfaz grafica de prube
"""

import pygame
from sys import exit
from copy import copy

from clase_main import Main

from visual.elemento_ui import ElementoUI
from visual.ventana import Ventana
from visual.boton import Boton
from visual.imagen import Imagen
from visual.texto import Texto

from pokedex.unimon import Unimon
from pokedex.habilidad import Habilidad

from datos.unimones import datos_unimones
from datos.habilidades import datos_habilidades
from datos.visual import datos_visual

# Crea la pantalla
screen = pygame.display.set_mode((Main.ancho, Main.altura))
pygame.display.set_caption("Unimon")

# Datos
datos_unimones()
datos_habilidades()
datos_visual()

# Crear Botones
Boton.crear_botones("main", Main.unimones["main"].keys(), Boton.seleccionar_1, Boton.deseleccionar_1)
Boton.botones_ventana(Main.unimones["main"].keys(), "main", Main.vent_2, "a")

while True:
    pos_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        # Cerrar el juego
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Click derecho
            if event.button == 1:

                Main.ventanas[Main.ventanas_dic][Main.vent_actual].collision_1(pos_mouse)

            # Click izquierdo
            if event.button == 3:

                Main.ventanas[Main.ventanas_dic][Main.vent_actual].collision_2(pos_mouse)

        # Efecto Hover
        if event.type == pygame.MOUSEMOTION:

            Main.ventanas[Main.ventanas_dic][Main.vent_actual].hover(pos_mouse)

    # Dibuja la pantalla
    screen.fill(Main.negro)

    Main.ventanas[Main.ventanas_dic][Main.vent_actual].dibujar(screen)

    pygame.display.update()
    Main.fps.tick(60)