"""
Archivo para crear elementos UI
"""

import pygame

from clase.clase_main import Main
from clase.cadena import Cadena

from visual.animacion import Animacion

class ElementoUI:

    def __init__(self, fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto, midleft = False):
        self.imagen = imagen_ruta
        self.fuente = fuente
        self.texto_color = texto_color
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.ancho_max = ancho
        self.ancho_nuevo = ancho

        # Solo se utiliza para las barras de vida
        self.midleft = midleft

        # Crear el texto
        self.texto_surf = fuente.render(texto, True, texto_color)
        self.texto_rect = self.texto_surf.get_rect(center=(x, y))

        # Gestionar el fondo (Si es imagen o color plano)
        if self.imagen:
            imagen_cargada = pygame.image.load(self.imagen).convert_alpha()
            self.rect_imagen = pygame.transform.scale(imagen_cargada, (ancho, alto))

            if midleft:
                self.rect = self.rect_imagen.get_rect(midleft=(x, y))
            else:
                self.rect = self.rect_imagen.get_rect(center=(x, y))

        else:
            self.rect = pygame.Rect(0, 0, ancho, alto)
            self.fondo_color = fondo_color

            if midleft:
                self.rect.midleft = (x, y)
            else:
                self.rect.center = (x, y)

        # Animacion
        self.usando_timer = False
        self.empieza = 0
        self.termina = 0

    # Modificar los elementos UI
    def cambiar_texto(self, texto):
        self.texto_surf = self.fuente.render(texto, True, self.texto_color)
        self.texto_rect = self.texto_surf.get_rect(center=(self.x, self.y))

    def cambiar_medidas(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

        if self.imagen:
            imagen_cargada = pygame.image.load(self.imagen).convert_alpha()
            self.rect_imagen = pygame.transform.scale(imagen_cargada, (ancho, alto))

            if self.midleft:
                self.rect = self.rect_imagen.get_rect(midleft=(self.x, self.y))
            else:
                self.rect = self.rect_imagen.get_rect(center=(self.x, self.y))
        else:
            self.rect = pygame.Rect(0, 0, ancho, alto)

            if self.midleft:
                self.rect.midleft = (self.x, self.y)
            else:
                self.rect.center = (self.x, self.y)

    def dibujar(self, screen):
        if self.usando_timer:
            if Main.timer:
                if Main.timer > self.empieza and Main.timer < self.termina and self.ancho > self.ancho_nuevo:
                    self.ancho -= 7
                    self.cambiar_medidas(self.ancho, self.alto)
                
                if Main.timer == self.termina:
                    unimon_usr = Main.unimones[Cadena.usuario][Main.unimon_usr]
                    unimon_npc = Main.unimones[Cadena.NPC][Main.unimon_npc]

                    Animacion.animacion_numero_hp(unimon_usr, unimon_npc)

            else:
                self.usando_timer = False

        # Verifica si tiene imagen para dibujarla
        if self.imagen:
            screen.blit(self.rect_imagen, self.rect)
        else:
            pygame.draw.rect(screen, self.fondo_color, self.rect)
        
        # Se dibuja el texto
        screen.blit(self.texto_surf, self.texto_rect)

    