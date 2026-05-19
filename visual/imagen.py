"""
Archivo para crear imagenes
"""

import pygame

class Imagen:
    imagenes = {}

    def __init__(self, nombre, imagen_ruta, ancho, altura, x, y):
        self.surf = pygame.image.load(imagen_ruta).convert()
        self.scale = pygame.transform.scale(self.surf, (ancho, altura))
        self.x = x
        self.y = y

        Imagen.imagenes[nombre] = self

    def dibujar(self, screen):
        screen.blit(self.scale, (self.x, self.y))