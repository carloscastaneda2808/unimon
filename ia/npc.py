"""
Archivo para el NPC
"""

from random import sample, choice, randint

from clase.clase_main import Main
from clase.cadena import Cadena

from pokedex.unimon import Unimon
from pokedex.habilidad import Habilidad

class NPC:
    def elegir_equipo():
        cantidad = len(Main.unimones[Cadena.usuario])

        Main.crear_diccionario(Main.unimones, Cadena.NPC)
        Main.unimones[Cadena.NPC] = dict(sample(list(Main.unimones[Cadena.main].items()), cantidad))

        for unimon in Main.unimones[Cadena.NPC].values():
            unimon.cambiar_front()

    def elegir_habilidades():
        cantidad = len(list(Main.unimones[Cadena.usuario].values())[0].hb)

        Main.crear_diccionario(Main.habilidades, Cadena.NPC)
        for unimon in Main.unimones[Cadena.NPC].values():
            unimon.hb.update(sample(list(unimon.hb_posibles), cantidad))

            for habilidad in unimon.hb:
                Habilidad.copiar_habilidad(Cadena.NPC, Cadena.main, habilidad)

    def sacar_unimon():
        if Main.unimon_npc:
            Unimon.eliminar_unimon_ventana(Main.unimon_npc, Cadena.main, Cadena.combate, Cadena.NPC)

        Main.unimon_npc = choice(
            [x for x in Main.unimones[Cadena.NPC].keys()
            if x != Main.unimon_npc]
        )
        unimon_npc = Main.unimones[Cadena.NPC][Main.unimon_npc]

        # Visual unimon
        Main.ventanas[Cadena.main][Cadena.combate].crear_dic_elementos(Cadena.NPC, None, None, None)
        Unimon.unimon_ventana(Cadena.NPC, Main.unimon_npc, Cadena.main, Cadena.combate, Cadena.NPC)

        # Visual texto
        Main.textos[Cadena.main][Cadena.unimon_npc].cambiar_texto(Main.unimon_npc)

        # Visual barra de vida
        texto_npc = Main.textos[Cadena.main][Cadena.hp_npc]
        texto_npc.ancho = texto_npc.ancho_max * unimon_npc.hp / unimon_npc.hp_max
        texto_npc.cambiar_medidas(texto_npc.ancho, texto_npc.alto)

        # Visual estado
        if unimon_npc.estado != Cadena.Nada:
            Main.textos[Cadena.main][Cadena.estado_npc].cambiar_texto(unimon_npc.estado)
            
        else:
            Main.textos[Cadena.main][Cadena.estado_npc].cambiar_texto("")

        # Visual numero hp
        Main.textos[Cadena.main][Cadena.numero_hp_npc].cambiar_texto(f"{unimon_npc.hp}")

    def elegir_movimiento():
        Main.movimiento_npc = choice(list(Main.unimones[Cadena.NPC][Main.unimon_npc].hb))

    def elegir_turno():
        unimon = Main.unimones[Cadena.NPC][Main.unimon_npc]

        if len(Main.unimones[Cadena.NPC]) > 1:
            acc = 10
            if unimon.hp < (unimon.hp_max / 4):
                acc += 10

            if acc >= randint(1, 100):
                NPC.sacar_unimon()
                
            else:
                NPC.elegir_movimiento()

        else:
            NPC.elegir_movimiento()

        