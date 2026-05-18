"""
Archivo para crear textos
"""

from elemento_ui import ElementoUI

class Texto(ElementoUI):
    textos = {}

    def __init__(self, nombre, x, y, ancho, alto, fuente, texto, texto_color, fondo_color, imagen_ruta=None):
        # Invoca a elementos UI
        super().__init__(x, y, ancho, alto, fuente, texto, texto_color, fondo_color, imagen_ruta)
        
        # Se guarda en un dicccionario
        Texto.textos[nombre] = self

    def cambiar_fondo(self, nuevo_fondo):
        if self.imagen:
            self.rect_imagen = nuevo_fondo
        else:
            self.fondo_color = nuevo_fondo
        
