import random


class Pokemon(object):
    def __init__(self, name, health_points, attack_power_upper_range, attack_power_lower_range):
        self.name = name
        self.health_points = health_points
        self.attack_power_lower_range = attack_power_lower_range
        self.attack_power_upper_range = attack_power_upper_range

    def attack(self):
        return random.randint(self.attack_power_lower_range, self.attack_power_upper_range)

    def defend(self, enemy, attack_power):
        self.health_points -= attack_power

    def growl(self):
        print("Growl")


class WaterType(Pokemon):
    pass

    def growl(self):
        print("Splish Splosh")

    def attack(self, enemy):
        if isinstance(enemy, FireType):
            return "Less effective"
        elif isinstance(enemy,GlassType):
            return "More Effective"
        else:
            return "No effect"


class FireType(Pokemon):
    pass

    def growl(self):
        print("Fire Fire")

    def attack(self, enemy):
        if isinstance(enemy, WaterType):
            return "Less effective"
        elif isinstance(enemy, GlassType):
            return "More Effective"
        else:
            return "No effect"


class GlassType(Pokemon):
    pass

    def growl(self):
        print('Cheep Cheep')

    def attack(self, enemy):
        if isinstance(enemy, FireType):
            return "Less effective"
        elif isinstance(enemy, WaterType):
            return "More Effective"
        else:
            return "No effect"


watertype1 = WaterType('Name1', 100, 50, 25)
firetype1 = FireType('Name2', 100, 50, 50)
glasstype1 = GlassType('Name3', 100, 75, 25)


print(watertype1.attack(watertype1))
print(glasstype1.attack(watertype1))
print(firetype1.attack(glasstype1))


watertype1.growl()
firetype1.growl()
glasstype1.growl()

# I got help from my dad on this assignment.
# He helped me to change the meanings of the methods in each individual subclass.
