"""
Archivo para interfaz grafica
"""

import pygame
from sys import exit
from copy import copy

from clase.clase_main import Main
from clase.cadena import Cadena

from visual.elemento_ui import ElementoUI
from visual.ventana import Ventana
from visual.boton import Boton
from visual.imagen import Imagen
from visual.texto import Texto

from pokedex.unimon import Unimon
from pokedex.habilidad import Habilidad

from partida.combate import Combate

from datos.unimones import datos_unimones
from datos.habilidades import datos_habilidades
from datos.visual import datos_visual

# Crea la pantalla
pygame.display.set_caption("Unimon")

# Reinicio
def reinicio():
    if Boton.reiniciar:
        Main.reinicio()
        datos_unimones()
        datos_visual()
        Boton.crear_botones(Cadena.main, Main.unimones[Cadena.main].keys(), Boton.elegir_unimon, Boton.descartar_unimon)
        Boton.botones_ventana(Main.unimones[Cadena.main].keys(), Cadena.main, Cadena.elegir_unimones, Cadena.a)

        Boton.reiniciar = False

def combate():
    if Main.combate:
        Combate.combate()
        Main.turno += 1
        Main.combate = False
        Main.animacion = True

# Datos
datos_unimones()
datos_habilidades()
datos_visual()

# Crear Botones
Boton.crear_botones(Cadena.main, Main.unimones[Cadena.main].keys(), Boton.elegir_unimon, Boton.descartar_unimon)
Boton.botones_ventana(Main.unimones[Cadena.main].keys(), Cadena.main, Cadena.elegir_unimones, Cadena.a)

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
                reinicio()
                combate()

            # Click izquierdo
            if event.button == 3:

                Main.ventanas[Main.ventanas_dic][Main.vent_actual].collision_2(pos_mouse)

        # Efecto Hover
        if event.type == pygame.MOUSEMOTION:

            Main.ventanas[Main.ventanas_dic][Main.vent_actual].hover(pos_mouse)

    # Dibuja la pantalla
    Main.screen.fill(Main.negro)
    Main.ventanas[Main.ventanas_dic][Main.vent_actual].dibujar(Main.screen)

    pygame.display.update()
    Main.fps.tick(60)