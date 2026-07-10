"""Interactive Russian Roulette game module.

Refactors and enhances russionrolled.txt to be clean, interactive, and PEP 8 compliant.
Allows the user to enter their name and participate in a suspenseful elimination game.
"""

import random
import time
from typing import List


def run_roulette() -> None:
    """Run an interactive Russian Roulette game."""
    print("=" * 45)
    print("Russian Roulette Elimination".center(45))
    print("=" * 45)
    print("\nIn this game, players take turns pulling the trigger on a 6-chamber revolver.")
    print("One chamber holds a live round. The cylinder is spun before the round starts.")
    print("Survival of the luckiest!")
    
    # Setup players
    default_players = ["Shweta", "Gunjan", "Arti", "Shivani", "Nidhi", "Deeksha", "Neha", "Alka"]
    
    print("\nDefault participants:", ", ".join(default_players))
    user_name = input("Enter your name to join (or press Enter to watch simulation): ").strip()
    
    players = list(default_players)
    if user_name:
        players.append(user_name)
        
    print(f"\nTotal participants ({len(players)}): {', '.join(players)}")
    input("Press Enter to load the bullet and spin the cylinder...")
    
    round_num = 1
    # Cylinder has 6 chambers
    chambers = [False] * 6
    chambers[random.randint(0, 5)] = True  # Load one bullet
    current_chamber = 0
    
    # We eliminate players one by one until only one is left
    while len(players) > 1:
        print(f"\n--- Round {round_num} (Players left: {len(players)}) ---")
        
        # Select player whose turn it is
        current_player = players[0]
        
        print(f"It is {current_player}'s turn.")
        if current_player == user_name:
            input("👉 Press Enter to pull the trigger... Good luck!")
        else:
            time.sleep(1.0)
            print(f"{current_player} takes the revolver and aims...")
            time.sleep(1.0)
            
        # Spin cylinder periodically or just check the current chamber
        # Russian roulette has two variants: spin the cylinder before every pull,
        # or pull sequentially. Sequential pull guarantees someone gets hit in 6 shots.
        # Let's do sequential check as it is more suspenseful.
        is_bullet = chambers[current_chamber]
        current_chamber = (current_chamber + 1) % 6
        
        print("*Click* ...")
        time.sleep(1.2)
        
        if is_bullet:
            print(f"💥 BANG! {current_player} is eliminated!")
            players.pop(0)  # Remove player
            # Reset revolver for the remaining players
            chambers = [False] * 6
            chambers[random.randint(0, 5)] = True
            current_chamber = 0
            time.sleep(1.5)
        else:
            print(f"💨 Phew! {current_player} survived!")
            # Move player to the back of the queue
            players.append(players.pop(0))
            time.sleep(1.0)
            
        round_num += 1
        
    print("\n" + "=" * 40)
    print(f"🏆 WINNER: {players[0].upper()} 🏆")
    print("=" * 40)
    time.sleep(1.5)


if __name__ == "__main__":
    run_roulette()
