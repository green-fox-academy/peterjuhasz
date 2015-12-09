class Sword:
    def demage(self):
        return 10

class Enhanced:
    def __init__(self, weapon):
        self.weapon = weapon
    def demage(self):
        return self.weapon.demage() + 5

class Magical:
    def __init__(self, weapon):
        self.weapon = weapon
    def demage(self):
        return self.weapon.demage() * 2

class Warrior:
    def __init__(self, weapon = Sword()):
        self.hp = 100
        self.weapon = weapon
    def strike(self, opponent):
        demage = self.weapon.demage()
        opponent.hp -= demage

warrior = Warrior(Enhanced(Sword()))
opponent = Warrior(Sword())

print(opponent.hp)
warrior.strike(opponent)
print(opponent.hp)
# --------------------------------------------------
class Bow:
    def demage(self):
        return 15

class explosive:
    def __init__(self, weapon):
        self.weapon = weapon.demage() + 20

class poison:
    def __init__(self, weapon):
        self.weapon = weapon.demage() * 2
