#Defines the attack class for the game
#Each attack has a name , base power, type :physical or magical , accuracy , debuffs 

import random


class Attack:
   def __init__(self , name , type , base_damage , accuracy , debuff=None):
      self.name = name
      self.type = type
      self.base_damage = base_damage
      self.accuracy = accuracy
      self.debuff = debuff

   def __str__(self):
      debuff_str = f"(debuff : {self.debuff})" if self.debuff else ""
      return f"{self.name}({self.type}) - damage : {self.base_damage} debuff : {debuff_str}"
   
   def calculate_damage(self , attacker , defender):
      if self.type == 'physical':
         atk  = attacker.get_effective_stat('phys_atk')
         def_ = defender.get_effective_stat('phys_def')
      else:
         atk  = attacker.get_effective_stat('mag_atk')
         def_ = defender.get_effective_stat('mag_def')
      damaage =max(1 , atk - def_ + self.base_damage)
      return damaage
   

#Roll a die (1-100) for this attack attempt.
# 2. Calculate effective success rate: Attack's accuracy, discounted by defender's evasion.
# 3. If die <= success rate: Attack connects (proceed to damage/debuff).
#    Else: Miss (no effect, turn ends or passes).
   def will_hit(self , attacker , defender):
      roll = random.randint(1 , 100)
      hit_chance = self.accuracy *(1 - defender.get_effective_stat('dodge')/100)
      return roll <= hit_chance
   
   def apply_debuff(self ,target):
      #TODO : Iteration 2
      pass 
