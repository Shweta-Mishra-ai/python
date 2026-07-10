"""Interactive Rock Paper Scissors game module.

Supports Human-vs-Computer and Computer-vs-Computer modes.
Fixes fixed computer choices, string comparison, and casing bugs from rock.txt and rockpaper.txt.
"""

import random
from typing import str as TypeStr

CHOICES = ["rock", "paper", "scissors"]

def determine_winner(player: str, computer: str) -> str:
    """Determine the result of a single round.
    
    Returns a string summary of the result.
    """
    if player == computer:
        return "Tie!"
    
    if player == "rock":
        if computer == "paper":
            return f"You lose! {computer.capitalize()} covers {player}."
        else:
            return f"You win! {player.capitalize()} smashes {computer}."
            
    if player == "paper":
        if computer == "scissors":
            return f"You lose! {computer.capitalize()} cuts {player}."
        else:
            return f"You win! {player.capitalize()} covers {computer}."
            
    if player == "scissors":
        if computer == "rock":
            return f"You lose... {computer.capitalize()} smashes {player}."
        else:
            return f"You win! {player.capitalize()} cuts {computer}."
            
    return "Invalid game state"


def play_human_vs_computer() -> None:
    """Run the Human vs Computer Rock Paper Scissors game loop."""
    print("\n--- Human vs Computer Mode ---")
    while True:
        # Prompt player choice
        user_input = input("Enter your play (Rock, Paper, Scissors) or 'q' to quit: ").strip().lower()
        if user_input in ['q', 'quit']:
            break
            
        if user_input not in CHOICES:
            print("That's not a valid play. Check your spelling!")
            continue
            
        # Select computer choice dynamically
        computer_choice = random.choice(CHOICES)
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # Determine and print winner
        result = determine_winner(user_input, computer_choice)
        print(result)
        print("-" * 30)


def play_computer_vs_computer() -> None:
    """Run the Computer vs Computer Rock Paper Scissors game loop."""
    print("\n--- Computer vs Computer Mode ---")
    rounds_input = input("How many rounds would you like to simulate? ")
    try:
        rounds = int(rounds_input)
    except ValueError:
        print("Invalid input. Simulating 3 rounds.")
        rounds = 3
        
    for i in range(1, rounds + 1):
        c1 = random.choice(CHOICES)
        c2 = random.choice(CHOICES)
        print(f"\nRound {i}:")
        print(f"Computer 1 choice: {c1.capitalize()}")
        print(f"Computer 2 choice: {c2.capitalize()}")
        
        if c1 == c2:
            print("It's a Tie!")
        else:
            # We treat Computer 1 as player and Computer 2 as computer
            res = determine_winner(c1, c2)
            # Adjust wording for computer vs computer
            res = res.replace("You win!", "Computer 1 wins!").replace("You lose!", "Computer 2 wins!").replace("You lose...", "Computer 2 wins!")
            print(res)
    print("-" * 30)


def play_game() -> None:
    """Main entry point to start the Rock Paper Scissors game."""
    print("=" * 45)
    print("Welcome to Rock, Paper, Scissors!".center(45))
    print("=" * 45)
    
    while True:
        print("\nSelect Game Mode:")
        print("1. Human vs Computer")
        print("2. Computer vs Computer")
        print("3. Exit Game")
        
        mode = input("Enter option (1-3): ").strip()
        if mode == '1':
            play_human_vs_computer()
        elif mode == '2':
            play_computer_vs_computer()
        elif mode == '3' or mode.lower() in ['exit', 'q']:
            print("Thanks for playing!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    play_game()
