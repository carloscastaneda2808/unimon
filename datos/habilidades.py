"""
Archivo para datos de las habilidades
"""

from settings.settings import Main
from pokedex.habilidad import Habilidad

# 48 Habilidades
def datos_habilidades():

    # FUEGO
    Habilidad("Lanzallamas", "Fuego", 90, 15, 100, "Especial", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Llamarada", "Fuego", 110, 5, 85, "Especial", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("EnviteÍgneo", "Fuego", 120, 15, 100, "Físico", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("ColmilloÍgneo", "Fuego", 65, 15, 95, "Físico", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("GiroFuego", "Fuego", 35, 15, 85, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("PuñoFuego", "Fuego", 75, 15, 100, "Físico", "Quemado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    
    Habilidad("Sofoco", "Fuego", 130, 5, 90, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # AGUA
    Habilidad("Surf", "Agua", 90, 15, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Hidrobomba", "Agua", 110, 5, 80, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Cascada", "Agua", 80, 15, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Hidrocañón", "Agua", 150, 5, 90, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    
    Habilidad("Hidrobomba", "Agua", 110, 5, 80, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # PLANTA
    Habilidad("HojaAfilada", "Planta", 55, 25, 95, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("RayoSolar", "Planta", 120, 10, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("LátigoCepa", "Planta", 45, 25, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Somnífero", "Planta", 0, 10, 80, "Estado", "Dormido", 100,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    
    Habilidad("GigaDrenado", "Planta", 75, 10, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # ELÉCTRICO
    Habilidad("Rayo", "Eléctrico", 90, 15, 100, "Especial", "Paralizado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Trueno", "Eléctrico", 110, 10, 70, "Especial", "Paralizado", 30,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("PuñoTrueno", "Eléctrico", 75, 15, 100, "Físico", "Paralizado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("OndaTrueno", "Eléctrico", 0, 20, 90, "Estado", "Paralizado", 100,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("OndaVoltio", "Eléctrico", 60, 20, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Chispazo", "Eléctrico", 80, 15, 100, "Especial", "Paralizado", 30,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Impactrueno", "Eléctrico", 40, 30, 100, "Especial", "Paralizado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # HIELO
    Habilidad("RayoHielo", "Hielo", 90, 10, 100, "Especial", "Congelado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Ventisca", "Hielo", 110, 5, 70, "Especial", "Congelado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    
    Habilidad("PuñoHielo", "Hielo", 75, 15, 100, "Físico", "Congelado", 10,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # VENENO
    Habilidad("BombaLodo", "Veneno", 90, 10, 100, "Especial", "Envenenado", 30,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Tóxico", "Veneno", 0, 10, 85, "Estado", "GravementeEnvenenado", 100,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    
    Habilidad("Ácido", "Veneno", 40, 30, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")



    # TIERRA
    Habilidad("Terremoto", "Tierra", 100, 10, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    
    Habilidad("TierraViva", "Tierra", 90, 10, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")



    # ROCA
    Habilidad("RocaAfilada", "Roca", 100, 5, 80, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    
    Habilidad("Avalancha", "Roca", 75, 10, 90, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # LUCHA
    Habilidad("ABocajarro", "Lucha", 120, 5, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Sumisión", "Lucha", 80, 20, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("TajoCruzado", "Lucha", 100, 5, 80, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # PSÍQUICO
    Habilidad("Psíquico", "Psíquico", 90, 10, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    
    Habilidad("Psicocorte", "Psíquico", 70, 20, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # FANTASMA
    Habilidad("BolaSombra", "Fantasma", 80, 15, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # BICHO
    Habilidad("TijeraX", "Bicho", 80, 15, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # VOLADOR
    Habilidad("TajoAéreo", "Volador", 75, 15, 95, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # DRAGÓN
    Habilidad("GarraDragón", "Dragon", 80, 15, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")


    # NORMAL
    Habilidad("Hiperrayo", "Normal", 150, 5, 90, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("VelocidadExtrema", "Normal", 80, 5, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("AtaqueRápido", "Normal", 40, 30, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    
    Habilidad("Triataque", "Normal", 80, 10, 100, "Especial", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("CuerpoPesado", "Normal", 80, 10, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    

    
    # SINIESTRO
    Habilidad("Triturar", "Siniestro", 80, 15, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")

    Habilidad("Mordisco", "Siniestro", 60, 25, 100, "Físico", "Nada", 0,
            ["images/habilidades/habilidad_generica.png"],
            Main.ancho * 9/12, Main.altura * 5/12, 500, 500,
            "main")
    