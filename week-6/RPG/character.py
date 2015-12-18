class Character:
    def __init__(self, name = 'monster', hp = 0, hp_max = 0, dexterity = 0, luck = 0, luck_max = 0, roll = 0 ):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.dexterity = dexterity
        self.luck = luck
        self.luck_max = luck_max
        
        self.roll = roll

    def __repr__(self):
        return 'name: {}, max_hp/hp: {}/{}, dexterity: {}, max_luck/luck: {}/{}'.format(self.name, self.hp_max, self.hp, self.dexterity, self.luck_max, self.luck)


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
