
text_break = ("-----------------------") # Line break var for UI readability
class player: # Creating Player class for game
    name = ""
    health = 10
    inventory = {
        "Health Potions" : 3,
        "Sword" : 1
    }
    level = 1
    damage = level * 0.5 # Calculates Damage Based on Level

    def __init__(self, name): # Init method for creating player object
        self.name = name

    def view_stats(self): # Method to view current Player stats
        print("Name -", self.name)
        print("Health -", self.health)
        print("Level -", self.level)
        print("Damage -", self.damage)

    def open_inventory(self):#Method to open the players inventory
        print("----Inventory----")
        z = 1
        for x, y in self.inventory.items(): # Loops through inventory (dict)
            print(z, x,"x", y)
            z += 1

        print(text_break)
        print("What would you like to do?")
        print("1. Use Item")
        print("2. Close inventory")
        user_input = input(">")

        match user_input:
            case "1":
                print(text_break)
                print("What item would you like to use?")
                user_input = input(">")
                try:
                    user_input = int(user_input)
                    no_items = len(self.inventory) # Gets the length of the player inventory
                    if user_input >0 and user_input <= no_items: # Checks if the user entered a valid number
                        self.use_item(user_input) # Calls use_item method with the validated user_input
                    else:
                        print("Sorry please enter a valid number")
                except:
                    print("Sorry please enter whole numbers")
                
            case "2":
                return
            case _:
                print("Sorry Try again")
                return

    def use_item(self, item):
        item_name = list(self.inventory)[item-1] # Gets item name
        item_quant = list(self.inventory.values())[item-1] # Gets number of requested item
        if item_quant <= 0:
            print("Sorry you do not have any of this item")
            return
        else:
            match item_name:
                case ("Health Potions"): # Health Potion Logic
                    self.health += 25 # Adds a flat 25 to players health
                    self.inventory[item_name] -= 1
                    item_quant = list(self.inventory.values())[item-1] # Subtracts 1 from item qaunt
                    print(text_break)
                    print("You gained 25 Health and now have" , self.health, "HP") # Updates Player
                    print("You now have", item_quant, "of", item_name, "left")
                            
player_1 = player("Ava") # TESTINg

print("")


player_1.open_inventory() # TESTING

