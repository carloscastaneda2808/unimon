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

# Funciones en extra
unimones_dic = unimon_enumerar(unimones, ancho, letras_unimones, negro, azul)

# Fondo
backround_surf = pygame.image.load("images/backround/inicio.jpg").convert()
backround_scale = pygame.transform.scale(backround_surf, (ancho, altura))

# Botones
botones = {"titulo": Boton(letras_titulo, "Unimon", negro, (ancho / 2, altura / 10), (400, 80), verde),
           "jugar": Boton(letras_botones, "Iniciar Partida", negro, (ancho / 2, 3 * altura / 10), (400, 80), azul),
           "estadisticas": Boton(letras_botones, "Estadisticas", negro, (ancho / 2, 5 * altura / 10),  (400, 80), azul),
           "configuracion": Boton(letras_botones, "Configuracion", negro, (ancho / 2, 7 * altura / 10), (400, 80), azul),
           "jugar2": Boton(letras_botones, "Iniciar Partida", negro, (ancho / 2, altura / 10), (400, 80), verde),
           "estadisticas2": Boton(letras_botones, "Estadisticas", negro, (ancho / 2, altura / 10),  (400, 80), verde),
           "configuracion2": Boton(letras_botones, "Configuracion", negro, (ancho / 2, altura / 10), (400, 80), verde),
           "salir": Boton(letras_botones, "Salir", negro, (ancho / 2, 9 * altura / 10), (400, 80), azul),
           }

# Menu
opcion = 1

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
                if opcion == 1:
                    if botones["jugar"].collision(pos_mouse):
                        opcion = 2
                        botones["jugar"].cambiar_fondo(azul)

                    elif botones["estadisticas"].collision(pos_mouse):
                        opcion = 3
                        botones["estadisticas"].cambiar_fondo(azul)

                    elif botones["configuracion"].collision(pos_mouse):
                        opcion = 4
                        botones["configuracion"].cambiar_fondo(azul)

                    elif botones["salir"].collision(pos_mouse):
                        pygame.quit()
                        exit()

                # Iniciar Partida
                elif opcion == 2:
                    for unimon_dic in unimones_dic.values():
                        if unimon_dic.collision(pos_mouse):
                            if unimon_dic.fondo == azul:
                                unimon_dic.cambiar_fondo(azul_oscuro)
                            else: 
                                unimon_dic.cambiar_fondo(azul)

                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        opcion = 1

                # Estadisticas
                elif opcion == 3:

                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        opcion = 1

                # Configuracion
                elif opcion == 4:
                    
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        opcion = 1

        # Cambia de color
        if event.type == pygame.MOUSEMOTION:
            # Menu principal
            if opcion == 1:
                if botones["jugar"].collision(pos_mouse):
                    botones["jugar"].cambiar_fondo(azul_oscuro)
                else: 
                    botones["jugar"].cambiar_fondo(azul)

                if botones["estadisticas"].collision(pos_mouse):
                    botones["estadisticas"].cambiar_fondo(azul_oscuro)
                else: 
                    botones["estadisticas"].cambiar_fondo(azul)

                if botones["configuracion"].collision(pos_mouse):
                    botones["configuracion"].cambiar_fondo(azul_oscuro)
                else: 
                    botones["configuracion"].cambiar_fondo(azul)

                if botones["salir"].collision(pos_mouse):
                    botones["salir"].cambiar_fondo(azul_oscuro)
                else: 
                    botones["salir"].cambiar_fondo(azul)

            # Iniciar Partida
            elif opcion == 2:
            
                if botones["salir"].collision(pos_mouse):
                    botones["salir"].cambiar_fondo(azul_oscuro)
                else: 
                    botones["salir"].cambiar_fondo(azul)

            # Estadisticas
            elif opcion == 3:
                
                
                if botones["salir"].collision(pos_mouse):
                    botones["salir"].cambiar_fondo(azul_oscuro)
                else: 
                    botones["salir"].cambiar_fondo(azul)

            # Configuracion
            elif opcion == 4:
                if botones["configuracion2"].collision(pos_mouse):
                    botones["configuracion2"].cambiar_fondo(azul_oscuro)
                else: 
                    botones["configuracion2"].cambiar_fondo(azul)
                
                if botones["salir"].collision(pos_mouse):
                    botones["salir"].cambiar_fondo(azul_oscuro)
                else: 
                    botones["salir"].cambiar_fondo(azul)

    screen.blit(backround_scale, (0, 0))

    if opcion == 1:
        botones["titulo"].dibujar(screen)

        botones["jugar"].dibujar(screen)

        botones["estadisticas"].dibujar(screen)

        botones["configuracion"].dibujar(screen)

        botones["salir"].dibujar(screen)    

    elif opcion == 2:
        botones["jugar2"].dibujar(screen)

        for unimon_dic in unimones_dic.values():
            unimon_dic.dibujar(screen)

        botones["salir"].dibujar(screen)

    elif opcion == 3:
        botones["estadisticas2"].dibujar(screen) 

        botones["salir"].dibujar(screen)    

    elif opcion == 4:
        botones["configuracion2"].dibujar(screen)  

        botones["salir"].dibujar(screen)  
    
    pygame.display.update()
    fps.tick(60)
