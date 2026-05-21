"""
Archivo para crear elementos UI
"""

import pygame

class ElementoUI:

    def __init__(self, fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto,):
        self.imagen = imagen_ruta

        # Crear el texto
        self.texto_surf = fuente.render(texto, True, texto_color)
        self.texto_rect = self.texto_surf.get_rect(center=(x, y))

        # Gestionar el fondo (Si es imagen o color plano)
        if self.imagen:
            imagen_cargada = pygame.image.load(self.imagen)
            self.rect_imagen = pygame.transform.scale(imagen_cargada, (ancho, alto))
            self.rect = self.rect_imagen.get_rect(center=(x, y))
        else:
            self.rect = pygame.Rect(0, 0, ancho, alto)
            self.rect.center = (x, y)
            self.fondo_color = fondo_color

    def dibujar(self, screen):
        # Verifica si tiene imagen para dibujarla
        if self.imagen:
            screen.blit(self.rect_imagen, self.rect)
        else:
            pygame.draw.rect(screen, self.fondo_color, self.rect)
        
        # Se dibuja el texto
        screen.blit(self.texto_surf, self.texto_rect)