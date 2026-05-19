"""
Archivo para crear ventanas
"""

class Ventana:
    ventanas = {}

    def __init__(self, nombre, imagenes, textos, botones):
        self.imagenes = imagenes
        self.textos = textos
        self.botones = botones

        Ventana.ventanas[nombre] = self

    def hover(self, pos_mouse, azul, azul_oscuro):
        for boton in self.botones:
            if boton.collision(pos_mouse):
                boton.cambiar_fondo(azul_oscuro)
            else:
                boton.cambiar_fondo(azul)

    def collision(self, pos_mouse, azul):
        for boton in self.botones:
            if boton.collision(pos_mouse):
                boton.cambiar_fondo(azul)
                return boton.funcion()
        return None

    def dibujar(self, screen):
        for imagen in self.imagenes:
            imagen.dibujar(screen)

        for texto in self.textos:
            texto.dibujar(screen)

        for boton in self.botones:
            boton.dibujar(screen)