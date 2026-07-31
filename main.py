class player: # Creating Player class for game
    name = ""
    health = 10
    inventory = {
        "Health Potions" : 3
    }
    level = 1
    damage = level * 0.5 # Calculates Damage Based on Level

    def __init__(self, name): # Initi method for creating player object
        self.name = name

    def view_stats(self): # Method to view current Player stats
        print("Name", self.name)
        print("Health", self.health)
        print("----Inventory----")
        for x, y in self.inventory.items(): # Loops throuhg inventory (dict)
            print(y,"x", x)
        print("------------------")
        print("Level", self.level)
        print("Damage", self.damage)

player_1 = player("Ava")

player_1.view_stats()
