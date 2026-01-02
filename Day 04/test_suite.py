import unittest
from unittest.mock import patch
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

from data import get_pokemon, get_attack
from battle import attack_damage, reduce_hp, check_faint
from pokemon import Pokemon

class TestPokemonGame(unittest.TestCase):
    def setUp(self):
        self.p1 = get_pokemon("Pikachu")
        self.p2 = get_pokemon("Squirtle")

    def test_pokemon_creation(self):
        """Test that Pokemon are created with correct stats and unique instances."""
        p1_copy = get_pokemon("Pikachu")
        self.assertNotEqual(id(self.p1), id(p1_copy), "Pokemon instances should be unique")
        self.assertEqual(self.p1.name, "Pikachu")
        self.assertEqual(self.p1.current_hp, 60)
        self.assertEqual(self.p1.max_hp, 60)

    def test_damage_calculation(self):
        """Test damage calculation logic."""
        # Pikachu uses Thunderbolt (Magical, 25 dmg) vs Squirtle (Mag Def 65)
        # Damage = 25 + 70 (Mag Atk) - 65 (Mag Def) = 30
        # Wait, logic is: base + atk - def
        # Thunderbolt: 25 base. Pikachu Mag Atk: 70. Total: 95.
        # Squirtle Mag Def: 65.
        # Expected: 95 - 65 = 30.
        
        # Mock random to ensure hit
        with patch('random.randint', return_value=1): 
            damage = attack_damage(self.p1, self.p2, 1) # Index 1 is Thunderbolt
            self.assertEqual(damage, 30)

    def test_hp_reduction(self):
        """Test HP reduction and fainting."""
        initial_hp = self.p2.current_hp
        fainted = reduce_hp(self.p2, 20)
        self.assertEqual(self.p2.current_hp, initial_hp - 20)
        self.assertFalse(fainted)

        # Fatal damage
        fainted = reduce_hp(self.p2, 1000)
        self.assertEqual(self.p2.current_hp, 0)
        self.assertTrue(fainted)

    def test_turn_order_logic(self):
        """Test speed based turn order."""
        # Pikachu (90) vs Squirtle (50)
        self.assertGreater(self.p1.speed, self.p2.speed)
        
        # Snorlax (20) vs Pikachu (90)
        snorlax = get_pokemon("Snorlax")
        self.assertLess(snorlax.speed, self.p1.speed)

if __name__ == '__main__':
    unittest.main()
