#attack class to handle and store attributes of attacks
class Attack:
   def __init__(self, name, type, base_damage, accuracy):
      self.name = name
      self.type = type
      self.base_damage = base_damage
      self.accuracy = accuracy

   def __str__(self):
      return f"{self.name}({self.type}) - damage : {self.base_damage} accuracy : {self.accuracy}"
   
   