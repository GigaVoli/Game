# %% Imports
import sys
import Shoppingcart
Options = ["1", "2", "3", "4"]
# %% Variables
inventory = []
# %% Dictionary
Dict = {"flashlight", "tent", "food and water", "tools", "map", "wand", "spellbook", "cool robes", "gold"}
# %% Function
def introScene():
    print("Welcome! This is a text based adventure game, meaning you will have the false sence os freedom, but all interactiong are actualy pre-coded! Have fun! Options are ordered 1, 2, 3, and 4 respective to their order.")
    print("Do you wake up or sleep in? (options 1(wake up) or 2(sleep in))")
    userInput = ""
    MaxHeath = 100
    Health = 100
    DeamonHealth = 100
    Speed = 100
    while userInput not in Options:
        userInput = input()
        # Starts the game
        if userInput == "1":
            print("You wake up")
            Sleep = False
            
        elif userInput == "2":
            print("You stay alseep")
            Sleep = True
    print("You're going camping, do you pack lightly or heavily (options 1(lightly) or 2(heavily))")
    userInput = ""
    while userInput not in Options:
        userInput = input()
        if userInput == "1":
            print("You pack lightly")
            inventory.append("flashlight")
            inventory.append("tent")
            inventory.append("food and water")
            inventory.append("wand")
            inventory.append("spellbook")
            print(inventory)
            
            
        elif userInput == "2":
            print("You pack heavily")
            Speed -=10
            inventory.append("flashlight")
            inventory.append("tent")
            inventory.append("food and water")
            inventory.append("wand")
            inventory.append("spellbook")
            inventory.append("tools")
            inventory.append("map")
            inventory.append("cool robes")
            inventory.append("gold")
            print(inventory)
            
    print("You get to the campsite, and you see a sparkling trail in the woods and hear a muffled laugh, do you follow it? (options 1(yes) or 2(no))")
    userInput = ""
    while userInput not in Options:
        userInput = input()
        if userInput == "1":
            print("You follow it, and find a spellbook with a light glowing aura around it. It has a note in a language you dont understand.")
            inventory.append("weird note")
            inventory.append("strange book")
            print(inventory)
            followedDeamon = True
        elif userInput == "2":
            print("You ignore it")
            followedDeamon = False
            
    if followedDeamon == True:
        print("You see a deamon approach you, and you feel you're life drained out of you as it raises its hand, what do you do? (options 1(firebolt) or 2(heal) or 3(holy ray))")
        Health -=10
    userInput = ""
    while DeamonHealth > 0:
        userInput = input()
        if userInput == "1":
            print("You cast firebolt, and the deamon is unfazed, and smirks at you, raising its hand again.")
            Health -=15
            
        elif userInput == "2":
            print("You cast heal, and heal yourself. To your suprise, the deamon is harmed to, but manages to get an attack off. You are hurt, but this seems to be working. What do you do? (options 1(firebolt) or 2(heal) or 3(holy ray))")
            Health += 15
            DeamonHealth -= 30
            Health -=7
            print(Health)
            
        elif userInput == "3" and "strange book" in inventory:
            print("You cast holy ray, and the deamon is badly hurt, and retreats into the woods. You find a strip of deamon leather on the ground.")
            DeamonHealth = 0
            inventory.append("deamon leather")
            print(inventory)
        else:
            print("You do not have the required item to cast this")
            
# %% Start
if __name__ == "__main__":
    ## Print statments
    print("Welcome to the text based adventure!")
    print("Press 1 to start, press 2 to exit")
    ## List of options and user input
    Options = ["1", "2", "3", "4"]
    userInput = ""
    ## Will continue if the number is not in the list
    while userInput not in Options:
        userInput = input()
        # Starts the game
        if userInput == "1":
            print("Welcome!")
            introScene()
        # Exits the game
        elif userInput == "2":
            sys.exit()
        # Is snarky about you doing the wrong thing
        else:
            print("Did you even listen? 1 or 2! Try again!")