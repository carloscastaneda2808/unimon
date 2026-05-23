"""
Archivo para los datos de lo visual
"""

from clase.clase_main import Main
from visual.boton import Boton
from visual.texto import Texto
from visual.ventana import Ventana
from visual.imagen import Imagen

def datos_visual():
    # Imagenes
    Imagen("inicio", "images/backround/inicio.jpg", 0, 0, Main.ancho, Main.altura, "main")

    # Textos
    Texto("inicio", Main.fuente_1, "Unimon", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, "main")
    Texto("elegir_unimones", Main.fuente_1, "Elegir Unimon", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, "main")
    Texto("elegir_habilidades", Main.fuente_1, "Elegir Habilidades", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, "main")
    Texto("combate", Main.fuente_1, "Combate", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, "main")
    Texto("atacar", Main.fuente_1, "Atacar", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, "main")
    Texto("sacar", Main.fuente_1, "Sacar", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, "main")

    # Combate
    Texto("gris", Main.fuente_1, "", Main.negro, Main.gris, None, Main.ancho * 1/2, Main.altura * 7/8, Main.ancho, Main.altura * 1/4, "main")
    
    Texto("cuadro_usr", Main.fuente_1, "", Main.negro, Main.gris, None, Main.ancho * 19/24, Main.altura * 15/24, 500, 150, "main")
    Texto("cuadro_npc", Main.fuente_1, "", Main.negro, Main.gris, None, Main.ancho * 5/24, Main.altura * 4/24, 500, 150, "main")

    Texto("unimon_usr", Main.fuente_3, "", Main.negro, Main.gris, None, Main.ancho * 17/24, Main.altura * 14/24, 0, 0, "main")
    Texto("unimon_npc", Main.fuente_3, "", Main.negro, Main.gris, None, Main.ancho * 3/24, Main.altura * 3/24, 0, 0, "main")

    Texto("estado_usr", Main.fuente_3, "", Main.negro, Main.gris, None, Main.ancho * 21/24, Main.altura * 14/24, 0, 0, "main")
    Texto("estado_npc", Main.fuente_3, "", Main.negro, Main.gris, None, Main.ancho * 7/24, Main.altura * 3/24, 0, 0, "main")

    Texto("numero_hp_usr", Main.fuente_3, "", Main.negro, Main.gris, None, Main.ancho * 17/24, Main.altura * 15/24, 0, 0, "main")
    Texto("numero_hp_npc", Main.fuente_3, "", Main.negro, Main.gris, None, Main.ancho * 3/24, Main.altura * 4/24, 0, 0, "main")

    Texto("hp_usr", Main.fuente_1, "", Main.negro, Main.verde, None, Main.ancho * 16/24, Main.altura * 16/24, 400, 30, "main", True)
    Texto("hp_npc", Main.fuente_1, "", Main.negro, Main.verde, None, Main.ancho * 2/24, Main.altura * 5/24, 400, 30, "main", True)

    Texto("resultado", Main.fuente_1, "", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 5/10, 700, 110, "main")

    # Stats
    Texto("stats", Main.fuente_1, "Stats", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, "main")
    Texto("cuadro_stats", Main.fuente_3, "", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 13/24, 500, 600, "main")

    Texto("linea_1", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 6/24, 0, 0, "stats")
    Texto("linea_2", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 8/24, 0, 0, "stats")
    Texto("linea_3", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 10/24, 0, 0, "stats")
    Texto("linea_4", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 12/24, 0, 0, "stats")
    Texto("linea_5", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 14/24, 0, 0, "stats")
    Texto("linea_6", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 16/24, 0, 0, "stats")
    Texto("linea_7", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 18/24, 0, 0, "stats")
    Texto("linea_8", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 20/24, 0, 0, "stats")

    # Estadisticas
    Texto("estadisticas", Main.fuente_1, "Estadisticas", Main.negro, Main.verde, None, Main.ancho *  1/2, Main.altura * 1/10, 700, 110, "main")
    Texto("cuadro_estadisticas", Main.fuente_3, "", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 13/24, 500, 600, "main")

    Texto("linea_1", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 6/24, 0, 0, "estadisticas")
    Texto("linea_2", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 8/24, 0, 0, "estadisticas")
    Texto("linea_3", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 10/24, 0, 0, "estadisticas")
    Texto("linea_4", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 12/24, 0, 0, "estadisticas")
    Texto("linea_5", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 14/24, 0, 0, "estadisticas")
    Texto("linea_6", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 16/24, 0, 0, "estadisticas")
    Texto("linea_7", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 18/24, 0, 0, "estadisticas")
    Texto("linea_8", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 20/24, 0, 0, "estadisticas")

    # Ayuda
    Texto("configuracion", Main.fuente_1, "Ayuda", Main.negro, Main.verde, None, Main.ancho * 1/2, Main.altura * 1/10, 700, 110, "main")
    Texto("cuadro_configuracion", Main.fuente_3, "", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 13/24, 800, 500, "main")

    Texto("linea_1", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 6/24, 0, 0, "configuracion")
    Texto("linea_2", Main.fuente_2, "Unimon es un juego por turnos,", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 8/24, 0, 0, "configuracion")
    Texto("linea_3", Main.fuente_2, "puedes elegir un maximo de", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 10/24, 0, 0, "configuracion")
    Texto("linea_4", Main.fuente_2, "6 unimones y 4 habilidades.", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 12/24, 0, 0, "configuracion")
    Texto("linea_5", Main.fuente_2, "Click izquierdo para seleccionar.", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 14/24, 0, 0, "configuracion")
    Texto("linea_6", Main.fuente_2, "Click derecho para quitar selecciones.", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 16/24, 0, 0, "configuracion")
    Texto("linea_7", Main.fuente_2, "Click central para ver stats.", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 18/24, 0, 0, "configuracion")
    Texto("linea_8", Main.fuente_2, "", Main.negro, Main.amarillo, None, Main.ancho * 12/24, Main.altura * 20/24, 0, 0, "configuracion")    

    # Botones
    # Inicio
    Boton("jugar", Main.fuente_2, "Jugar", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 3/10, 400, 80, Boton.ventana_elegir_unimones, None, None, None, "main")
    Boton("estadisticas", Main.fuente_2, "Estadisticas", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 5/10, 400, 80, Boton.ventana_estadisticas, None, None, None, "main")
    Boton("configuracion", Main.fuente_2, "Ayuda", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 7/10, 400, 80, Boton.ventana_configuracion, None, None, None, "main")
    Boton("salir", Main.fuente_2, "Salir", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 9/10, 400, 80, Boton.ventana_salir, None, None, None, "main")

    # Elegir Unimones
    Boton("atras_1", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/4, Main.altura * 9/10, 400, 80, Boton.ventana_inicio, None, None, None, "main")
    Boton("seguir_1", Main.fuente_2, "Seguir", Main.negro, Main.azul, None, Main.ancho * 3/4, Main.altura * 9/10, 400, 80, Boton.ventana_elegir_habilidades, None, None, None, "main")

    # Elegir Habilidades
    Boton("atras_2", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/4, Main.altura * 9/10, 400, 80, Boton.ventana_elegir_unimones, None, None, None, "main")
    Boton("seguir_2", Main.fuente_2, "Seguir", Main.negro, Main.azul, None, Main.ancho * 3/4, Main.altura * 9/10, 400, 80, Boton.ventana_sacar, None, None, None, "main")

    # Estadisticas
    Boton("atras_6", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/5, Main.altura * 9/10, 400, 80, Boton.ventana_inicio, None, None, None, "main")
    Boton("borrar_historial", Main.fuente_2, "Borrar Historial", Main.negro, Main.azul, None, Main.ancho * 4/5, Main.altura * 9/10, 400, 80, Boton.borrar_historial, None, None, None, "main")

    # Configuracion
    Boton("atras_3", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 9/10, 400, 80, Boton.ventana_inicio, None, None, None, "main")

    # Combate
    Boton("atacar", Main.fuente_2, "Atacar", Main.negro, Main.azul, None, Main.ancho * 4/24, Main.altura * 22/24, 400, 80, Boton.ventana_atacar, None, None, None, "main")
    Boton("sacar", Main.fuente_2, "Sacar", Main.negro, Main.azul, None, Main.ancho * 12/24, Main.altura * 22/24, 400, 80, Boton.ventana_sacar, None, None, None, "main")
    Boton("huir", Main.fuente_2, "Huir", Main.negro, Main.azul, None, Main.ancho * 20/24, Main.altura * 22/24, 400, 80, Boton.ventana_inicio, None, None, None, "main")

    # Atacar y Sacar
    Boton("atras_4", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 9/10, 400, 80, Boton.ventana_combate, None, None, None, "main")

    # Boton de cada unimon de elegir_habilidades
    Boton("atras_5", Main.fuente_2, "Atrás", Main.negro, Main.azul, None, Main.ancho * 1/2, Main.altura * 9/10, 400, 80, Boton.ventana_elegir_habilidades, None, None, None, "main")

    # Ventanas
    Ventana("inicio",
            {"a" : 
             ["main", {"inicio"},
            "main", {"inicio"},
            "main", {"jugar", "estadisticas", "configuracion", "salir"}]},
            "main")

    Ventana("elegir_unimones",
            {"a" : 
             ["main", {"inicio"},
            "main", {"elegir_unimones"},
            "main", {"atras_1", "seguir_1"}]},
            "main")

    Ventana("elegir_habilidades",
            {"a" : 
             ["main", {"inicio"},
            "main", {"elegir_habilidades"},
            "main", {"atras_2", "seguir_2"}]},
            "main")

    Ventana("estadisticas",
            {"a" : 
             ["main", {"inicio"},
            "main", {"estadisticas", "cuadro_estadisticas"},
            "main", {"atras_6", "borrar_historial"}],

            "b" :
            [None, set(),
             "estadisticas", {"linea_1", "linea_2", "linea_3", "linea_4", "linea_5", "linea_6", "linea_7", "linea_8"},
             None, set()]},
            "main")

    Ventana("configuracion",
            {"a" : 
             ["main", {"inicio"},
            "main", {"configuracion", "cuadro_configuracion"},
            "main", {"atras_3"}],

            "b" :
            [None, set(),
             "configuracion", {"linea_1", "linea_2", "linea_3", "linea_4", "linea_5", "linea_6", "linea_7", "linea_8"},
             None, set()]},
            "main")

    Ventana("combate",
            
            {"a" : 
             ["main", {"inicio"},
            "main", {"gris"},
            None, set()],

            "c" :
            [None, set(),
             "main", {"cuadro_usr", "cuadro_npc"},
             "main", {"atacar", "sacar", "huir"}],

            "d" : 
            [None, set(),
             "main", {"unimon_usr", "unimon_npc", "hp_usr", "hp_npc", "estado_usr", "estado_npc", "numero_hp_usr", "numero_hp_npc"},
             None, set()]},
            "main")

    Ventana("atacar",
            {"a" : 
             ["main", {"inicio"},
            "main", {"atacar"},
            "main", {"atras_4"}]},
            "main")

    Ventana("sacar",
            {"a" : 
             ["main", {"inicio"},
            "main", {"sacar"},
            "main", {"atras_4"}]},
            "main")
    
    Ventana("resultado", 
            {"a": 
             ["main", {"inicio"}, 
              "main", {"resultado"}, 
              "main", {"atras_3"}]}, 
              "main")
    
    Ventana("stats",
            {"a":
             ["main", {"inicio"},
              "main", {"stats", "cuadro_stats"},
              None, set()],
            "b":
             [None, set(),
              "stats", {"linea_1", "linea_2", "linea_3", "linea_4", "linea_5", "linea_6", "linea_7", "linea_8"},
              None, set()]},
              "main")