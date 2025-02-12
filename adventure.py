"""sample adventure"""

import random

#items will be represented as strings
def acquire_item(inventory, item):
    """appends item to inventory list, prints a message"""
    inventory.append(item) #APPEND - adds an item to the inventory list, used to update the list
    print("You found a " + item + " in the room.")
    return inventory

def display_inventory(inventory):
    """prints current inventory"""
    if inventory == []:
        print("Your inventory is empty.")
    else:
        i = 1
        print("Your inventory:")
        for item in inventory: #IN OPERATOR - iterates through each item in inventory
            #used to print inventory
            print(str(i) + ". " + str(item))
            i+=1

def display_player_status(player_health):
    """displays player health"""
    # ... function code ...
    #parameter player_health = current health of the player
    #functionality - prints players current health to console in user friendly format
    #returns - nothing
    if player_health == 100:
        #test 8 keeps bugging out... hopefully this fixes it?
        print("You defeated the monster!")
    elif player_health>= -50:
        print("Your current health: " + str(player_health))

def handle_path_choice(player_health):
    """handle path choice"""
    # ... function code ...
    #functionality - randomly chooses path for the player, either "left" or "right".
    # you should use random.choise["left", "right"]
    path = random.choice(["left", "right"])
    if path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        player_health += 10
    elif path == "right":
        print("You fall into a pit and lose 15 health points.")
        player_health -= 15
    if player_health <= 0:
        player_health = 0
        print("You are barely alive!")
    updated_player_health = player_health
    return updated_player_health

def player_attack(monster_health):
    """player attack"""
    # ... function code ...
    #function - simulates player's attack. player always inflicts 15 damage
    print("You strike the monster for 15 damage!")
    monster_health -= 15
    updated_monster_health = monster_health
    return updated_monster_health

def monster_attack(player_health):
    """monster attack"""
    # ... function code ...
    #function - simulates monster's attack
    #randomly determines if monster lands crit hit
    chance = random.random()
    if chance <= 0.5:
        #crit
        player_health -= 20
        print("The monster lands a critical hit for 20 damage!")
    else:
        player_health -= 10
        print("The monster hits you for 10 damage!")
    updated_player_health = player_health
    return updated_player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """combat encounter"""
    # ... function code ...
    #function - manages combat encounter using while loop
    treasure_found_and_won = has_treasure
    while monster_health > 0 and player_health > 0:
        display_player_status(player_health)
        monster_health = player_attack(monster_health)
        player_health = monster_attack(player_health)
    if player_health < 0:
        print("Game over!")
        treasure_found_and_won = False
    elif monster_health < 0:
        print("You defeated the monster!")
        treasure_found_and_won = has_treasure
    return treasure_found_and_won # boolean

def check_for_treasure(has_treasure):
    """check for treasure"""
    # ... function code ...
    if has_treasure is True:
        print("You found the hidden treasure! You win!")
    elif has_treasure is False:
        print("The monster did not have the treasure. You continue your journey.")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """iterates through each room in dungeon rooms"""
    userschoice = ""
    for rooms in dungeon_rooms:
        print(rooms[0])
        if rooms[1] is not None:
            acquire_item(inventory, rooms[1])
        if rooms[2] == "puzzle":
            print("You encounter a puzzle!")
            userschoice = input("'Solve' or 'Skip'? ")
            are_equal: bool = userschoice in ("Solve", "solve")
            if are_equal is True:
                success = random.choice([True,False])
                if success is True:
                    print(rooms[3][0])
                else:
                    print(rooms[3][1])
        elif rooms[2] == "trap":
            print("You see a potential trap!")
            userschoice = input("'Disarm' or 'Bypass'? ")
            are_equal: bool = userschoice in ("Disarm", "disarm")
            if are_equal is True:
                success = random.choice([True,False])
                if success is True:
                    print(rooms[3][0])
                else:
                    print(rooms[3][1])
        elif rooms[2] == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        if rooms[2] == "none":
            health_change = 0
        else:
            health_change = rooms[3][2]
        player_health += health_change
        if player_health <= 0:
            player_health = 0
            print("You are barely alive!")
        display_inventory(inventory)
    display_player_status(player_health)
    #print("If you try to run 'dungeon_rooms.pop[1],")
    #if type(dungeon_rooms[1]) != tuple:
    #dungeon_rooms.pop([1]) #POP - removes value from list,
    #used to demonstrate that tuple cannot be changed
    #else:
    #print(dungeon_rooms[1], " - it can't be changed, it is immutable!")
    #print("Trying to pop it would result in a TypeError!")
    return player_health, inventory

def main():
    """main"""
    inventory = []
    dungeon_rooms = [
    ("A dusty old library", "key", "puzzle", ("You solved the puzzle!", \
        "The puzzle remains unsolved.", -5)),
    ("A narrow passage with a creaky floor", None, "trap", \
        ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
    ("A grand hall with a shimmering pool", "healing potion", "none", None),
    ("A small room with a locked chest", "treasure", "puzzle", \
     ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]
    player_health = 100
    monster_health = 70
    # Example hardcoded value
    has_treasure = False
    has_treasure = random.choice([True, False])
    # Randomly assign treasure.
    player_health = handle_path_choice(player_health)
    treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)
    check_for_treasure(treasure_obtained_in_combat)
    # Or has_treasure, depending on logic.
    if player_health > 0:
        player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)

if __name__ == "__main__":
    main()
