'''
Archivo para el combate
'''

# sirve para ataques solo de daño
def restar_hp(habilidad, unimon_atacante, unimon_atacado):
    unimon_atacado.hp -= (unimon_atacante.habilidades[habilidad] * unimon_atacante.atk / unimon_atacado.df) // 2 + 2

# verifica si el unimon esta debilitado
def verificar_hp(unimon):
    return unimon.hp <= 0