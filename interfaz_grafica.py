"""
Archivo de interfaz grafica 3
"""

import pygame
from random import randint
from sys import exit
from copy import copy, deepcopy

from funciones_UP.lectura import abrir_unimon
from funciones_graficas.boton import Boton
from pokedex.unimon import Unimon

# Funciones
def eliminar_titulo(nombre):
    titulos.pop(nombre)

def crear_titulo(nombre):
    titulos[f"{nombre}"] = Boton(letras_titulo, f"{nombre}", negro, (ancho / 2, altura / 10), titulo_tamanio, verde)

def obj_botones(objetos, tipo, negro, azul):

    objetos_por_filas = 5
    espacio = ancho / (objetos_por_filas + 1)

    for i, obj in enumerate(objetos):

        columna = i % objetos_por_filas
        fila = i // objetos_por_filas

        x = espacio * (columna + 1)
        y = 300 + fila * 100

        botones[f"{obj.nombre}_{tipo}"] = Boton(letras_unimones, obj.nombre, negro, (x, y), (180, 60), azul, obj)

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
letras_unimones = pygame.font.Font("letras/SHPinscher-Regular.otf", 50)

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
            "atacar": Boton(letras_titulo, "Atacar", negro, (ancho / 2, altura / 10), titulo_tamanio, verde),
            "cambiar": Boton(letras_titulo, "Cambiar", negro, (ancho / 2, altura / 10), titulo_tamanio, verde)

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
    "cambiar": Boton(letras_botones, "Cambiar", negro, (ancho / 2, 5 * altura / 10),  boton_tamanio, azul),

    # Salir
    "salir": Boton(letras_botones, "Salir", negro, (ancho / 2, 9 * altura / 10), boton_tamanio, azul),
    "salir_izquierda": Boton(letras_botones, "Atrás", negro, (ancho / 4, 9 * altura / 10), boton_tamanio, azul),

    # Se aniaden botones de cada unimon, que son sus habilidades
    }

# Botones de los unimones
obj_botones(unimones, "general", negro, azul)

# Menus
ventanas = { "menu_principal": ["elegir_unimones", "estadisticas", "configuracion", "salir"],
                    # se crea la ventana de elegir_unimones con crear_ventana()
                    # se crea la ventana de elegir_habilidades con crear_ventana() mas tarde
                    "combate": ["atacar", "cambiar", "salir"],
                    "estadisticas": ["salir"],
                    "configuracion": ["salir"],
                    "atacar": ["salir"],
                    "cambiar": ["salir"],
                    }

# Ventanas de elegir_unimones
lista_unimones = [f"{unimon.nombre}_general" for unimon in unimones]
lista_unimones.append("salir_izquierda")
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

        # Cambiar ventana
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
                                    lista_unimones.append("salir_izquierda")
                                    lista_unimones.append("combate")
                                    crear_ventana("elegir_habilidades", lista_unimones)

                                    # Menu de unimon con habilidades
                                    crear_titulo(unimon.nombre)
                                    obj_botones(unimon.hb_posibles, f"{unimon.nombre}_hb_posibles", negro, azul)
                                    lista_hb = [f"{hb}_{unimon.nombre}_hb_posibles" for hb in unimon.lista_hb()]
                                    lista_hb.append("salir")
                                    crear_ventana(unimon.nombre, lista_hb)

                                else:
                                    boton.cambiar_fondo(rojo)
                        
                            elif boton.fondo == cian:
                                # Boton
                                boton.cambiar_fondo(azul_oscuro)

                                # Clase
                                equipo_usr.remove(unimon)

                                # Menu de equipo
                                obj_botones(equipo_usr, "equipo_usr", negro, azul)
                                lista_unimones = [f"{unimon.nombre}_equipo_usr" for unimon in equipo_usr]
                                lista_unimones.append("salir_izquierda")
                                lista_unimones.append("combate")
                                crear_ventana("elegir_habilidades", lista_unimones)

                                # Eliminar menu de unimon con habilidades
                                eliminar_titulo(unimon.nombre)
                                eliminar_obj_botones(unimon.hb_posibles, f"{unimon.nombre}_hb_posibles")
                                eliminar_ventana(unimon.nombre)

                    if botones["salir_izquierda"].collision(pos_mouse):
                        botones["salir_izquierda"].cambiar_fondo(azul)
                        vent = "menu_principal"

                    elif botones["elegir_habilidades"].collision(pos_mouse):
                        botones["elegir_habilidades"].cambiar_fondo(azul)
                        vent = "elegir_habilidades"

                # Elegir Habilidades
                elif vent == "elegir_habilidades":

                    # FUNCION PARA MOSTRAR LOS UNIMONES ELEGIDOS
                    for unimon in equipo_usr:
                        boton = botones[f"{unimon.nombre}_equipo_usr"]
                        if boton.collision(pos_mouse):
                            boton.cambiar_fondo(azul)
                            vent = f"{unimon.nombre}"

                    if botones["salir_izquierda"].collision(pos_mouse):
                        botones["salir_izquierda"].cambiar_fondo(azul)
                        vent = "elegir_unimones"

                    elif botones["combate"].collision(pos_mouse):
                        botones["combate"].cambiar_fondo(azul)
                        vent = "combate"

                # Combate
                elif vent == "combate":
                    if botones["atacar"].collision(pos_mouse):
                        botones["atacar"].cambiar_fondo(azul)
                        vent = "atacar"

                    elif botones["cambiar"].collision(pos_mouse):
                        botones["cambiar"].cambiar_fondo(azul)
                        vent = "cambiar"
                    
                    elif botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        vent = "elegir_habilidades"

                # Atacar y cambiar
                elif vent == "atacar":
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        vent = "combate"

                elif vent == "cambiar":
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        vent = "combate"

                # Estadisticas
                elif vent == "estadisticas":
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        vent = "menu_principal"

                # Configuracion
                elif vent == "configuracion":  
                    if botones["salir"].collision(pos_mouse):
                        botones["salir"].cambiar_fondo(azul)
                        vent = "menu_principal"

                # Venta de cada unimon
                for unimon in equipo_usr:
                    if vent == f"{unimon.nombre}":
                        for hb in unimon.hb_posibles:
                            boton = botones[f"{hb.nombre}_{unimon.nombre}_hb_posibles"]

                            if boton.collision(pos_mouse):
                                if boton.fondo == azul_oscuro:
                                    if len(unimon.hb) < cantidad_habilidades:
                                        # Boton
                                        boton.cambiar_fondo(cian)

                                        # Clase
                                        unimon.hb.append(hb)

                                    else:
                                        boton.cambiar_fondo(rojo)
                            
                                elif boton.fondo == cian:
                                    # Boton
                                    boton.cambiar_fondo(azul_oscuro)

                                    # Clase
                                    unimon.hb.remove(hb)

                        if botones["salir"].collision(pos_mouse):
                            botones["salir"].cambiar_fondo(azul)
                            vent = "elegir_habilidades"

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

    elif vent == "atacar":
        titulos["atacar"].dibujar(screen)

    elif vent == "cambiar":
        titulos["cambiar"].dibujar(screen)

    elif vent == "estadisticas":
        titulos["estadisticas"].dibujar(screen)  

    elif vent == "configuracion":
        titulos["configuracion"].dibujar(screen)

    # Dibuja los titulos de los unimoes
    for unimon in equipo_usr:
        if vent == f"{unimon.nombre}":
            titulo = titulos[f"{unimon.nombre}"]
            titulo.dibujar(screen)

    # Dibuja los botones
    for boton_nombre in ventanas.get(vent, []):
        botones[boton_nombre].dibujar(screen)
    
    pygame.display.update()
    fps.tick(60)