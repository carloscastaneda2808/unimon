"""
Archivo para crear los unimones
"""

import pygame
from copy import copy

from clase_main import Main

class Unimon:

    def __init__(self, key, tipo, 
                 hp, atk_fisico, df_fisico, atk_especial, df_especial, spe, 
                 estado, estado_duracion,
                 hb_posibles,
                 imagenes_rutas, x, y, ancho, altura,
                 dic):
        
        # Estadisticas
        self.tipo = tipo
        self.hp = hp
        self.hp_max = hp
        self.atk_fisico = atk_fisico
        self.df_fisico = df_fisico
        self.atk_especial = atk_especial
        self.df_especial = df_especial
        self.spe = spe
        self.spe_max = spe

        # Habilidades
        self.hb = set()
        self.hb_posibles = hb_posibles

        # Estado
        self.estado = estado
        self.estado_duracion = estado_duracion

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

        # Guardar en la clase
        if dic not in Main.unimones:
            Main.unimones[dic] = {}
        Main.unimones[dic][key] = self

    # Funcion para crear unimones
    def copiar_unimon(copiar, copiado, unimon):
        Main.unimones[copiar][unimon] = copy(Main.unimones[copiado][unimon])

    def eliminar_unimon(dic, unimon):
        Main.unimones[dic].pop(unimon)

    def unimon_ventana(unimon_dic, unimon, ventanas_dic, ventana, dic_elementos):
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][6] = unimon_dic
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][7].add(unimon)

    def eliminar_unimon_ventana(unimon_dic, unimon, ventanas_dic, ventana, dic_elementos):
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][7].remove(unimon)
    
    # Funciones
    def verificar_hp(self):
        return self.hp > 0

    # Funciones de Sprite
    def cambiar_front(self):
        self.cambiar_xy(Main.ancho * 9/12, Main.altura * 5/12)
        self.cambiar_imagen(0)

    def cambiar_back(self):
        self.cambiar_xy(Main.ancho * 3/12, Main.altura * 9/12)
        self.cambiar_imagen(1)

    def cambiar_imagen(self, index):
        self.index = index
        self.imagen = self.frames[self.index]
        self.rect = self.imagen.get_rect(center = (self.x, self.y))

    def cambiar_xy(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.imagen.get_rect(center = (self.x, self.y))

    def dibujar(self, screen):
        screen.blit(self.imagen, self.rect)

