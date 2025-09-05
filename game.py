import random
from goblin import Goblin
from hero import Hero
from boss import RedGoblin

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero

    hero = Hero("eragon the dragon rider")


    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.attack()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.take_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    if hero.is_alive() and defeated_goblins == len(goblins):
        hero.gain_health(50)
        print("the boss has smelt the dead of his minions and has entered the battle feild")
        boss = RedGoblin("Red Goblin Boss")
        while hero.is_alive() and boss.is_alive():
            print("\nBoss Battle Round!")
            
            # Hero's turn to attack
            damage = hero.attack()
            print(f"Hero attacks {boss.name} for {damage} damage!")
            boss.take_damage(damage)

            # Check if the boss was defeated
            if not boss.is_alive():
                print(f"{boss.name} has been defeated! The hero is victorious! ༼ ᕤ◕◡◕ ༽ᕤ")
                break

            # Boss's turn to attack
            damage = boss.attack()
            print(f"{boss.name} attacks hero for {damage} damage!")
            hero.take_damage(damage)

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
