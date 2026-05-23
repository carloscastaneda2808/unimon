"""
Archivo para leer y escribir archivos
"""

from clase.clase_main import Main

class Archivo:
    def leer_historial():
        Main.historial = []

        with open("resources/historial.txt", "r", encoding = "utf-8") as file:
            lineas = file.readlines()

            for linea in lineas:

                if linea.strip() != "" and not linea.startswith("#"):
                    Main.historial.append(linea.strip())

        # Lo siguiente se hace para que se puede escribir en los textos del diccionario estadisticas
        while len(Main.historial) < 8:
            Main.historial.append("")

        if len(Main.historial) > 8:
            Main.historial = Main.historial[-8:]

    def escribir_historial():

        with open("resources/historial.txt", "a") as file:
            if Main.historial_nuevo != "":
                file.write(Main.historial_nuevo + "\n")

    def borrar_historial():

        with open("resources/historial.txt", "w") as file:
            pass