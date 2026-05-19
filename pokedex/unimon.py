"""
Archivo para crear los unimones
"""

import pygame

pygame.init()

info_pantalla = pygame.display.Info()
ancho = info_pantalla.current_w
altura = info_pantalla.current_h

class Unimon:
    unimones = {}

    def __init__(self, nombre, tipo, 
                 hp, atk_fisico, df_fisico, atk_especial, df_especial, spe, 
                 estado, estado_duracion,
                 hb_posibles,
                 imagenes_rutas, x, y, ancho, altura):
        
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
        self.hb = []
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
        Unimon.unimones[nombre] = self
    
    # Funciones
    def verificar_hp(self):
        return self.hp > 0

    # Funciones de Sprite
    def cambiar_front(self):
        self.cambiar_xy(ancho * 9/12, altura * 5/12)
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

