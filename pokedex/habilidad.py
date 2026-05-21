"""
Archivo para hacer las habilidades
"""

import pygame

from clase.main import Main
from random import randint

class Habilidad:
    
    def __init__(self, key, tipo, 
                 poder, pp, acc, sts, estado, estado_acc,
                 imagenes_rutas, x, y, ancho, altura,
                 dic):

        self.tipo = tipo
        self.poder = poder
        self.pp = pp
        self.acc = acc
        self.sts = sts
        self.estado = estado
        self.estado_acc = estado_acc

        # Sprite
        self.frames = []

        for imagen_ruta in imagenes_rutas:    
            frame = pygame.image.load(imagen_ruta).convert_alpha()
            frame = pygame.transform.scale(frame, (ancho, altura))
            self.frames.append(frame)
        
        self.x = x
        self.y = y
        self.index = 0
        self.imagen = self.frames[self.index]
        self.rect = self.imagen.get_rect(center = (self.x, self.y))
        
        if dic not in Main.habilidades:
            Main.habilidades[dic] = {}
        Main.habilidades[dic][key] = self

    # Funciones
    def verificar_estado_acc(self):
        return self.acc >= randint(1, 100)

    # Funciones de Sprite
    def cambiar_imagen(self, index):
        self.index = index
        self.imagen = self.frames[self.index]
        self.rect = self.imagen.get_rect(center = (self.x, self.y))

    def dibujar(self, screen):
        screen.blit(self.imagen, self.rect)

