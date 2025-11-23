from player import Player
from data import get_pokemon_names, get_pokemon, get_attack_names, get_attack

#handles logic for the start of game 1.get player name 2. let the choose a pokemon 

def intialize_players():
    player1 = Player(input("Enter player 1 name: "))
    player2 = Player(input("Enter player 2 name: "))    
    for i in range(1): # Each player picks 1 pokemon for now
        print(f"\n--- {player1.name}'s Turn ---")
        choose_pokemon(player1)
        print(f"\n--- {player2.name}'s Turn ---")
        choose_pokemon(player2)
    return [player1, player2]

def choose_pokemon(player):
   available_pokemons = get_pokemon_names()
   print("Available Pokemons : ")
   for name in available_pokemons:
      print(f" - {name}")
   
   while True:
       pokemon_name = input("Enter pokemon name: ").strip().capitalize()
       if pokemon_name in available_pokemons:
           player.party.append(get_pokemon(pokemon_name))
           print (f"{player.name} has caught {pokemon_name}")
           show_pokemon_details(pokemon_name)
           break
       else:
           print("Invalid pokemon name ! Try again !")

# ------------------------------
#  MENU-BASED TEST PROGRAM
# ------------------------------

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
