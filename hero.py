import random

class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    def __init__(self, name):
        self.name = name
        self.health = 160
        self.attack_power = random.randint(10, 20)

    def attack(self):
        return random.randint(self.attack_power, self.attack_power + 10)
    def gain_health(self, amount):
        self.health += amount
        print(f"{self.name} gains {amount} health. Health is now {self.health}.")

    def take_damage(self, damage):
        self.health -= damage
        # TODO We should prevent the goblins health from going into the NEGATIVE
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False