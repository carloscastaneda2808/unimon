"""
Archivo de interfaz grafica 3
"""

import pygame
from random import randint
from sys import exit
from copy import copy, deepcopy
from time import sleep

from funciones_UP.lectura import abrir_unimon
from funciones_graficas.boton import Boton
from pokedex.unimon import Unimon

# Funciones
def eliminar_titulo(nombre):
    titulos.pop(nombre)

def crear_titulo(nombre, texto = None):
    if not texto:
        texto = copy(nombre)

    titulos[f"{nombre}"] = Boton(letras_titulo, f"{texto}", negro, (ancho / 2, altura / 10), titulo_tamanio, verde)

def obj_botones(objetos, tipo, negro, azul):

    objetos_por_filas = 4
    espacio = ancho / (objetos_por_filas + 1)

    for i, obj in enumerate(objetos):

        columna = i % objetos_por_filas
        fila = i // objetos_por_filas

        x = espacio * (columna + 1)
        y = 230 + fila * 100

        botones[f"{obj.nombre}_{tipo}"] = Boton(letras_unimones, obj.nombre, negro, (x, y), (250, 60), azul, obj)

def eliminar_obj_botones(objetos, tipo):
    for obj in objetos:
        botones.pop(f"{obj.nombre}_{tipo}")

def crear_ventana(nombre, botones):
    ventanas[f"{nombre}"] = botones

def eliminar_ventana(nombre):
    ventanas.pop(nombre)

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
cian = "cyan"
negro = "Black"
gris = "gray"

# Letras
letras_titulo = pygame.font.Font("letras/SHPinscher-Regular.otf", 100)
letras_botones = pygame.font.Font("letras/SHPinscher-Regular.otf", 50)
letras_unimones = pygame.font.Font("letras/SHPinscher-Regular.otf", 35)

# Tamanio
titulo_tamanio = (700, 110)
boton_tamanio = (400, 80)

# Fondo
backround_surf = pygame.image.load("images/backround/inicio.jpg").convert()
backround_scale = pygame.transform.scale(backround_surf, (ancho, altura))

# Titulos
titulos = { "menu_principal": Boton(letras_titulo, "Menu Principal", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
            "elegir_unimones": Boton(letras_titulo, "Elegir Unimones", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
            "elegir_habilidades": Boton(letras_titulo, "Elegir Habilidades", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
            "estadisticas": Boton(letras_titulo, "Estadisticas", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
            "configuracion": Boton(letras_titulo, "Configuracion", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
            "combate": Boton(letras_titulo, "Combate", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
            # "atacar": Boton(letras_titulo, "Atacar", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
            "sacar": Boton(letras_titulo, "Sacar", negro, (ancho / 2, altura / 10), titulo_tamanio, verde)

            # se aniaden los titulos de cada unimon
            }

# Botones
botones = {
    # Menu principal
    "elegir_unimones": Boton(letras_botones, "Elegir Unimones", negro, (ancho / 2, 3 * altura / 10), boton_tamanio, azul),
    "estadisticas": Boton(letras_botones, "Estadisticas", negro, (ancho / 2, 5 * altura / 10), boton_tamanio, azul),
    "configuracion": Boton(letras_botones, "Configuracion", negro, (ancho / 2, 7 * altura / 10), boton_tamanio, azul),

    # Elegir unimones
    "elegir_habilidades": Boton(letras_botones, "Elegir Habilidades", negro, (3 * ancho / 4, 9 * altura / 10), boton_tamanio, azul),

    # Elegir habilidades
    "combate": Boton(letras_botones, "Combate", negro, (3 * ancho / 4, 9 * altura / 10), boton_tamanio, azul),

    # Combate
    "atacar": Boton(letras_botones, "Atacar", negro, (ancho / 2, 3 * altura / 10), boton_tamanio, azul),
    "sacar": Boton(letras_botones, "Sacar", negro, (ancho / 2, 5 * altura / 10),  boton_tamanio, azul),

    # Salir
    "salir": Boton(letras_botones, "Salir", negro, (ancho / 2, 9 * altura / 10), boton_tamanio, azul),

    # Atras
    "atras": Boton(letras_botones, "Atrás", negro, (ancho / 2, 9 * altura / 10), boton_tamanio, azul),
    "atras_izquierda": Boton(letras_botones, "Atrás", negro, (ancho / 4, 9 * altura / 10), boton_tamanio, azul),

    # Seguir
    "seguir_derecha": Boton(letras_botones, "Seguir", negro, (3 * ancho / 4, 9 * altura / 10), boton_tamanio, azul),

    # Se aniaden botones de cada unimon, que son sus habilidades
    }

# Botones de los unimones
obj_botones(unimones, "general", negro, azul)

# Menus
ventanas = { "menu_principal": ["elegir_unimones", "estadisticas", "configuracion", "salir"],
                    # se crea la ventana de elegir_unimones con crear_ventana()
                    
                    "elegir_habilidades": ["atras_izquierda", "seguir_derecha"],

                    "combate": ["atacar", "sacar", "atras"],
                    "estadisticas": ["atras"],
                    "configuracion": ["atras"],

                    "sacar": ["atras"],
                    }

# Ventanas de elegir_unimones
lista_unimones = [f"{unimon.nombre}_general" for unimon in unimones]
lista_unimones.append("atras_izquierda")
lista_unimones.append("elegir_habilidades")
crear_ventana("elegir_unimones", lista_unimones)

# Funciones de los unimones
cantidad_unimones = 6
cantidad_habilidades = 4
equipo_usr = []

# Opcion vent(ventana)
vent = "menu_principal"

# Ciclo principal
while True:
    pos_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Click izquierdo
        # Para cambiar de ventanas y seleccionar opcion
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                # Menu principal
                if vent == "menu_principal":
                    if botones["elegir_unimones"].collision(pos_mouse):
                        vent = "elegir_unimones"
                        botones["elegir_unimones"].cambiar_fondo(azul)

                    elif botones["estadisticas"].collision(pos_mouse):
                        vent = "estadisticas"
                        botones["estadisticas"].cambiar_fondo(azul)

                    elif botones["configuracion"].collision(pos_mouse):
                        vent = "configuracion"
                        botones["configuracion"].cambiar_fondo(azul)

                    elif botones["salir"].collision(pos_mouse):
                        pygame.quit()
                        exit()

                # Elegir Unimon
                elif vent == "elegir_unimones":
                    # FUNCION PARA IMPRIMIR UNIMONES
                    for unimon in unimones:
                        boton = botones[f"{unimon.nombre}_general"]
                        if boton.collision(pos_mouse):
                            if boton.fondo == azul_oscuro:
                                if len(equipo_usr) < cantidad_unimones:
                                    # Boton
                                    boton.cambiar_fondo(cian)

                                    # Clase
                                    equipo_usr.append(unimon)

                                    # Menu de equipo
                                    obj_botones(equipo_usr, "equipo_usr", negro, azul)
                                    lista_unimones = [f"{unimon.nombre}_equipo_usr" for unimon in equipo_usr]
                                    lista_unimones.append("atras_izquierda")
                                    lista_unimones.append("seguir_derecha")
                                    crear_ventana("elegir_habilidades", lista_unimones)

                                    # Menu de sacar
                                    lista_unimones = [f"{unimon.nombre}_equipo_usr" for unimon in equipo_usr]
                                    lista_unimones.append("atras")
                                    crear_ventana("sacar", lista_unimones)
                                    
                                    # Menu de unimon con habilidades posibles
                                    crear_titulo(unimon.nombre)
                                    obj_botones(unimon.hb_posibles, f"{unimon.nombre}_hb_posibles", negro, azul)
                                    lista_hb = [f"{hb.nombre}_{unimon.nombre}_hb_posibles" for hb in unimon.hb_posibles]
                                    lista_hb.append("atras")
                                    crear_ventana(f"{unimon.nombre}_hb_posibles", lista_hb)

                                else:
                                    boton.cambiar_fondo(rojo)

                    if botones["atras_izquierda"].collision(pos_mouse):
                        botones["atras_izquierda"].cambiar_fondo(azul)
                        vent = "menu_principal"

                    elif botones["elegir_habilidades"].collision(pos_mouse):
                        if equipo_usr:
                            botones["elegir_habilidades"].cambiar_fondo(azul)
                            vent = "elegir_habilidades"

                        else:
                            botones["elegir_habilidades"].cambiar_fondo(rojo)

                # Elegir Habilidades
                elif vent == "elegir_habilidades":

                    # FUNCION PARA MOSTRAR LOS UNIMONES ELEGIDOS
                    for unimon in equipo_usr:
                        boton = botones[f"{unimon.nombre}_equipo_usr"]
                        if boton.collision(pos_mouse):
                            boton.cambiar_fondo(azul)
                            vent = f"{unimon.nombre}_hb_posibles"

                    if botones["atras_izquierda"].collision(pos_mouse):
                        botones["atras_izquierda"].cambiar_fondo(azul)
                        vent = "elegir_unimones"

                    elif botones["seguir_derecha"].collision(pos_mouse):
                        pasar = True
                        for unimon in equipo_usr:
                            if not unimon.hb:
                                pasar = False
                                break

                        if pasar:
                            botones["seguir_derecha"].cambiar_fondo(azul)
                            vent = "sacar"
                        
                        else:
                            botones["seguir_derecha"].cambiar_fondo(rojo)

                # Combate
                elif vent == "combate":
                    if botones["atacar"].collision(pos_mouse):
                        botones["atacar"].cambiar_fondo(azul)
                        vent = f"{unimon_usr.nombre}_hb"

                    elif botones["sacar"].collision(pos_mouse):
                        botones["sacar"].cambiar_fondo(azul)
                        vent = "sacar"
                    
                    elif botones["atras"].collision(pos_mouse):
                        botones["atras"].cambiar_fondo(azul)
                        vent = "elegir_habilidades"
                
                # Sacar
                elif vent == "sacar":
                    for unimon in equipo_usr:
                        boton = botones[f"{unimon.nombre}_equipo_usr"]
                        if boton.collision(pos_mouse):
                            boton.cambiar_fondo(azul)
                            vent = "combate"
                            unimon_usr = unimon
            
                    if botones["atras"].collision(pos_mouse):
                        botones["atras"].cambiar_fondo(azul)
                        vent = "combate"

                # Estadisticas
                elif vent == "estadisticas":
                    if botones["atras"].collision(pos_mouse):
                        botones["atras"].cambiar_fondo(azul)
                        vent = "menu_principal"

                # Configuracion
                elif vent == "configuracion":  
                    if botones["atras"].collision(pos_mouse):
                        botones["atras"].cambiar_fondo(azul)
                        vent = "menu_principal"

                # Ventana de cada unimon
                for unimon in equipo_usr:
                    if vent == f"{unimon.nombre}_hb_posibles":
                        for hb in unimon.hb_posibles:
                            boton = botones[f"{hb.nombre}_{unimon.nombre}_hb_posibles"]

                            if boton.collision(pos_mouse):
                                if boton.fondo == azul_oscuro:
                                    if len(unimon.hb) < cantidad_habilidades:
                                        # Boton
                                        boton.cambiar_fondo(cian)

                                        # Clase
                                        unimon.hb.append(hb)

                                        # Menu de unimon con habilidades
                                        obj_botones(unimon.hb, f"{unimon.nombre}_hb", negro, azul)
                                        lista_hb = [f"{hb.nombre}_{unimon.nombre}_hb" for hb in unimon.hb]
                                        lista_hb.append("atras")
                                        crear_ventana(f"{unimon.nombre}_hb", lista_hb)

                                    else:
                                        boton.cambiar_fondo(rojo)

                        if botones["atras"].collision(pos_mouse):
                            botones["atras"].cambiar_fondo(azul)
                            vent = "elegir_habilidades"

                for unimon in equipo_usr:
                    if vent == f"{unimon.nombre}_hb":
                        for hb in unimon.hb:
                            boton = botones[f"{hb.nombre}_{unimon.nombre}_hb"]

                            if boton.collision(pos_mouse):
                                boton.cambiar_fondo(azul)
                                vent = "combate"
                                atacaque_usr = hb

                        if botones["atras"].collision(pos_mouse):
                            botones["atras"].cambiar_fondo(azul)
                            vent = "combate"

            # Click derecho
            # Para quitar slecciones
            if event.button == 3:
                # Elegir Unimon
                if vent == "elegir_unimones":
                    # FUNCION PARA IMPRIMIR UNIMONES
                    for unimon in unimones:
                        boton = botones[f"{unimon.nombre}_general"]
                        if boton.collision(pos_mouse):
                            if boton.fondo == cian:
                                # Boton
                                boton.cambiar_fondo(azul_oscuro)

                                # Clase
                                equipo_usr.remove(unimon)

                                # Actualizar menu de equipo
                                obj_botones(equipo_usr, "equipo_usr", negro, azul)
                                lista_unimones = [f"{unimon.nombre}_equipo_usr" for unimon in equipo_usr]
                                lista_unimones.append("atras_izquierda")
                                lista_unimones.append("seguir_derecha")
                                crear_ventana("elegir_habilidades", lista_unimones)

                                # Actualizar menu de sacar
                                lista_unimones = [f"{unimon.nombre}_equipo_usr" for unimon in equipo_usr]
                                lista_unimones.append("atras")
                                crear_ventana("sacar", lista_unimones)

                                # Eliminar menu de unimon con habilidades posibles
                                eliminar_titulo(unimon.nombre)
                                eliminar_obj_botones(unimon.hb_posibles, f"{unimon.nombre}_hb_posibles")
                                eliminar_ventana(f"{unimon.nombre}_hb_posibles")
                
                for unimon in equipo_usr:
                    if vent == f"{unimon.nombre}_hb_posibles":
                        for hb in unimon.hb_posibles:
                            boton = botones[f"{hb.nombre}_{unimon.nombre}_hb_posibles"]

                            if boton.collision(pos_mouse):                            
                                if boton.fondo == cian:
                                    # Boton
                                    boton.cambiar_fondo(azul_oscuro)

                                    # Clase
                                    unimon.hb.remove(hb)

                                    # Actualizar menu de unimon con habilidades
                                    obj_botones(unimon.hb, f"{unimon.nombre}_hb", negro, azul)
                                    lista_hb = [f"{hb.nombre}_{unimon.nombre}_hb" for hb in unimon.hb]
                                    lista_hb.append("atras")
                                    crear_ventana(f"{unimon.nombre}_hb", lista_hb)

        # Cambiar de color
        if event.type == pygame.MOUSEMOTION:
                    
            for boton_nombre in ventanas.get(vent, []):
                boton = botones[boton_nombre]
                if boton.collision(pos_mouse) and boton.fondo != cian:
                    boton.cambiar_fondo(azul_oscuro)

                elif boton.fondo != cian:
                    boton.cambiar_fondo(azul)

    # Imprime la pantalla
    screen.blit(backround_scale, (0, 0))

    if vent == "menu_principal":
        titulos["menu_principal"].dibujar(screen)  

    elif vent == "elegir_unimones":
        titulos["elegir_unimones"].dibujar(screen)

    elif vent == "elegir_habilidades":
        titulos["elegir_habilidades"].dibujar(screen)

    elif vent == "combate":
        titulos["combate"].dibujar(screen)

    elif vent == "sacar":
        titulos["sacar"].dibujar(screen)

    elif vent == "estadisticas":
        titulos["estadisticas"].dibujar(screen)  

    elif vent == "configuracion":
        titulos["configuracion"].dibujar(screen)

    # Dibuja los titulos de los unimoes
    for unimon in equipo_usr:
        if vent == f"{unimon.nombre}_hb_posibles":
            titulo = titulos[f"{unimon.nombre}"]
            titulo.dibujar(screen)

    for unimon in equipo_usr:
        if vent == f"{unimon.nombre}_hb":
            titulo = titulos[f"{unimon.nombre}"]
            titulo.dibujar(screen)

    # Dibuja los botones
    for boton_nombre in ventanas.get(vent, []):
        botones[boton_nombre].dibujar(screen)
    
    pygame.display.update()
    fps.tick(60)