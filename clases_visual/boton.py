"""
Archivo para crear botones
"""

from elemento_ui import ElementoUI

class Boton(ElementoUI):
    botones = {}

    def __init__(self, nombre, x, y, ancho, alto, fuente, texto, texto_color, boton_color, imagen_ruta=None):
        # super() invoca a elementos UI
        super().__init__(x, y, ancho, alto, fuente, texto, texto_color, boton_color, imagen_ruta)
        
        # Se guarda en un diccionario
        Boton.botones[nombre] = self

    def collision(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)
    
    def cambiar_boton(self, nuevo_fondo):
        if self.imagen:
            self.rect_imagen = nuevo_fondo
        else:
            self.fondo_color = nuevo_fondo
