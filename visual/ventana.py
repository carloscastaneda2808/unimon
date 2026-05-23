"""
Archivo para crear ventanas
"""
from clase.clase_main import Main
from clase.cadena import Cadena

class Ventana:

    def __init__(self, key,  dic_elementos, dic_ventanas):

        for llave in dic_elementos.keys():
            dic_elementos[llave].append(None)
            dic_elementos[llave].append(set())
            dic_elementos[llave].append(None)
            dic_elementos[llave].append(set())

        self.dic_elementos = dic_elementos

        # imagenes_dic = value[0]
        # imagenes = value[1]

        # textos_dic = value[2]
        # textos = value[3]

        # botones_dic = value[4]
        # botones = value[5]

        # unimones_dic = value[6]
        # unimones = value[7]

        # habilidades_dic = value[8]
        # habilidades = value[9]

        if dic_ventanas not in Main.ventanas:
            Main.ventanas[dic_ventanas] = {}
        Main.ventanas[dic_ventanas][key] = self

    def crear_ventana(dic_ventanas, key, dic_elementos):
        if dic_elementos["a"][0] == None:
            dic_elementos["a"][0] = "main"
        
        if dic_elementos["a"][1] == None:
            dic_elementos["a"][1] = {"inicio"}

        Ventana(key, dic_elementos, dic_ventanas)

    def eliminar_ventana(dic, key):
        Main.ventanas[dic].pop(key)

    def crear_dic_elementos(self, key, imagenes_dic, textos_dic, botones_dic):

        if key not in self.dic_elementos:
            self.dic_elementos[key] = [imagenes_dic, set(), textos_dic, set(), botones_dic, set(), None, set(), None, set()]

    def eliminar_dic_elementos(self, key):
        
        if key in self.dic_elementos:
            self.dic_elementos.pop(key)

    def hover(self, pos_mouse):
        for value in self.dic_elementos.values():

            for key in value[5]:
                boton = Main.botones[value[4]][key]

                if boton.collision(pos_mouse):
                    boton.cambiar_fondo(Main.azul_oscuro)

                else:
                    boton.cambiar_fondo(Main.azul)

    # Click izquierdo
    def collision_1(self, pos_mouse):
        for value in self.dic_elementos.values():

            for key in value[5]:
                boton = Main.botones[value[4]][key]

                if boton.collision(pos_mouse):
                    if boton.funcion_1:
                        boton.funcion_1(value[4], key)

    # Click derecho
    def collision_2(self, pos_mouse):
        for value in self.dic_elementos.values():

            for key in value[5]:
                boton = Main.botones[value[4]][key]

                if boton.collision(pos_mouse):
                    if boton.funcion_2:
                        boton.funcion_2(value[4], key)

    # Click rueda
    def collision_3(self, pos_mouse):
        for value in self.dic_elementos.values():

            for key in value[5]:
                boton = Main.botones[value[4]][key]

                if boton.collision(pos_mouse):
                    if boton.funcion_3:
                        boton.funcion_3(value[4], key)

    def dibujar(self, screen):

        # Primero se dibuja el fondo
        for value in self.dic_elementos.values():

            for key in value[1]:
                Main.imagenes[value[0]][key].dibujar(screen)

        # Segundo se dibujan los unimones
        for value in self.dic_elementos.values():

            for key in value[7]:
                Main.unimones[value[6]][key].dibujar(screen)

        # Tercero se dibujan las habilidades
        for value in self.dic_elementos.values():

            for key in value[9]:
                Main.habilidades[value[8]][key].dibujar(screen)

        # Cuarto se dibujan los textos y los botones
        for value in self.dic_elementos.values():

            for key in value[3]:
                Main.textos[value[2]][key].dibujar(screen)

            for key in value[5]:
                Main.botones[value[4]][key].dibujar(screen)
