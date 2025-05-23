""" Necessary Modules:
- json: To handle JSON data for questions and answers."""
# Trivia Game
# This is a simple trivia game where the user is asked a series of questions (retrieved from a JSON file).
import json
import os

# Main Menu 
def main_menu():
    print("Welcome to the Trivia Game!")
    print("1. Start Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        start_game()
    elif choice == '2':
        exit_game()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# Start Game
def start_game():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen at the start
    print("Starting the game...")
    # Load questions from JSON file generated by Github Copilot
    with open('questions.json', 'r') as file:
        questions = json.load(file)
    
    score = 0
    for question in questions:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")
        
        answer = input("Enter your answer (1-4): ")
        if question['options'][int(answer) - 1] == question['answer']:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
            print(f"The correct answer was: {question['answer']}")
        input("Press Enter to continue...")  # Pause before next question
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen before showing the score
    print(f"Your score: {score}/{len(questions)}")
    # Clear the screen before showing the main menu
    input("Press Enter to return to the main menu...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    main_menu()

# Exit Game
def exit_game():
    print("Thank you for playing the Trivia Game!")
    exit()

# Run the main menu
if __name__ == "__main__":
    main_menu()
