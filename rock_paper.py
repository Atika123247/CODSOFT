import random

def rps_game():
    print("--- CodSoft Rock-Paper-Scissors Game ---")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
    
    # Optional: Initialize score tracking variables
    user_score = 0
    computer_score = 0
    
    choices = ['rock', 'paper', 'scissors']

    while True:
        # User Input: Prompt the user to choose
        user_choice = input("\nChoose rock, paper, or scissors (or type 'exit' to quit): ").strip().lower()
        
        if user_choice == 'exit':
            print("\nFinal Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! Goodbye.")
            break
            
        if user_choice not in choices:
            print("Invalid choice! Please type 'rock', 'paper', or 'scissors'.")
            continue

        # Computer Selection: Generate a random choice
        computer_choice = random.choice(choices)
        
        print(f"\nYour choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")

        # Game Logic: Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display current tracking score
        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")
        
        # Play Again prompt
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nFinal Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    rps_game()