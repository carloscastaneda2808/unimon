"""
Archivo para crear imagenes
"""

import pygame

from settings.settings import Main

class Imagen:

    def __init__(self, key, imagen_ruta, x, y, ancho, altura, dic):
        self.surf = pygame.image.load(imagen_ruta).convert()
        self.scale = pygame.transform.scale(self.surf, (ancho, altura))
        self.x = x
        self.y = y

        if dic not in Main.imagenes:
            Main.imagenes[dic] = {}
        Main.imagenes[dic][key] = self

    # Dibujar
    def dibujar(self, screen):
        screen.blit(self.scale, (self.x, self.y))