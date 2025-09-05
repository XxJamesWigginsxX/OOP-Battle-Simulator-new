from enemy import Enemy

class BabyElf(Enemy):
    def cry():
        return ("Waaah! Waaah!")
    
    def take_damage(self, damage):
        print("Baby Elf cries loudly! Waaah! Waaah!")
        return super().take_damage(damage)

