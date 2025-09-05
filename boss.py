from enemy import Enemy
import random

class RedGoblin(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = 30


    def GrimDemise(self):
        if self.health < 50:
            self.attack_power += 20
        return self.attack_power