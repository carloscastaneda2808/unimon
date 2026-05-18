"""
Archivo para crear botones
"""

from clases_visual.elemento_ui import ElementoUI

class Boton(ElementoUI):
    botones = {}

    def __init__(self, nombre, fuente, texto, texto_color, boton_color, imagen_ruta, x, y, ancho, alto, tipo, accion):
        # super() invoca a elementos UI
        super().__init__(fuente, texto, texto_color, boton_color, imagen_ruta, x, y, ancho, alto)
        self.tipo = tipo
        self.accion = accion
        
        # Se guarda en un diccionario
        Boton.botones[nombre] = self

    def collision(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)
    
    def cambiar_boton(self, nuevo_fondo):
        if self.imagen:
            self.rect_imagen = nuevo_fondo
        else:
            self.fondo_color = nuevo_fondo
