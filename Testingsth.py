RAW_ATTACKS = {
    'Tackle': {'type': 'physical', 'base_damage': 15, 'accuracy': 95, 'debuff': None},
    'Thunderbolt': {'type': 'magical', 'base_damage': 25, 'accuracy': 90, 'debuff': {'speed': 0.8}},
    'Flamethrower': {'type': 'magical', 'base_damage': 30, 'accuracy': 85, 'debuff': None},
    'Vine Whip': {'type': 'physical', 'base_damage': 20, 'accuracy': 100, 'debuff': {'defense_phys': 0.9}},  # Note: 'defense_phys' -> we'll map to 'phys_def' in use.
    'Water Gun': {'type': 'magical', 'base_damage': 18, 'accuracy': 100, 'debuff': None},
    'Earthquake': {'type': 'physical', 'base_damage': 35, 'accuracy': 80, 'debuff': {'speed': 0.7}},
    'Ice Beam': {'type': 'magical', 'base_damage': 28, 'accuracy': 90, 'debuff': {'dodge': 0.5}},
    'Peck': {'type': 'physical', 'base_damage': 12, 'accuracy': 100, 'debuff': None},
    'Psychic': {'type': 'magical', 'base_damage': 32, 'accuracy': 85, 'debuff': {'defense_mag': 0.8}},
    'Body Slam': {'type': 'physical', 'base_damage': 25, 'accuracy': 90, 'debuff': {'attack_phys': 0.9}},
    'Bubble': {'type': 'magical', 'base_damage': 15, 'accuracy': 100, 'debuff': {'speed': 0.85}},
    'Rock Throw': {'type': 'physical', 'base_damage': 22, 'accuracy': 80, 'debuff': None},
    'Shadow Ball': {'type': 'magical', 'base_damage': 27, 'accuracy': 90, 'debuff': {'defense_mag': 0.85}},
    'Quick Attack': {'type': 'physical', 'base_damage': 10, 'accuracy': 100, 'debuff': None},
    'Fire Punch': {'type': 'physical', 'base_damage': 20, 'accuracy': 95, 'debuff': {'defense_phys': 0.9}},
    'Thunder Wave': {'type': 'magical', 'base_damage': 0, 'accuracy': 90, 'debuff': {'speed': 0.5}},
    'Razor Leaf': {'type': 'physical', 'base_damage': 24, 'accuracy': 85, 'debuff': None},
    'Dragon Breath': {'type': 'magical', 'base_damage': 30, 'accuracy': 80, 'debuff': {'dodge': 0.7}},
    # Added 'Bone Club' for Cubone.
    'Bone Club': {'type': 'physical', 'base_damage': 25, 'accuracy': 85, 'debuff': {'defense_phys': 0.85}},
}

for name, data in RAW_ATTACKS.items():
   print (name)
   print (data['type'])
   print (data['base_damage'])
   print (data['accuracy'])
   print (data['debuff'])
   print ("\n")