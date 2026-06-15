"""
Archivo para crear textos
"""

from settings.settings import Main
from visual.elemento_ui import ElementoUI

class Texto(ElementoUI):

    def __init__(self, key, fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto, dic, midleft = False):
        # Hereda elementos UI
        super().__init__(fuente, texto, texto_color, fondo_color, imagen_ruta, x, y, ancho, alto, midleft)
        
        # Se guarda en un dicccionario
        if dic not in Main.textos:
            Main.textos[dic] = {}
        Main.textos[dic][key] = self

    # Cambia el fondo
    def cambiar_fondo(self, nuevo_fondo):
        if self.imagen:
            self.rect_imagen = nuevo_fondo
        else:
            self.fondo_color = nuevo_fondo

    # Funciones para crear, eliminar o modificar textos
    def crear_titulo(dic, key, texto):
        Texto(key, Main.fuente_1, texto, Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, dic)

    def eliminar_texto(dic, key):
        Main.textos[dic].pop(key)

    # Funciones para agregar o quitar textos de una venta
    def texto_ventana(texto, ventanas_dic, ventana, dic_elementos):
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][3].add(texto)

    def eliminar_texto_ventana(texto, ventanas_dic, ventana, dic_elementos):
        Main.ventanas[ventanas_dic][ventana].dic_elementos[dic_elementos][3].remove(texto)

