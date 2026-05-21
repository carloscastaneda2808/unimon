"""
Archivo para los datos de los unimones
"""

import pygame

from clase.main import Main
from pokedex.unimon import Unimon
# from pokedex.habilidad import Habilidad

from datos.habilidades import datos_habilidades

def datos_unimones():
       Unimon("Charizard", "Fuego", 153, 84, 78, 109, 85, 100, "Nada", 0,
              {"Lanzallamas", "TajoAéreo", "GarraDragón", "Llamarada", "AnilloÍgneo", "Sofoco", "GiroFuego", "AtaqueRápido"},
              ["images/pokemon/charizard_front.png",
              "images/pokemon/charizard_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Arcanine", "Fuego", 165, 110, 80, 100, 80, 95, "Nada", 0,
              {"EnviteÍgneo", "VelocidadExtrema", "Lanzallamas", "Rayo", "Triturar", "VoltioCruel", "ColmilloÍgneo", "Llamarada"},
              ["images/pokemon/arcanine_front.png",
              "images/pokemon/arcanine_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Flareon", "Fuego", 140, 130, 60, 95, 110, 65, "Nada", 0,
              {"EnviteÍgneo", "Lanzallamas", "Llamarada", "Mordisco", "Triturar", "CuerpoPesado", "PuñoFuego", "Sofoco"},
              ["images/pokemon/flareon_front.png",
              "images/pokemon/flareon_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Blastoise", "Agua", 154, 83, 100, 85, 105, 78, "Nada", 0,
              {"Surf", "Hidrobomba", "RayoHielo", "Cascada", "Hidrocañón", "Terremoto", "PistolaAgua", "Mordisco"},
              ["images/pokemon/blastoise_front.png",
              "images/pokemon/blastoise_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Gyarados", "Agua", 170, 125, 79, 60, 100, 81, "Nada", 0,
              {"Cascada", "Terremoto", "Hidrobomba", "GarraDragón", "Mordisco", "Triturar", "Ventisca", "Hiperrayo"},
              ["images/pokemon/gyarados_front.png",
              "images/pokemon/gyarados_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Lapras", "Agua", 205, 85, 80, 85, 95, 60, "Nada", 0,
              {"RayoHielo", "Surf", "Hidrobomba", "Psíquico", "Ventisca", "Rayo", "CuerpoPesado", "RayoBurbuja"},
              ["images/pokemon/lapras_front.png",
              "images/pokemon/lapras_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Vaporeon", "Agua", 205, 65, 60, 110, 95, 65, "Nada", 0,
              {"Surf", "Hidrobomba", "RayoHielo", "BolaSombra", "RayoBurbuja", "Ácido", "Mordisco", "Triataque"},
              ["images/pokemon/vaporeon_front.png",
              "images/pokemon/vaporeon_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Starmie", "Agua", 135, 75, 85, 100, 85, 115, "Nada", 0,
              {"Surf", "Psíquico", "RayoHielo", "Rayo", "Hidrobomba", "OndaTrueno", "BolaSombra", "GiroFuego"},
              ["images/pokemon/starmie_front.png",
              "images/pokemon/starmie_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Venusaur", "Planta", 155, 82, 83, 100, 100, 80, "Nada", 0,
              {"HojaAfilada", "RayoSolar", "BombaLodo", "Somnífero", "GigaDrenado", "PlantaFeroz", "LátigoCepa"},
              ["images/pokemon/venusaur_front.png",
              "images/pokemon/venusaur_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Raichu", "Eléctrico", 135, 90, 55, 90, 80, 110, "Nada", 0,
              {"Rayo", "Trueno", "VelocidadExtrema", "Surf", "OndaTrueno", "PuñoTrueno", "OndaVoltio", "Impactrueno"},
              ["images/pokemon/raichu_front.png",
              "images/pokemon/raichu_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Jolteon", "Eléctrico", 140, 65, 60, 110, 95, 130, "Nada", 0,
              {"Rayo", "Trueno", "BolaSombra", "BombaLodo", "OndaVoltio", "Chispazo", "OndaTrueno", "AtaqueRápido"},
              ["images/pokemon/jolteon_front.png",
              "images/pokemon/jolteon_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Alakazam", "Psíquico", 130, 50, 45, 135, 95, 120, "Nada", 0,
              {"Psíquico", "BolaSombra", "OndaTóxica", "Rayo", "RayoHielo", "Triataque", "OndaTrueno", "Psicocorte"},
              ["images/pokemon/alakazam_front.png",
              "images/pokemon/alakazam_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Machamp", "Lucha", 165, 130, 80, 65, 85, 55, "Nada", 0,
              {"ABocajarro", "Avalancha", "Terremoto", "PuñoTrueno", "PuñoFuego", "PuñoHielo", "Sumisión", "TajoCruzado"},
              ["images/pokemon/machamp_front.png",
              "images/pokemon/machamp_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Gengar", "Fantasma", 135, 65, 60, 130, 75, 110, "Nada", 0,
              {"BolaSombra", "BombaLodo", "Psíquico", "Rayo", "Trueno", "GigaDrenado", "OndaTóxica"},
              ["images/pokemon/gengar_front.png",
              "images/pokemon/gengar_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Nidoking", "Veneno", 156, 102, 77, 85, 75, 85, "Nada", 0,
              {"Terremoto", "BombaLodo", "Avalancha", "RayoHielo", "Rayo", "Llamarada", "PuyaNociva", "TierraViva"},
              ["images/pokemon/nidoking_front.png",
              "images/pokemon/nidoking_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Aerodactyl", "Roca", 155, 105, 65, 60, 75, 130, "Nada", 0,
              {"Avalancha", "TajoAéreo", "Terremoto", "ColmilloÍgneo", "GarraDragón", "RocaAfilada", "Triturar", "Mordisco"},
              ["images/pokemon/aerodactyl_front.png",
              "images/pokemon/aerodactyl_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Scyther", "Bicho", 145, 110, 80, 55, 80, 105, "Nada", 0,
              {"TijeraX", "TajoAéreo", "Hiperrayo", "GarraDragón", "AtaqueRápido", "Psicocorte", "CuerpoPesado", "Cascada"},
              ["images/pokemon/scyther_front.png",
              "images/pokemon/scyther_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Dragonite", "Dragon", 166, 134, 95, 100, 100, 80, "Nada", 0,
              {"GarraDragón", "VelocidadExtrema", "Lanzallamas", "RayoHielo", "Surf", "Trueno", "Terremoto", "Dragoaliento"},
              ["images/pokemon/dragonite_front.png",
              "images/pokemon/dragonite_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Snorlax", "Normal", 235, 110, 65, 65, 110, 30, "Nada", 0,
              {"CuerpoPesado", "Terremoto", "Hiperrayo", "Surf", "Lanzallamas", "Rayo", "PuñoHielo", "Triturar"},
              ["images/pokemon/snorlax_front.png",
              "images/pokemon/snorlax_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")

       Unimon("Chansey", "Normal", 325, 5, 5, 35, 105, 50, "Nada", 0,
              {"Tóxico", "RayoHielo", "Psíquico", "Rayo", "BombaLodo", "Triataque", "Llamarada"},
              ["images/pokemon/chansey_front.png",
              "images/pokemon/chansey_back.png"],
              Main.ancho * 3/12, Main.altura * 9/12, 500, 500,
              "main")
