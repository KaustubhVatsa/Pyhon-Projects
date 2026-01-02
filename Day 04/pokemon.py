#class to initalize pokemon 
class Pokemon :
   def __init__(self , name , base_stats , attacks):
      self.name = name
      self.max_hp=base_stats['hp']
      self.phys_atk = base_stats['phys_atk']
      self.mag_atk = base_stats['mag_atk']
      self.speed = base_stats['speed']
      self.phys_def = base_stats['phys_def']
      self.mag_def = base_stats['mag_def']
      self.dodge = base_stats['dodge']
      self.total_base_stat = self.phys_atk + self.mag_atk + self.speed + self.phys_def + self.mag_def + self.dodge + self.max_hp
      self.current_hp = self.max_hp
      self.attack = attacks

   def __str__(self):
      attacks = ", ".join(a.name for a in getattr(self, "attack", []))
      return (f"{self.name} | HP: {self.current_hp}/{self.max_hp} | phys_atk: {self.phys_atk} | "
            f"mag_atk: {self.mag_atk} | phys_def: {self.phys_def} | mag_def: {self.mag_def} | "
            f"speed: {self.speed} | dodge: {self.dodge} | total: {self.total_base_stat} | "
            f"attacks: [{attacks}]")