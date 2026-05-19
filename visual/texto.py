"""
Archivo para crear textos
"""

from visual.elemento_ui import ElementoUI

class Texto(ElementoUI):
    textos = {}

    def __init__(self, nombre, fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto):
        # Invoca a elementos UI
        super().__init__(fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto)
        
        # Se guarda en un dicccionario
        Texto.textos[nombre] = self

    def cambiar_fondo(self, nuevo_fondo):
        if self.imagen:
            self.rect_imagen = nuevo_fondo
        else:
            self.fondo_color = nuevo_fondo
        
