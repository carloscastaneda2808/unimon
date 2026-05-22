"""
Archivo para hacer las habilidades
"""

import pygame

from random import randint
from time import sleep

from clase.clase_main import Main
from clase.cadena import Cadena

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
        self.imagenes_rutas = imagenes_rutas
        self.frames = []

        for imagen_ruta in self.imagenes_rutas:    
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
    def cambiar_front(self):
        self.cambiar_medidas(400, 400)
        self.cambiar_imagen(0)
        self.cambiar_xy(Main.ancho * 9/12, Main.altura * 5/12)

    def cambiar_back(self):
        self.cambiar_medidas(600, 600)
        self.cambiar_imagen(0)
        self.cambiar_xy(Main.ancho * 3/12, Main.altura * 8/12)

    def cambiar_imagen(self, index):
        self.index = index
        self.imagen = self.frames[self.index]
        self.rect = self.imagen.get_rect(center = (self.x, self.y))

    def cambiar_xy(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.imagen.get_rect(center = (self.x, self.y))

    def cambiar_medidas(self, ancho, altura):
        self.frames.clear()

        for imagen_ruta in self.imagenes_rutas:    
            frame = pygame.image.load(imagen_ruta).convert_alpha()
            frame = pygame.transform.scale(frame, (ancho, altura))
            self.frames.append(frame)

    def dibujar(self, screen, jugador):
        if jugador == Cadena.usuario:
            self.cambiar_back()

        if jugador == Cadena.NPC:
            self.cambiar_front()

        screen.blit(self.imagen, self.rect)

