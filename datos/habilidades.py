"""
Archivo para datos de las habilidades
"""

import pygame
from pokedex.habilidad import Habilidad

pygame.init()

info_pantalla = pygame.display.Info()
ancho = info_pantalla.current_w
altura = info_pantalla.current_h

def datos_habilidades():
    Habilidad("Lanzallamas", "Fuego", 90, 15, 100, "Especial", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Llamarada", "Fuego", 110, 5, 85, "Especial", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("EnviteÍgneo", "Fuego", 120, 15, 100, "Físico", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("ColmilloÍgneo", "Fuego", 65, 15, 95, "Físico", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("GiroFuego", "Fuego", 35, 15, 85, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("AnilloÍgneo", "Fuego", 150, 5, 90, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("PuñoFuego", "Fuego", 75, 15, 100, "Físico", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Sofoco", "Fuego", 130, 5, 90, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Surf", "Agua", 90, 15, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Hidrobomba", "Agua", 110, 5, 80, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Cascada", "Agua", 80, 15, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("PistolaAgua", "Agua", 40, 25, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Hidrocañón", "Agua", 150, 5, 90, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Martillazo", "Agua", 100, 10, 90, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("RayoBurbuja", "Agua", 65, 20, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Tenaza", "Agua", 35, 15, 85, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("HojaAfilada", "Planta", 55, 25, 95, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("RayoSolar", "Planta", 120, 10, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("LátigoCepa", "Planta", 45, 25, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("PlantaFeroz", "Planta", 150, 5, 90, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Somnífero", "Planta", 0, 10, 80, "Estado", "Dormido", 100,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Espora", "Planta", 0, 15, 100, "Estado", "Dormido", 100,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("GigaDrenado", "Planta", 75, 10, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Rayo", "Eléctrico", 90, 15, 100, "Especial", "Paralizado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Trueno", "Eléctrico", 110, 10, 70, "Especial", "Paralizado", 30,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("PuñoTrueno", "Eléctrico", 75, 15, 100, "Físico", "Paralizado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Impactrueno", "Eléctrico", 40, 30, 100, "Especial", "Paralizado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("OndaVoltio", "Eléctrico", 60, 20, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Chispazo", "Eléctrico", 80, 15, 100, "Especial", "Paralizado", 30,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("VoltioCruel", "Eléctrico", 90, 15, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("OndaTrueno", "Eléctrico", 0, 20, 90, "Estado", "Paralizado", 100,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("RayoHielo", "Hielo", 90, 10, 100, "Especial", "Congelado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Ventisca", "Hielo", 110, 5, 70, "Especial", "Congelado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("PuñoHielo", "Hielo", 75, 15, 100, "Físico", "Congelado", 10,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("BombaLodo", "Veneno", 90, 10, 100, "Especial", "Envenenado", 30,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Tóxico", "Veneno", 0, 10, 85, "Estado", "GravementeEnvenenado", 100,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Terremoto", "Tierra", 100, 10, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("RocaAfilada", "Roca", 100, 5, 80, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("ABocajarro", "Lucha", 120, 5, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Psíquico", "Psíquico", 90, 10, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("BolaSombra", "Fantasma", 80, 15, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("TijeraX", "Bicho", 80, 15, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("TajoAéreo", "Volador", 75, 15, 95, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("GarraDragón", "Dragon", 80, 15, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Dragoaliento", "Dragon", 60, 20, 100, "Especial", "Paralizado", 30,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Hiperrayo", "Normal", 150, 5, 90, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("VelocidadExtrema", "Normal", 80, 5, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("AtaqueRápido", "Normal", 40, 30, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Triataque", "Normal", 80, 10, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Triturar", "Siniestro", 80, 15, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)

    Habilidad("Mordisco", "Siniestro", 60, 25, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            ancho * 9/12, altura * 5/12, 500, 500)