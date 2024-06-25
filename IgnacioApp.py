"""
A Hello World and Rock-Paper-Scissors applicaction, very simple and basic.
"""
import random

def main():
    """
    Main function that prints Hello World, makes the user play Rock-Paper-Scissors
    with the cpu and recommends a song.
    """
    print("Hello, World!")
    play_janken()
    recommend_a_song()


def play_janken():
    """
    Function to play Rock-Paper-Scissors with the user (janken from the Japanese name)
    """
    hands = ["rock", "paper", "scissors"]
    cpu_hand = random.choice(hands) # Chooses a random string from the list 'hands'.

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

def recommend_a_song():
    """
    Function that prints a random song from the songs in songs.txt .
    """
    songs = open("songs.txt").read().split('\n')
    song = random.choice(songs)
    print(f"You may have won, lost or tied, anyways, go listen to this song: {song}")


if __name__ == "__main__": # Para que al llamar al programa se ejecute
    main()