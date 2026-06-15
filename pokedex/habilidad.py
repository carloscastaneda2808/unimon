"""
Archivo para hacer las habilidades
"""

import pygame

from random import randint
from copy import copy

from settings.settings import Main

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

        # Timer
        self.usando_timer = False
        self.empieza = 0
        self.termina = 0

        for imagen_ruta in self.imagenes_rutas:    
            frame = pygame.image.load(imagen_ruta).convert_alpha()
            frame = pygame.transform.scale(frame, (ancho, altura))
            self.frames.append(frame)
        
        self.x = x
        self.y = y
        self.index = 0
        self.imagen = self.frames[self.index]
        self.rect = self.imagen.get_rect(center = (self.x, self.y))
        
        # Guardar en la clase
        if dic not in Main.habilidades:
            Main.habilidades[dic] = {}
        Main.habilidades[dic][key] = self
    



    # Funciones para copiar o eliminar habilidades
    def copiar_habilidad(copiar, copiado, habilidad):
        Main.habilidades[copiar][habilidad] = copy(Main.habilidades[copiado][habilidad])

    def eliminar_habilidad(dic, habilidad):
        Main.habilidades[dic].pop(habilidad)




    # Funciones para verificar
    def verificar_estado_acc(self):
        return self.acc >= randint(1, 100)




    # Funciones para agregar o quitar habilidades de una ventana
    def habilidad_ventana(habilidad_dic, habilidad, ventanas_dic, ventana, dic_elementos):
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][8] = habilidad_dic
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][9].add(habilidad)

    def eliminar_habilidad_ventana(habilidad, ventanas_dic, ventana, dic_elementos):
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][8] = None
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][9].remove(habilidad)

    def limpiar_habilidad_ventana(ventanas_dic, ventana, dic_elementos):
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][8] = None
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][9].clear




    # Funciones de Sprite
    def cambiar_front(self):
        self.cambiar_medidas(300, 300)
        self.cambiar_imagen(0)
        self.cambiar_xy(Main.ancho * 18/24, Main.altura * 7/24)

    def cambiar_back(self):
        self.cambiar_medidas(400, 400)
        self.cambiar_imagen(0)
        self.cambiar_xy(Main.ancho * 6/24, Main.altura * 13/24)

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

    def dibujar(self, screen):

        if self.usando_timer:
            if Main.timer:
                if Main.timer > self.empieza and Main.timer < self.termina:
                    screen.blit(self.imagen, self.rect)
            
            else:
                self.usando_timer = False

