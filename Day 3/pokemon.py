from attack import Attack

class Pokemon: 
   def __init__(self , name , base_stats , attacks):
      self.name = name
      self.max_hp = base_stats['hp']
      self.current_hp = self.max_hp
      self.phys_atk = base_stats['phys_atk']
      self.mag_atk = base_stats['mag_atk']
      self.speed = base_stats['speed']
      self.phys_def = base_stats['phys_def']
      self.mag_def = base_stats['mag_def']
      self.dodge = base_stats['dodge']
      self.total_base_stat = self.phys_atk + self.mag_atk + self.speed + self.phys_def + self.mag_def + self.dodge + self.max_hp
      #modifiers for calculating debuffs 
      self.modifiers = {
         'phys_atk':1.0,
         'mag_atk':1.0,
         'speed':1.0,
         'phys_def':1.0,
         'mag_def':1.0,
         'dodge':1.0
      }
      self.attack = attacks
   
   def __str__(self):
      #display name , hp , key_stats 
      return f"{self.name} total_base_stats :{self.total_base_stat} \nHP :{self.current_hp}/{self.max_hp}\n Attack : {self.phys_atk} Physical Attack {self.mag_atk} Magical Attack\n Defense : {self.phys_def} Physical Defense {self.mag_def} Magical Defense \nDodge : {self.dodge} \nSpeed : {self.speed}"
      
   def isFainted(self):
      return self.current_hp <= 0
   def get_effective_stat(self, stat):
        # Returns effective value for stat (base * mod for Iteration 2).
        # Why? Call everywhere (damage, speed)—abstracts debuffs.
        base = getattr(self, stat)  # Dynamic: self.speed, etc.
        # mod = self.modifiers.get(stat, 1.0)  # Skipped: Always base for now.
        # return int(base * mod)
        return base  # Iteration 1: Pure base (debuffs disabled).

   def take_damage(self, amount):
        # Reduces HP, clamps to 0. Returns new HP.
        # Why? Encapsulates—no direct HP access elsewhere.
        self.current_hp = max(0, self.current_hp - amount)
        return self.current_hp

   def heal(self, amount):
        # Heals up to max (future items).
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        return self.current_hp

   def reset_modifiers(self):
        # Resets modifiers to 1.0 (for switch/battle start).
        # Why? Clears debuffs later—harmless now.
        self.modifiers = {k: 1.0 for k in self.modifiers}  # Fresh dict.

   def get_attacks_display(self):
       # Numbered list for menus.
        return [f"{i+1}. {attack.name}" for i, attack in enumerate(self.attack)]
   
if __name__ == "__main__":
    from data import POKEMON_DATA
    pika = POKEMON_DATA['Pikachu']
    char = POKEMON_DATA['Charmander']
    
    attack = pika.attack[0]  # Tackle
    print(f"Damage calc: {attack.calculate_damage(pika, char)}")  # 40 - 40 + 15 = 15
    
    if attack.will_hit(pika, char):  # ~81% chance
        print("Hit!")
        char.take_damage(attack.calculate_damage(pika, char))
        print(f"Charmander HP: {char.current_hp}/65")  # e.g., 50/65
    else:
        print("Miss!")
    
    print("Attacks:", pika.get_attacks_display()[:2])  # ['1. Tackle', '2. Thunderbolt']
    pika.reset_modifiers()  # No effect yet.
    print(f"Pikachu speed (base): {pika.get_effective_stat('speed')}")  # 90 (ignores mod)