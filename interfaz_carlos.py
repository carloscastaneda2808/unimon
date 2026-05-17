"""
Archivo de interfaz grafica 2
"""

import pygame
from random import randint
from sys import exit
from copy import copy, deepcopy

from funciones_graficas.boton import Boton
from funciones_graficas.extra import unimon_enumerar
from funciones_UP.lectura import abrir_unimon
from pokedex.unimon import Unimon

unimones = abrir_unimon()

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
negro = "Black"

# Letras
letras_titulo = pygame.font.Font("letras/SHPinscher-Regular.otf", 100)
letras_botones = pygame.font.Font("letras/SHPinscher-Regular.otf", 50)
letras_unimones = pygame.font.Font("letras/SHPinscher-Regular.otf", 50)

# Tamanio
titulo_tamanio = (700, 110)
boton_tamanio = (400, 80)

# Funciones en extra
unimones_dic = unimon_enumerar(unimones, ancho, letras_unimones, negro, azul)

# Fondo
backround_surf = pygame.image.load("images/backround/inicio.jpg").convert()
backround_scale = pygame.transform.scale(backround_surf, (ancho, altura))

# Botones
botones = {"titulo": Boton(letras_titulo, "Unimon", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
           
           "jugar": Boton(letras_botones, "Iniciar Partida", negro, (ancho / 2, 3 * altura / 10), boton_tamanio, azul),
           "estadisticas": Boton(letras_botones, "Estadisticas", negro, (ancho / 2, 5 * altura / 10),  boton_tamanio, azul),
           "configuracion": Boton(letras_botones, "Configuracion", negro, (ancho / 2, 7 * altura / 10), boton_tamanio, azul),
           "salir": Boton(letras_botones, "Salir", negro, (ancho / 2, 9 * altura / 10), boton_tamanio, azul),

           "elegir_unimon": Boton(letras_titulo, "Elegir Unimon", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
           "elegir_habilidades": Boton(letras_titulo, "Elegir Habilidades", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
           "combate": Boton(letras_titulo, "Combate", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),

           "salir2": Boton(letras_botones, "Salir", negro, (ancho / 4, 9 * altura / 10), boton_tamanio, azul),
           "seguir": Boton(letras_botones, "Seguir", negro, (3 * ancho / 4, 9 * altura / 10), boton_tamanio, azul),

           "estadisticas2": Boton(letras_titulo, "Estadisticas", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),

           "configuracion2": Boton(letras_titulo, "Configuracion", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),

           "mochila": Boton(letras_botones, "Mochila", negro, (ancho / 2, 3 * altura / 10), boton_tamanio, azul),
           "cambiar": Boton(letras_botones, "Cambiar", negro, (ancho / 2, 5 * altura / 10),  boton_tamanio, azul),
           "huir": Boton(letras_botones, "Huir", negro, (ancho / 2, 7 * altura / 10), boton_tamanio, azul),

           "mochila2": Boton(letras_titulo, "Mochila", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
           "cambiar2": Boton(letras_titulo, "Cambiar", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
           "huir2": Boton(letras_titulo, "Huir", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
           }

# Menus
botones_estado = {"menu_principal": ["jugar", "estadisticas", "configuracion", "salir"],
                  
                  "elegir_unimon": ["salir2", "seguir"],
                  "elegir_habilidades": ["salir2", "seguir"],
                  "combate": ["mochila", "cambiar", "huir", "salir"],

                  "estadisticas": ["salir"],
                  "configuracion": ["salir"],

                  "mochila": ["salir"],
                  "cambiar": ["salir"],
                  "huir": ["salir"],}

# Opcines
ventana = "menu_principal"

# Ciclo principal
while True:
    pos_mouse = pygame.mouse.get_pos() 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Cambiar menu
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                # Menu principal
                if ventana == "menu_principal":
                    if botones["jugar"].collision(pos_mouse):
                        ventana = "elegir_unimon"
                        botones["jugar"].cambiar_fondo(azul)

                    elif botones["estadisticas"].collision(pos_mouse):
                        ventana = "estadisticas"
                        botones["estadisticas"].cambiar_fondo(azul)

                    elif botones["configuracion"].collision(pos_mouse):
                        ventana = "configuracion"
                        botones["configuracion"].cambiar_fondo(azul)

                    elif botones["salir"].collision(pos_mouse):
                        pygame.quit()
                        exit()

                # Iniciar Partida
                # Elegir Unimon
                elif ventana == "elegir_unimon":
                    for unimon_dic in unimones_dic.values():
                        if unimon_dic.collision(pos_mouse):
                            if unimon_dic.fondo == azul:
                                unimon_dic.cambiar_fondo(azul_oscuro)
                            else: 
                                unimon_dic.cambiar_fondo(azul)

                    if botones["salir2"].collision(pos_mouse):
                        botones["salir2"].cambiar_fondo(azul)
                        ventana = "menu_principal"

                    elif botones["seguir"].collision(pos_mouse):
                        botones["seguir"].cambiar_fondo(azul)
                        ventana = "elegir_habilidades"

                # Elegir Habilidades
                elif ventana == "elegir_habilidades":
                    if botones["salir2"].collision(pos_mouse):
                        botones["salir2"].cambiar_fondo(azul)
                        ventana = "elegir_unimon"

                    elif botones["seguir"].collision(pos_mouse):
                        botones["seguir"].cambiar_fondo(azul)
                        ventana = "combate"

                # Combate
                elif ventana == "combate":
                    if botones["mochila"].collision(pos_mouse):
                        botones["mochila"].cambiar_fondo(azul)
                        ventana = "mochila"

                    elif botones["cambiar"].collision(pos_mouse):
                        botones["cambiar"].cambiar_fondo(azul)
                        ventana = "cambiar"
                    
                    elif botones["huir"].collision(pos_mouse):
                        botones["huir"].cambiar_fondo(azul)
                        ventana = "huir"

                    elif botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        ventana = "elegir_habilidades"
                
                # mochila, cambiar y huir
                elif ventana == "mochila":
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        ventana = "combate"

                elif ventana == "cambiar":
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        ventana = "combate"
                
                elif ventana == "huir":
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        ventana = "combate"

                # Estadisticas
                elif ventana == "estadisticas":
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        ventana = "menu_principal"

                # Configuracion
                elif ventana == "configuracion":  
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        ventana = "menu_principal"

        # Cambia de color
        if event.type == pygame.MOUSEMOTION:

            for boton_nombre in botones_estado.get(ventana, []):
                boton = botones[boton_nombre]
                if boton.collision(pos_mouse):
                    boton.cambiar_fondo(azul_oscuro)
                else:
                    boton.cambiar_fondo(azul)

    screen.blit(backround_scale, (0, 0))

    if ventana == "menu_principal":
        botones["titulo"].dibujar(screen)  

    elif ventana == "elegir_unimon":
        botones["elegir_unimon"].dibujar(screen)

        for unimon_dic in unimones_dic.values():
            unimon_dic.dibujar(screen)

    elif ventana == "elegir_habilidades":
        botones["elegir_habilidades"].dibujar(screen)

    elif ventana == "combate":
        botones["combate"].dibujar(screen)

    elif ventana == "mochila":
        botones["mochila2"].dibujar(screen)

    elif ventana == "cambiar":
        botones["cambiar2"].dibujar(screen)

    elif ventana == "huir":
        botones["huir2"].dibujar(screen)

    elif ventana == "estadisticas":
        botones["estadisticas2"].dibujar(screen)  

    elif ventana == "configuracion":
        botones["configuracion2"].dibujar(screen)

    for boton_nombre in botones_estado.get(ventana, []):
        botones[boton_nombre].dibujar(screen)
    
    pygame.display.update()
    fps.tick(60)
