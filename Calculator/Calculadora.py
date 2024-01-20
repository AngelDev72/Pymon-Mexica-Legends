def calcular_stats_base(base, nivel):
    stat_base = ((2 * base + 5) * nivel) // 100
    return stat_base

# Datos del Pymon
base_hp = 180
base_ataque = 90
base_defensa = 103
base_sp_attack = 105
base_sp_defense = 105
base_velocidad = 100

# Calcular y mostrar stats base para niveles del 5 al 100
for nivel in range(5, 105, 5):
    ataque = calcular_stats_base(base_ataque, nivel)
    defensa = calcular_stats_base(base_defensa, nivel)
    velocidad = calcular_stats_base(base_velocidad, nivel)
    sp_attack = calcular_stats_base(base_sp_attack, nivel)
    sp_defense = calcular_stats_base(base_sp_defense, nivel)
    hp = calcular_stats_base(base_hp, nivel)
    
    print(f"Nivel {nivel}: - HP: {hp} | Ataque: {ataque} | Defensa: {defensa} | Velocidad: {velocidad} | Sp. Ataque: {sp_attack} | Sp. Defensa: {sp_defense}")