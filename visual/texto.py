"""
Archivo para crear textos
"""

from clase.clase_main import Main
from visual.elemento_ui import ElementoUI

class Texto(ElementoUI):

    def __init__(self, key, fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto, dic):
        # Invoca a elementos UI
        super().__init__(fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto)
        
        # Se guarda en un dicccionario
        if dic not in Main.textos:
            Main.textos[dic] = {}
        Main.textos[dic][key] = self

    def cambiar_fondo(self, nuevo_fondo):
        if self.imagen:
            self.rect_imagen = nuevo_fondo
        else:
            self.fondo_color = nuevo_fondo

    # Funcion para crear botones
    def crear_titulo(dic, key, texto):
        Texto(key, Main.fuente_1, texto, Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, dic)

    def eliminar_texto(dic, key):
        Main.textos[dic].pop(key)

    def texto_ventana(texto, ventanas_dic, ventana, dic_elementos):
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][3].add(texto)

    def cambiar_texto(self, texto):
        self.texto_surf = self.fuente.render(texto, True, self.texto_color)
        self.texto_rect = self.texto_surf.get_rect(center=(self.x, self.y))

