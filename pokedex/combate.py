'''
Archivo para el combate
'''

# sirve para ataques de danio solo y escribe un mensaje
def restar_hp(mensaje, habilidad, unimon_atacante, unimon_atacado):
    danio = (habilidad.poder * unimon_atacante.atk / unimon_atacado.df) // 4 + 2
    print(f"\nEl {unimon_atacante} de {mensaje} utilizo {habilidad} haciendo {danio} de danio")

    unimon_atacado.hp -= danio

# verifica si el unimon esta debilitado y escribe un mensaje, falta poner una variable mensaje como un restar_hp
def verificar_hp(unimon):
    if unimon.hp < 0:
        hp = 0
    else:
        hp = unimon.hp

    print(f"{unimon.nombre} tiene {hp} puntos de HP")
    return unimon.hp <= 0