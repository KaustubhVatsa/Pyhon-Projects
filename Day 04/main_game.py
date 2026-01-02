from initial import intialize_players
from battle import attack_damage, reduce_hp
import time

def main():
    print("Welcome to the Pokemon Battle Game!")
    players = intialize_players()
    player1 = players[0]
    player2 = players[1]

    # For now, we just take the first pokemon from each party
    p1_pokemon = player1.party[0]
    p2_pokemon = player2.party[0]

    print(f"\nBattle Start: {player1.name}'s {p1_pokemon.name} VS {player2.name}'s {p2_pokemon.name}!")
    time.sleep(1)

    while p1_pokemon.current_hp > 0 and p2_pokemon.current_hp > 0:
        # Determine turn order based on speed
        if p1_pokemon.speed >= p2_pokemon.speed:
            first, second = (player1, p1_pokemon), (player2, p2_pokemon)
        else:
            first, second = (player2, p2_pokemon), (player1, p1_pokemon)

        # First Player Turn
        if not take_turn(first[0], first[1], second[1]):
            break # Game over if defender fainted
        
        # Second Player Turn
        if not take_turn(second[0], second[1], first[1]):
            break # Game over if defender fainted
        
        print("\n--- End of Round ---\n")
        time.sleep(1)

    winner = player1 if p1_pokemon.current_hp > 0 else player2
    print(f"\n🏆 {winner.name} wins the battle! 🏆")

def take_turn(attacker_player, attacker_pokemon, defender_pokemon):
    print(f"\n{attacker_player.name}'s Turn ({attacker_pokemon.name})")
    print(f"{attacker_pokemon.name} HP: {attacker_pokemon.current_hp}/{attacker_pokemon.max_hp}")
    print(f"{defender_pokemon.name} HP: {defender_pokemon.current_hp}/{defender_pokemon.max_hp}")
    
    print("Choose an attack:")
    for i, attack in enumerate(attacker_pokemon.attack):
        print(f"{i+1}. {attack.name} (Type: {attack.type}, Dmg: {attack.base_damage}, Acc: {attack.accuracy}%)")
    
    while True:
        try:
            choice = int(input("Enter attack number: ")) - 1
            if 0 <= choice < len(attacker_pokemon.attack):
                break
            print("Invalid choice!")
        except ValueError:
            print("Please enter a number.")

    # Execute Attack
    damage = attack_damage(attacker_pokemon, defender_pokemon, choice)
    
    if damage:
        print(f"{attacker_pokemon.name} used {attacker_pokemon.attack[choice].name}!")
        print(f"It dealt {damage} damage!")
        fainted = reduce_hp(defender_pokemon, damage)
        if fainted:
            return False # Game Over
    else:
        print(f"{attacker_pokemon.name} used {attacker_pokemon.attack[choice].name} but it missed!")
    
    return True # Game Continues

if __name__ == "__main__":
    main()
