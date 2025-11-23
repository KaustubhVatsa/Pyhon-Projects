from attack import Attack
from pokemon import Pokemon

RAW_ATTACKS = {
    'Tackle':       {'type': 'physical', 'base_damage': 15, 'accuracy': 95, 'debuff': None},
    'Thunderbolt':  {'type': 'magical',  'base_damage': 25, 'accuracy': 90, 'debuff': {'speed': 0.8}},
    'Flamethrower': {'type': 'magical',  'base_damage': 30, 'accuracy': 85, 'debuff': None},
    'Vine Whip':    {'type': 'physical', 'base_damage': 20, 'accuracy': 100,'debuff': {'defense_phys': 0.9}},
    'Water Gun':    {'type': 'magical',  'base_damage': 18, 'accuracy': 100,'debuff': None},
    'Earthquake':   {'type': 'physical', 'base_damage': 35, 'accuracy': 80, 'debuff': {'speed': 0.7}},
    'Ice Beam':     {'type': 'magical',  'base_damage': 28, 'accuracy': 90, 'debuff': {'dodge': 0.5}},
    'Peck':         {'type': 'physical', 'base_damage': 12, 'accuracy': 100,'debuff': None},
    'Psychic':      {'type': 'magical',  'base_damage': 32, 'accuracy': 85, 'debuff': {'defense_mag': 0.8}},
    'Body Slam':    {'type': 'physical', 'base_damage': 25, 'accuracy': 90, 'debuff': {'attack_phys': 0.9}},
    'Bubble':       {'type': 'magical',  'base_damage': 15, 'accuracy': 100,'debuff': {'speed': 0.85}},
    'Rock Throw':   {'type': 'physical', 'base_damage': 22, 'accuracy': 80, 'debuff': None},
    'Shadow Ball':  {'type': 'magical',  'base_damage': 27, 'accuracy': 90, 'debuff': {'defense_mag': 0.85}},
    'Quick Attack': {'type': 'physical', 'base_damage': 10, 'accuracy': 100,'debuff': None},
    'Fire Punch':   {'type': 'physical', 'base_damage': 20, 'accuracy': 95, 'debuff': {'defense_phys': 0.9}},
    'Thunder Wave': {'type': 'magical',  'base_damage': 0,  'accuracy': 90, 'debuff': {'speed': 0.5}},
    'Razor Leaf':   {'type': 'physical', 'base_damage': 24, 'accuracy': 85, 'debuff': None},
    'Dragon Breath':{'type': 'magical',  'base_damage': 30, 'accuracy': 80, 'debuff': {'dodge': 0.7}},
    'Bone Club':    {'type': 'physical', 'base_damage': 25, 'accuracy': 85, 'debuff': {'defense_phys': 0.85}},
}

ATTACKS = {name: Attack(name, data['type'], data['base_damage'], data['accuracy'])
           for name, data in RAW_ATTACKS.items()}

RAW_POKEMON = {
'Pikachu': {
'hp': 60, 'phys_atk': 40, 'mag_atk': 70, 'phys_def': 30, 'mag_def': 50, 'speed': 90, 'dodge': 15,
'attacks': ['Tackle', 'Thunderbolt', 'Quick Attack', 'Thunder Wave']
},
'Charmander': {
'hp': 65, 'phys_atk': 50, 'mag_atk': 60, 'phys_def': 40, 'mag_def': 45, 'speed': 70, 'dodge': 10,
'attacks': ['Tackle', 'Flamethrower', 'Fire Punch', 'Quick Attack']
},
'Squirtle': {
'hp': 75, 'phys_atk': 45, 'mag_atk': 55, 'phys_def': 60, 'mag_def': 65, 'speed': 50, 'dodge': 5,
'attacks': ['Water Gun', 'Bubble', 'Tackle', 'Ice Beam']
},
'Bulbasaur': {
'hp': 70, 'phys_atk': 55, 'mag_atk': 50, 'phys_def': 50, 'mag_def': 55, 'speed': 60, 'dodge': 10,
'attacks': ['Vine Whip', 'Razor Leaf', 'Tackle', 'Earthquake']
},
'Snorlax': {
'hp': 100, 'phys_atk': 70, 'mag_atk': 30, 'phys_def': 80, 'mag_def': 40, 'speed': 20, 'dodge': 5,
'attacks': ['Body Slam', 'Earthquake', 'Tackle', 'Peck']
},
'Jigglypuff': {
'hp': 55, 'phys_atk': 30, 'mag_atk': 65, 'phys_def': 25, 'mag_def': 45, 'speed': 80, 'dodge': 20,
'attacks': ['Peck', 'Bubble', 'Psychic', 'Shadow Ball']
},
'Meowth': {
'hp': 50, 'phys_atk': 60, 'mag_atk': 40, 'phys_def': 35, 'mag_def': 30, 'speed': 85, 'dodge': 25,
'attacks': ['Quick Attack', 'Peck', 'Rock Throw', 'Tackle']
},
'Psyduck': {
'hp': 60, 'phys_atk': 40, 'mag_atk': 70, 'phys_def': 30, 'mag_def': 60, 'speed': 65, 'dodge': 15,
'attacks': ['Water Gun', 'Psychic', 'Bubble', 'Ice Beam']
},
'Machop': {
'hp': 80, 'phys_atk': 75, 'mag_atk': 25, 'phys_def': 55, 'mag_def': 25, 'speed': 45, 'dodge': 5,
'attacks': ['Tackle', 'Earthquake', 'Rock Throw', 'Body Slam']
},
'Abra': {
'hp': 45, 'phys_atk': 20, 'mag_atk': 85, 'phys_def': 20, 'mag_def': 50, 'speed': 95, 'dodge': 20,
'attacks': ['Psychic', 'Shadow Ball', 'Thunderbolt', 'Quick Attack']
},
'Geodude': {
'hp': 85, 'phys_atk': 65, 'mag_atk': 20, 'phys_def': 90, 'mag_def': 20, 'speed': 15, 'dodge': 0,
'attacks': ['Rock Throw', 'Earthquake', 'Tackle', 'Body Slam']
},
'Ponyta': {
'hp': 70, 'phys_atk': 50, 'mag_atk': 60, 'phys_def': 45, 'mag_def': 50, 'speed': 75, 'dodge': 15,
'attacks': ['Flamethrower', 'Fire Punch', 'Quick Attack', 'Peck']
},
'Slowpoke': {
'hp': 90, 'phys_atk': 35, 'mag_atk': 60, 'phys_def': 50, 'mag_def': 70, 'speed': 25, 'dodge': 5,
'attacks': ['Water Gun', 'Psychic', 'Bubble', 'Thunder Wave']
},
'Drowzee': {
'hp': 65, 'phys_atk': 40, 'mag_atk': 65, 'phys_def': 40, 'mag_def': 55, 'speed': 55, 'dodge': 10,
'attacks': ['Psychic', 'Shadow Ball', 'Peck', 'Body Slam']
},
'Krabby': {
'hp': 75, 'phys_atk': 70, 'mag_atk': 30, 'phys_def': 65, 'mag_def': 30, 'speed': 50, 'dodge': 10,
'attacks': ['Bubble', 'Vine Whip', 'Rock Throw', 'Tackle']
},
'Voltorb': {
'hp': 50, 'phys_atk': 30, 'mag_atk': 70, 'phys_def': 25, 'mag_def': 45, 'speed': 90, 'dodge': 25,
'attacks': ['Thunderbolt', 'Thunder Wave', 'Quick Attack', 'Tackle']
},
'Exeggcute': {
'hp': 80, 'phys_atk': 45, 'mag_atk': 60, 'phys_def': 50, 'mag_def': 65, 'speed': 40, 'dodge': 5,
'attacks': ['Vine Whip', 'Psychic', 'Shadow Ball', 'Earthquake']
},
'Cubone': {
'hp': 70, 'phys_atk': 65, 'mag_atk': 35, 'phys_def': 55, 'mag_def': 35, 'speed': 60, 'dodge': 10,
'attacks': ['Bone Club', 'Earthquake', 'Rock Throw', 'Peck']
}
}

POKEMON_DATA = RAW_POKEMON

# Helpers 

#List all pokemons
def get_pokemon_names():
    return list(POKEMON_DATA.keys())

#Get a pokemon by name
def get_pokemon(name):
    if name not in POKEMON_DATA:
        return None
    stats = POKEMON_DATA[name]
    attack_objs = [ATTACKS[a_name] for a_name in stats['attacks']]
    return Pokemon(name, stats, attack_objs)

#get all atttacks 
def get_attack(name):
    return ATTACKS.get(name)

#Get all attacks
def get_attack_names():
    return list(ATTACKS.keys())


