"""
Archivo para crear botones
"""

import pygame

from visual.elemento_ui import ElementoUI

class Boton(ElementoUI):
    botones = {}

    def __init__(self, nombre, fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto, funcion):
        # super() invoca a elementos UI
        super().__init__(fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto)
        self.funcion = funcion
        
        # Se guarda en un diccionario
        Boton.botones[nombre] = self

    def collision(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)
    
    def cambiar_fondo(self, nuevo_fondo):
        if self.imagen:
            self.rect_imagen = nuevo_fondo
        else:
            self.fondo_color = nuevo_fondo

    def ventana_inicio():
        return "inicio"

    def ventana_elegir_unimones():
        return "elegir_unimones"

    def ventana_elegir_habilidades():
        return "elegir_habilidades"

    def ventana_estadisticas():
        return "estadisticas"

    def ventana_configuracion():
        return "configuracion"

    def ventana_combate():
        return "combate"

    def ventana_atacar():
        return "atacar"

    def ventana_sacar():
        return "sacar"
    
    def ventana_salir():
        pygame.quit()
        exit()

    def objetos_botones(objetos, ancho):
        
        objetos_por_filas = 4
        espacio = ancho / (objetos_por_filas + 1)

        for i, obj in enumerate(objetos):

            columna = i % objetos_por_filas
            fila = i // objetos_por_filas

            x = espacio * (columna + 1)
            y = 230 + fila * 100

        Boton(f"{obj.nombre}", )