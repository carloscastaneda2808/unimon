"""
Archivo para los estados
"""

from random import randint

from settings.cadena import Cadena

class Estado:
    def estado_antes(unimon):
        if unimon.estado == Cadena.Dormido:
            Estado.dormido(unimon)

        elif unimon.estado == Cadena.Congelado:
            Estado.congelado(unimon)

    def estado_danio(unimon):
        if unimon.estado == Cadena.Quemado:
            Estado.quemado(unimon)

        elif unimon.estado == Cadena.Envenenado:
            Estado.envenenado(unimon)

        elif unimon.estado == Cadena.GravementeEnvenenado:
            Estado.gravemente_envenenado(unimon)

    # aplica el estado de sueño con duracion variable y probabilidad de despertar
    # modifique esta funcion porque en el pokemon el estado dormido dura entre 1 o 3 turno
    # y eso se elige al principio, no cada turno
    def dormido(unimon):

        # se usan numeros negativos para no confundir con duracion de gravemente envenenado
        if unimon.estado_duracion == 0:
            unimon.estado_duracion = randint(1, 3)

        else:
            unimon.estado_duracion -= 1

            if unimon.estado_duracion == 0:
                unimon.estado = Cadena.Nada

    def congelado(unimon):

        if 20 >= randint(1, 100):
            unimon.estado = Cadena.Nada

    def paralizado(unimon):

        if unimon.estado == Cadena.Paralizado:
            return 12 >= randint(1, 100)
        
    def paralizado_speed(unimon):

        if unimon.estado == Cadena.Paralizado:
            unimon.spe = unimon.spe_max / 2

    def quemado(unimon):
        unimon.restar_hp(unimon.hp_max / 16)

    def quemado_atk_fisico(unimon):

        if unimon.estado == Cadena.Quemado:
            unimon.atk_fisico = unimon.atk_fisico_max / 2

    def envenenado(unimon):
        unimon.restar_hp(unimon.hp_max / 6)

    def gravemente_envenenado(unimon):

        if unimon.estado_duracion == 0:
            unimon.estado_duracion = 1

        unimon.restar_hp(unimon.estado_duracion * unimon.hp_max / 16)
        unimon.estado_duracion += 1
