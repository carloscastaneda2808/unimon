"""
Archivo para crear los sprite de los unimones
"""

import pygame

class Sprite():
    sprites = {}

    def __init__(self, nombre, imagenes_rutas, x, y, ancho, altura):
        self.frames = []

        for imagen_ruta in imagenes_rutas:    
            frame = pygame.image.load(imagen_ruta).convert_alpha()
            frame = pygame.transform.scale(frame, (ancho, altura))
            self.frames.append(frame)
        
        self.index = 0
        self.imagen = self.frames[self.index]
        self.rect = self.imagen.get_rect(center = (x, y))
        
        Sprite.sprites[nombre] = self

    def cambiar_imagen(self, index):
        self.index = index
        self.imagen = self.frames[self.index]

    def dibujar(self, screen):
        screen.blit(self.imagen, self.rect)