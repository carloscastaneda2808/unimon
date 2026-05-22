"""
Archivo para crear los unimones
"""

import pygame

from copy import copy

from clase.clase_main import Main

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
        self.atk_fisico = atk_fisico
        self.df_fisico = df_fisico
        self.atk_especial = atk_especial
        self.df_especial = df_especial
        self.spe = spe

        self.hp_max = hp
        self.atk_fisico_max = atk_fisico
        self.spe_max = spe

        # Habilidades
        self.hb = set()
        self.hb_posibles = hb_posibles

        # Estado
        self.estado = estado
        self.estado_duracion = estado_duracion

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
        self.index = 1
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

    def eliminar_unimon_ventana(unimon, ventanas_dic, ventana, dic_elementos):
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][6] = None
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][7].remove(unimon)
    
    # Funciones
    def restar_hp(self, danio):
        self.hp -= round(danio)

        if self.hp < 0: 
            self.hp = 0

    def verificar_hp(self):
        return self.hp > 0

    # Funciones de Sprite
    def cambiar_front(self):
        self.cambiar_medidas(400, 400)
        self.cambiar_imagen(0)
        self.cambiar_xy(Main.ancho * 9/12, Main.altura * 5/12)

    def cambiar_back(self):
        self.cambiar_medidas(600, 600)
        self.cambiar_imagen(1)
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

    def dibujar(self, screen):
        if self.usando_timer:
            if Main.timer:
                if Main.timer > self.empieza and Main.timer < self.termina:
                    self.y += 10
                    self.cambiar_xy(self.x, self.y)

            else:
                self.usando_timer = False
            
        screen.blit(self.imagen, self.rect)

