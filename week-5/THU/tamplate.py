class Weapon:
    def strike(self, warrior, opponent):
        opponent.hp -= self.damage()
        warrior.hp -= self.self_infect()
    def damage(self):
        raise "Not implemented"
    def self_infect(self):
        raise "Not implemented"
class Sword(Weapon):
    def damage(self):
        return 15
    def self_infect(self):
        return 10
class Bow(Weapon):
    def damage(self):
        return 10
    def self_infect(self):
        return 5

class Enchanced(Weapon):
    def __init__(self, alma):
        self.alma = alma
    def damage(self):
        return self.alma.damage() * 2
    def self_infect(self):
        return self.alma.self_infect() / 2

class Warrior:
    def __init__(self, weapon, hp):
        self.weapon = weapon
        self.hp = hp
    def strike(self, opponent):
        self.weapon.strike(self, opponent)
    def __repr__(self):
        return "Warrior hp= {}".format(self.hp)

warrior = Warrior(Enchanced(Sword()), 100)
opponent = Warrior(Bow(), 100)

warrior.strike(opponent)
print(warrior)
print(opponent)

opponent.strike(warrior)
print(warrior)
print(opponent)
