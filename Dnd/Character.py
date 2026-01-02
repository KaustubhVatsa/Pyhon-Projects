class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def attack(self):
        raise NotImplementedError("Implemented by child class")

    def is_Alive(self):
        return self.hp > 0


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 125

    def attack(self):
        return 20


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 80

    def attack(self):
        return 40


if __name__ == "__main__":
    hero = Mage("KV")
    print(f"{hero.name} \n,{hero.hp}\n ")
