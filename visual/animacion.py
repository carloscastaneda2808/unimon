"""
Archivo para las animacion
"""

from clase.clase_main import Main
from clase.cadena import Cadena

from pokedex.habilidad import Habilidad

class Animacion:
    def animacion_habilidad(habilidad, jugador, primero):
        value = Main.habilidades[jugador][habilidad]
        Main.timer_termina += 60

        if primero:
            value.usando_timer = True
            value.empieza = Main.timer_termina - 60
            value.termina = Main.timer_termina
        else:
            value.usando_timer = True
            value.empieza = Main.timer_termina - 60
            value.termina = Main.timer_termina

        if jugador == Cadena.usuario:
            value.cambiar_front()
        else:
            value.cambiar_back()

        Habilidad.limpiar_habilidad_ventana(Cadena.main, Cadena.combate, jugador)
        Habilidad.habilidad_ventana(jugador, habilidad, Cadena.main, Cadena.combate, jugador)

    def animacion_barra_hp(unimon_usr, unimon_npc):
        texto_usr = Main.textos[Cadena.main][Cadena.hp_usr]
        texto_npc = Main.textos[Cadena.main][Cadena.hp_npc]

        Main.timer_termina += 60

        texto_usr.usando_timer = True
        texto_usr.empieza = Main.timer_termina - 60
        texto_usr.termina = Main.timer_termina

        texto_npc.usando_timer = True
        texto_npc.empieza = Main.timer_termina - 60
        texto_npc.termina = Main.timer_termina

        # Inicia el timer
        Main.timer = 1

        texto_usr.ancho_nuevo = texto_usr.ancho_max * unimon_usr.hp / unimon_usr.hp_max
        texto_npc.ancho_nuevo = texto_npc.ancho_max * unimon_npc.hp / unimon_npc.hp_max

    def animacion_debilitado(unimon_usr, unimon_npc):
        animacion = False

        if not unimon_usr.verificar_hp():
            Main.timer = 1
            unimon_usr.usando_timer = True
            animacion = True

        if not unimon_npc.verificar_hp():
            Main.timer = 1
            unimon_npc.usando_timer = True
            animacion = True

        if animacion:
            Main.timer_termina += 60
            unimon_usr.empieza = Main.timer_termina - 60
            unimon_usr.termina = Main.timer_termina
            unimon_npc.empieza = Main.timer_termina - 60
            unimon_npc.termina = Main.timer_termina

    def animacion_estado(unimon_usr, unimon_npc):
        if unimon_usr.estado != Cadena.Nada:
            Main.textos[Cadena.main][Cadena.estado_usr].cambiar_texto(unimon_usr.estado)
        else:
            Main.textos[Cadena.main][Cadena.estado_usr].cambiar_texto("")

        if unimon_npc.estado != Cadena.Nada:
            Main.textos[Cadena.main][Cadena.estado_npc].cambiar_texto(unimon_npc.estado)

        else:
            Main.textos[Cadena.main][Cadena.estado_npc].cambiar_texto("")

    def animacion_numero_hp(unimon_usr, unimon_npc):
        Main.textos[Cadena.main][Cadena.numero_hp_usr].cambiar_texto(f"{unimon_usr.hp}")
        Main.textos[Cadena.main][Cadena.numero_hp_npc].cambiar_texto(f"{unimon_npc.hp}")
