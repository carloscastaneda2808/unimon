"""
Archivo para el NPC
"""

from random import sample, choice, randint

from clase_main import Main
from pokedex.unimon import Unimon

class NPC:
    def elegir_equipo():
        cantidad = len(Main.unimones["usuario"])

        Main.crear_diccionario(Main.unimones, "NPC")
        Main.unimones["NPC"] = dict(sample(list(Main.unimones["main"].items()), cantidad))

        for unimon in Main.unimones["NPC"].values():
            unimon.cambiar_front()

    def elegir_habilidades():
        cantidad = len(list(Main.unimones["usuario"].values())[0].hb)

        for unimon in Main.unimones["NPC"].values():
            unimon.hb.update(sample(list(unimon.hb_posibles), cantidad))

    def sacar_unimon():
        if Main.unimon_npc:
            Unimon.eliminar_unimon_ventana(Main.unimon_npc, "main", Main.vent_6, "b")

        Main.unimon_npc = choice(
            [x for x in Main.unimones["NPC"].keys()
            if x != Main.unimon_npc]
        )

        Unimon.unimon_ventana("NPC", Main.unimon_npc, "main", Main.vent_6, "b")

    def elegir_movimiento():
        Main.movimiento_npc = choice(list(Main.unimones["NPC"][Main.unimon_npc].hb))

    def elegir_turno():
        unimon = Main.unimones["NPC"][Main.unimon_npc]

        acc = 10
        if unimon.hp < (unimon.hp_max / 4):
            acc += 10

        if acc >= randint(1, 100):
            NPC.sacar_unimon()

        else:
            NPC.elegir_movimiento()

        