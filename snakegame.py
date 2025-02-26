import random

# Options for the game
choices = ["snake", "water", "gun"]

# Ask the player for their choice
player = input("You Choose : ").lower()

# Computer picks a random choice
computer = random.choice(choices)

print("Computer chose:", computer)

# Winning rules
if player == computer:
    print("It's a tie!")
elif (player == "snake" and computer == "water") or \
     (player == "water" and computer == "gun") or \
     (player == "gun" and computer == "snake"):
    print("You win! 🎉")
else:
    print("Computer wins! 😢")
