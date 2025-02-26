import random

def rps_game():
    choices = ['rock', 'paper', 'scissors']
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if user_choice == 'quit':
            break
            
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("Computer wins!")

rps_game()
