"""Interactive Snakes and Ladders game module.

Merges and refactors ladder.txt, snakeladder.txt, and snakegame.txt.
Supports custom board sizes (20 and 100) and dynamic player counts (2-4).
"""

import random
import time
from typing import Dict, List


class SnakesAndLadders:
    """Snakes and Ladders game engine."""

    def __init__(self, target_score: int = 100):
        self.target_score = target_score
        
        # Configure board configurations
        if target_score == 20:
            self.snake_squares = {16: 4, 18: 2, 11: 8}
            self.ladder_squares = {3: 12, 7: 15}
        else:  # Default to 100
            self.target_score = 100
            self.snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
            self.ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}
            
        self.players: List[Dict] = []

    def setup_players(self) -> None:
        """Prompt and set up player names and counts safely."""
        while True:
            try:
                print(f"\nSetting up a board size of {self.target_score}.")
                count_str = input("How many players are in the game? (2-4): ").strip()
                count = int(count_str)
                if 2 <= count <= 4:
                    break
                print("Game supports only 2 to 4 players. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        self.players = []
        for i in range(1, count + 1):
            name = input(f"What is the name of Player {i}? ").strip()
            if not name:
                name = f"Player {i}"
            self.players.append({"name": name, "position": 0})

    def roll_dice(self) -> int:
        """Roll a single 6-sided die."""
        return random.randint(1, 6)

    def move_player(self, player_idx: int) -> int:
        """Roll dice and move the specified player.
        
        Handles snakes, ladders, and prints player status.
        """
        player = self.players[player_idx]
        name = player["name"]
        pos = player["position"]
        
        roll = self.roll_dice()
        new_pos = pos + roll
        
        # Check for board limits. Standard rules: must land exactly or bounce back.
        # Original version: if position > 99 (or 19), they win.
        # We will support a clean bounce-back logic, or direct win if new_pos >= target.
        # Let's keep it simple: new_pos can't exceed target, or they stay in place.
        if new_pos > self.target_score:
            print(f"{name} rolled a {roll} but needs exactly {self.target_score - pos} to win. Stays on {pos}.")
            return pos
            
        print(f"{name} rolled a {roll} and is now on {new_pos}.")
        
        if new_pos in self.snake_squares:
            down_pos = self.snake_squares[new_pos]
            print(f"🐍 Oh no! {name} got bitten by a snake and slid down to {down_pos}!")
            new_pos = down_pos
        elif new_pos in self.ladder_squares:
            up_pos = self.ladder_squares[new_pos]
            print(f"🪜 Hurrah! {name} climbed a ladder to {up_pos}!")
            new_pos = up_pos
            
        player["position"] = new_pos
        return new_pos

    def play(self) -> None:
        """Main game loop."""
        self.setup_players()
        
        names_str = ", ".join(p["name"] for p in self.players)
        print(f"\n{names_str}, welcome to Snakes and Ladders!")
        input("Press Enter to start the game...")
        
        winner = None
        round_num = 1
        
        while not winner:
            print(f"\n--- Round {round_num} ---")
            for idx in range(len(self.players)):
                player = self.players[idx]
                input(f"[{player['name']}'s turn] Press Enter to roll...")
                
                new_pos = self.move_player(idx)
                if new_pos == self.target_score:
                    winner = player["name"]
                    break
            round_num += 1
            
        print("\n" + "=" * 40)
        print(f"🏆 {winner.upper()} WINS THE GAME! 🏆")
        print("=" * 40)
        time.sleep(1.5)


def play_game() -> None:
    """Choose board size and play the game."""
    print("=" * 45)
    print("Snakes and Ladders".center(45))
    print("=" * 45)
    
    while True:
        print("\nSelect Board Size:")
        print("1. Standard Board (100 steps)")
        print("2. Mini Board (20 steps)")
        print("3. Exit")
        
        choice = input("Enter selection (1-3): ").strip()
        if choice == '1':
            game = SnakesAndLadders(target_score=100)
            game.play()
        elif choice == '2':
            game = SnakesAndLadders(target_score=20)
            game.play()
        elif choice == '3' or choice.lower() in ['exit', 'q']:
            print("Thanks for playing!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    play_game()
