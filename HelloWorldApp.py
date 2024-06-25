"""
A simple Hello World application following PEP 8 standards.
"""
import random

def main():
    """
    Main function to print 'Hello, World!'.
    """
    print("Hello, World!")
    play_janken()

def play_janken():
    """
    Function to play Rock-Paper-Scissors with the user (janken from JP)
    """
    hands = ["rock", "paper", "scissors"]
    cpu_hand = random.choice(hands)

    user_hand = input("Enter your choice (rock, paper or scissors): ").strip().lower()
    if user_hand not in hands:
        print("Invalid choice. Please choose and write 'rock', 'paper' or 'scissors'rock.")
        return
    print(f"Computer plays: {cpu_hand}")
    winner(user_hand, cpu_hand)

def winner(user_hand: str, cpu_hand: str) -> str:
    """
    Function to determine the winner of Rock-Paper-Scissors (Janken)
    """
    if user_hand == cpu_hand:
        print("That's a tie!")
    elif user_hand == "rock" and cpu_hand == "scissors":
        print("You win this round!")
    elif user_hand == "paper" and cpu_hand == "rock":
        print("You win this round!")
    elif user_hand == "scissors" and cpu_hand == "paper":
        print("You win this round!")
    else:
        print("You lose this round!")

if __name__ == "__main__":
    main()