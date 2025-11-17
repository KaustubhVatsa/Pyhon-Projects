from player import Player

#handles logic for the start of game 1.get player name 2. let the choose a pokemon 

def intialize_game():
   player_name = input("Enter your name: ")
   player = Player(player_name)
   choose_pokemon(player)
   return player

def choose_pokemon(player):
   #show the list of pokemon available and let the player choose one pokemon
   #add this pokemon to the player party list 
   #TODO:"Implement after pokemon class"
   pass

# ------------------------------
#  MENU-BASED TEST PROGRAM
# ------------------------------

from data import (
    get_pokemon_names,
    get_pokemon,
    get_attack_names,
    get_attack,
)

def show_pokemon_details(name):
    """Pretty display for a Pokemon."""
    p = get_pokemon(name)
    print("\n========== POKEMON DATA ==========")
    print(f"Name: {p.name}")
    print(f"HP: {p.max_hp}")
    print(f"Physical Attack: {p.phys_atk}")
    print(f"Magical Attack: {p.mag_atk}")
    print(f"Physical Defense: {p.phys_def}")
    print(f"Magical Defense: {p.mag_def}")
    print(f"Speed: {p.speed}")
    print(f"Dodge: {p.dodge}")
    print(f"Total Stats: {p.total_base_stat}")

    print("\nAttacks:")
    for atk in p.attack:
        print(f"  - {atk}")
    print("==================================\n")


def show_attack_details(name):
    """Pretty display for an Attack."""
    atk = get_attack(name)
    print("\n========== ATTACK DATA ==========")
    print(f"Name: {atk.name}")
    print(f"Type: {atk.type}")
    print(f"Base Damage: {atk.base_damage}")
    print(f"Accuracy: {atk.accuracy}")
    print("=================================\n")


def test():
    while True:
        print("\n====== MAIN MENU ======")
        print("1. List all Pokémon")
        print("2. Check a Pokémon")
        print("3. List all Attacks")
        print("4. Check an Attack")
        print("5. Exit")
        print("========================")

        choice = input("Enter choice: ")

        # 1) List all Pokémon
        if choice == "1":
            print("\nAll Pokémon:")
            for name in get_pokemon_names():
                print(" -", name)

        # 2) Check 1 Pokémon details
        elif choice == "2":
            name = input("Enter Pokémon name: ")
            if name in get_pokemon_names():
                show_pokemon_details(name)
            else:
                print("❌ Pokémon not found!")

        # 3) List all attacks
        elif choice == "3":
            print("\nAll Attacks:")
            for name in get_attack_names():
                print(" -", name)

        # 4) Check 1 attack details
        elif choice == "4":
            name = input("Enter Attack name: ")
            if name in get_attack_names():
                show_attack_details(name)
            else:
                print("❌ Attack not found!")

        # Exit
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")
test() 