
#battle logic for the game
import random

def attack_damage(attacker, defender, move):
   #pass attacking pokemon , defending pokemon and attacks
   #calculate attack damage
   #get move details 
   if will_hit(attacker , defender , move):
      move = attacker.attack[move]
      base_damage = move.base_damage
      type_of_attack = move.type
      if(type_of_attack == 'physical'):
         damage_of_attack = base_damage + attacker.phys_atk
         damage = max(1 , damage_of_attack - defender.phys_def)
      else:
         damage_of_attack = base_damage + attacker.mag_atk
         damage = max(1 , damage_of_attack - defender.mag_def)
      return damage
   
#check if attack hits
def will_hit(attacker , defender , move):
   move = attacker.attack[move]
   accuracy = move.accuracy
   roll = random.randint(1 , 100)
   hit_chance = accuracy *(1 - defender.dodge/100)
   return roll <= hit_chance

 
#reduce hp of opponent by attack damage
def reduce_hp(defender, damage):
   defender.current_hp -= damage
   defender.current_hp = max(0, defender.current_hp) # Prevent negative HP
   return check_faint(defender)

#check if opponent has fainted
def check_faint(defender):
   if defender.current_hp <= 0:
      print(f"{defender.name} has fainted!")
      return True
   return False