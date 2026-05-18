"""
Archivo para crear ventanas
"""

class Ventana:
    ventanas = {}

    def __init__(self, nombre, textos, botones):
        self.textos = textos
        self.botones = botones

        Ventana.ventanas[nombre] = self

    def dibujar(self, screen):
        for texto in self.textos:
            texto.dibujar(screen)

        for boton in self.botones:
            boton.dibujar(screen)