"""
Archivo para los datos de lo visual
"""

from clase_main import Main
from visual.boton import Boton
from visual.texto import Texto
from visual.ventana import Ventana
from visual.imagen import Imagen

def datos_visual():
    # Imagenes
    Imagen("inicio", "images/backround/inicio.jpg", Main.ancho, Main.altura, 0, 0, "main")

    # Textos
    Texto("inicio", Main.fuente_1, "Unimon", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, "main")
    Texto("elegir_unimones", Main.fuente_1, "Elegir Unimon", Main.negro, Main.verde, None, Main.ancho / 2, Main.altura / 10, 700, 110, "main")
    Texto("elegir_habilidades", Main.fuente_1, "Elegir Habilidades", Main.negro, Main.verde, None, Main.ancho / 2, Main.altura / 10, 700, 110, "main")
    Texto("estadisticas", Main.fuente_1, "Estadisticas", Main.negro, Main.verde, None, Main.ancho / 2, Main.altura / 10, 700, 110, "main")
    Texto("configuracion", Main.fuente_1, "Configuracion", Main.negro, Main.verde, None, Main.ancho / 2, Main.altura / 10, 700, 110, "main")
    Texto("combate", Main.fuente_1, "Combate", Main.negro, Main.verde, None, Main.ancho / 2, Main.altura / 10, 700, 110, "main")
    Texto("atacar", Main.fuente_1, "Atacar", Main.negro, Main.verde, None, Main.ancho / 2, Main.altura / 10, 700, 110, "main")
    Texto("sacar", Main.fuente_1, "Sacar", Main.negro, Main.verde, None, Main.ancho / 2, Main.altura / 10, 700, 110, "main")

    # Botones
    # Inicio
    Boton("jugar", Main.fuente_2, "Jugar", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 3/10, 400, 80, Boton.ventana_elegir_unimones, None, "main")
    Boton("estadisticas", Main.fuente_2, "Estadisticas", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 5/10, 400, 80, Boton.ventana_estadisticas, None, "main")
    Boton("configuracion", Main.fuente_2, "Configuracion", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 7/10, 400, 80, Boton.ventana_configuracion, None, "main")
    Boton("salir", Main.fuente_2, "Salir", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 9/10, 400, 80, Boton.ventana_salir, None, "main")

    # Elegir Unimones
    Boton("atras_1", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/4, Main.altura * 9/10, 400, 80, Boton.ventana_inicio, None, "main")
    Boton("seguir_1", Main.fuente_2, "Seguir", Main.negro, Main.azul, None, Main.ancho * 3/4, Main.altura * 9/10, 400, 80, Boton.ventana_elegir_habilidades, None, "main")

    # Elegir Habilidades
    Boton("atras_2", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/4, Main.altura * 9/10, 400, 80, Boton.ventana_elegir_unimones, None, "main")
    Boton("seguir_2", Main.fuente_2, "Seguir", Main.negro, Main.azul, None, Main.ancho * 3/4, Main.altura * 9/10, 400, 80, Boton.ventana_sacar, None, "main")

    # Estadisticas y Configuracion
    Boton("atras_3", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 9/10, 400, 80, Boton.ventana_inicio, None, "main")

    # Combate
    Boton("atacar", Main.fuente_2, "Atacar", Main.negro, Main.azul, None, Main.ancho * 1/6, Main.altura * 9/10, 400, 80, Boton.ventana_atacar, None, "main")
    Boton("sacar", Main.fuente_2, "Sacar", Main.negro, Main.azul, None, Main.ancho * 3/6, Main.altura * 9/10, 400, 80, Boton.ventana_sacar, None, "main")
    Boton("huir", Main.fuente_2, "Huir", Main.negro, Main.azul, None, Main.ancho * 5/6, Main.altura * 9/10, 400, 80, Boton.ventana_inicio, None, "main")

    # Atacar y Sacar
    Boton("atras_4", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 9/10, 400, 80, Boton.ventana_combate, None, "main")

    # Boton de cada unimon de elegir_habilidades
    Boton("atras_5", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 9/10, 400, 80, Boton.ventana_elegir_habilidades, None, "main")

    # Ventanas
    Ventana("inicio",
            {"a" : ["main", {"inicio"},
            "main", {"inicio"},
            "main", {"jugar", "estadisticas", "configuracion", "salir"}]},
            "main")

    Ventana("elegir_unimones",
            {"a" : ["main", {"inicio"},
            "main", {"elegir_unimones"},
            "main", {"atras_1", "seguir_1"}]},
            "main")

    Ventana("elegir_habilidades",
            {"a" : ["main", {"inicio"},
            "main", {"elegir_habilidades"},
            "main", {"atras_2", "seguir_2"}]},
            "main")

    Ventana("estadisticas",
            {"a" : ["main", {"inicio"},
            "main", {"estadisticas"},
            "main", {"atras_3"}]},
            "main")

    Ventana("configuracion",
            {"a" : ["main", {"inicio"},
            "main", {"configuracion"},
            "main", {"atras_3"}]},
            "main")

    Ventana("combate",
            {"a" : ["main", {"inicio"},
            "main", {"combate"},
            "main", {"atacar", "sacar", "huir"}]},
            "main")

    Ventana("atacar",
            {"a" : ["main", {"inicio"},
            "main", {"atacar"},
            "main", {"atras_4"}]},
            "main")

    Ventana("sacar",
            {"a" : ["main", {"inicio"},
            "main", {"sacar"},
            "main", {"atras_4"}]},
            "main")