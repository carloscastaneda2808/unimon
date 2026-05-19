"""
Archivo para interfaz grafica de prube
"""

import pygame
from sys import exit
from copy import copy

from visual.boton import Boton
from visual.texto import Texto
from visual.ventana import Ventana
from visual.imagen import Imagen

from datos.unimones import datos_unimones
from datos.habilidades import datos_habilidades

pygame.init()

# Pantalla
info_pantalla = pygame.display.Info()
ancho = info_pantalla.current_w
altura = info_pantalla.current_h
screen = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption("Unimon")

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

# Letras
fuente_1 = pygame.font.Font("letras/SHPinscher-Regular.otf", 100)
fuente_2 = pygame.font.Font("letras/SHPinscher-Regular.otf", 50)
fuente_3 = pygame.font.Font("letras/SHPinscher-Regular.otf", 35)

# Imagenes
Imagen("inicio", "images/backround/inicio.jpg", ancho, altura, 0, 0)

# Textos
Texto("inicio", fuente_1, "Unimon", negro, verde, None, ancho * 1/2, altura * 1/10, 700, 110)
Texto("elegir_unimones", fuente_1, "Elegir Unimon", negro, verde, None, ancho / 2, altura / 10, 700, 110)
Texto("elegir_habilidades", fuente_1, "Elegir Habilidades", negro, verde, None, ancho / 2, altura / 10, 700, 110)
Texto("estadisticas", fuente_1, "Estadisticas", negro, verde, None, ancho / 2, altura / 10, 700, 110)
Texto("configuracion", fuente_1, "Configuracion", negro, verde, None, ancho / 2, altura / 10, 700, 110)
Texto("combate", fuente_1, "Combate", negro, verde, None, ancho / 2, altura / 10, 700, 110)
Texto("atacar", fuente_1, "Atacar", negro, verde, None, ancho / 2, altura / 10, 700, 110)
Texto("sacar", fuente_1, "Sacar", negro, verde, None, ancho / 2, altura / 10, 700, 110)

# Botones
# Inicio
Boton("jugar", fuente_2, "Jugar", negro, azul, None, ancho * 1/2, altura * 3/10, 400, 80, Boton.ventana_elegir_unimones)
Boton("estadisticas", fuente_2, "Estadisticas", negro, azul, None, ancho * 1/2, altura * 5/10, 400, 80, Boton.ventana_estadisticas)
Boton("configuracion", fuente_2, "Configuracion", negro, azul, None, ancho * 1/2, altura * 7/10, 400, 80, Boton.ventana_configuracion)
Boton("salir", fuente_2, "Salir", negro, azul, None, ancho * 1/2, altura * 9/10, 400, 80, Boton.ventana_salir)

# Elegir Unimones
Boton("atras_1", fuente_2, "Atrás", negro, azul, None, ancho * 1/4, altura * 9/10, 400, 80, Boton.ventana_inicio)
Boton("seguir_1", fuente_2, "Seguir", negro, azul, None, ancho * 3/ 4, altura * 9/10, 400, 80, Boton.ventana_elegir_habilidades)

# Elegir Habilidades
Boton("atras_2", fuente_2, "Atrás", negro, azul, None, ancho * 1/4, altura * 9/10, 400, 80, Boton.ventana_elegir_unimones)
Boton("seguir_2", fuente_2, "Seguir", negro, azul, None, ancho * 3/4, altura * 9/10, 400, 80, Boton.ventana_combate)

# Estadisticas y Configuracion
Boton("atras_3", fuente_2, "Atrás", negro, azul, None, ancho * 1/2, altura * 9/10, 400, 80, Boton.ventana_inicio)

# Combate
Boton("atacar", fuente_2, "Atacar", negro, azul, None, ancho * 1/6, altura * 9/10, 400, 80, Boton.ventana_atacar)
Boton("sacar", fuente_2, "Sacar", negro, azul, None, ancho * 3/6, altura * 9/10, 400, 80, Boton.ventana_sacar)
Boton("huir", fuente_2, "Huir", negro, azul, None, ancho * 5/6, altura * 9/10, 400, 80, Boton.ventana_elegir_habilidades)

# Atacar y Sacar
Boton("atras_4", fuente_2, "Atrás", negro, azul, None, ancho * 1/2, altura * 9/10, 400, 80, Boton.ventana_combate)


# Ventanas
Ventana("inicio", [Imagen.imagenes["inicio"]], [Texto.textos["inicio"]], [Boton.botones["jugar"], Boton.botones["estadisticas"], Boton.botones["configuracion"], Boton.botones["salir"]])

Ventana("elegir_unimones", [Imagen.imagenes["inicio"]], [Texto.textos["elegir_unimones"]], [Boton.botones["atras_1"], Boton.botones["seguir_1"]])
Ventana("elegir_habilidades", [Imagen.imagenes["inicio"]], [Texto.textos["elegir_habilidades"]], [Boton.botones["atras_2"], Boton.botones["seguir_2"]])

Ventana("estadisticas", [Imagen.imagenes["inicio"]], [Texto.textos["estadisticas"]], [Boton.botones["atras_3"]])
Ventana("configuracion", [Imagen.imagenes["inicio"]], [Texto.textos["configuracion"]], [Boton.botones["atras_3"]])

Ventana("combate", [Imagen.imagenes["inicio"]], [Texto.textos["combate"]], [Boton.botones["atacar"], Boton.botones["sacar"], Boton.botones["huir"]])

Ventana("atacar", [Imagen.imagenes["inicio"]], [Texto.textos["atacar"]], [Boton.botones["atras_4"]])

Ventana("sacar", [Imagen.imagenes["inicio"]], [Texto.textos["sacar"]], [Boton.botones["atras_4"]])

# Datos
datos_unimones()
datos_habilidades()

# Empieza en inicio
ventana = "inicio"

while True:
    pos_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        # Cerrar el juego
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                funcion = Ventana.ventanas[ventana].collision(pos_mouse, azul)
                if funcion:
                    ventana = funcion

        # Efecto Hover
        if event.type == pygame.MOUSEMOTION:

            Ventana.ventanas[ventana].hover(pos_mouse, azul, azul_oscuro)

    screen.fill(negro)
    Ventana.ventanas[ventana].dibujar(screen)
    pygame.display.update()
    fps.tick(60)