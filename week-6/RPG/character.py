class Character:
    def __init__(self, name = 'player1', hp = 0, dexterity = 0, luck = 0,  ):
        self.name = name
        self.hp = hp
        self.dexterity = dexterity
        self.luck = luck

    def __repr__(self):
        return 'name: {}, hp: {}, dexterity: {}, luck: {}'.format(self.name, self.hp, self.dexterity, self.luck)
    #
    # def get_hp(self):
    #     pass
    #
    # def get_dexterity(self):
    #     pass
    #
    # def luck(self):
    #     pass

    # def strike(self, opponent):
    #     opponent.hp -= self.damage
    #
    # def roll_status(self):
    #     pass

# class Monster(Character):
#     pass

# class Player(character):
#     def __init__(self):



# class Inventory(character):
#     def __init__(self):
#         pass

    # def weapon(self, type?):
    #     pass
    #
    # def armor(self, ):
    #     pass
    #
    # def potinon(self):



# Then it should print the whole character stats:
# Dexterity
# Strength
# Luck
# Inventory:
# Sword
# Leather Armor
# Selected potion
