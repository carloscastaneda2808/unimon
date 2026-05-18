"""
Archivo para crear botones
"""
import pygame
from copy import copy

from pokedex.unimon import Unimon

pygame.init()

class Boton:
    def __init__(self, fuente, texto, color, centro, tamanio, fondo, dato = None):
        self.surf = fuente.render(texto, True, color)
        self.rect = self.surf.get_rect(center = centro)
        self.boton = pygame.Rect(0, 0, tamanio[0], tamanio[1])
        self.boton.center = self.rect.center
        self.fondo = fondo
        self.dato = dato

    def cambiar_fondo(self, nuevo_fondo):
        self.fondo = copy(nuevo_fondo)

    def dibujar(self, screen):
        pygame.draw.rect(screen, self.fondo, self.boton)
        screen.blit(self.surf, self.rect)

    def collision(self, pos_mouse):
        return self.boton.collidepoint(pos_mouse)
