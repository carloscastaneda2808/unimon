"""
Archivo para funciones extra de interfaz grafica
"""

import pygame
from funciones_graficas.boton import Boton

def unimon_enumerar(unimones, ancho, letras_unimones, negro, azul):
    unimones_dic = {}

    unimon_por_filas = 5
    espacio = ancho / (unimon_por_filas + 1)

    for i, unimon in enumerate(unimones):

        columna = i % unimon_por_filas
        fila = i // unimon_por_filas

        x = espacio * (columna + 1)
        y = 300 + fila * 100

        unimones_dic[f"unimon{i}"] = Boton(letras_unimones, unimon.nombre, negro, (x, y), (180, 60), azul)

    return unimones_dic