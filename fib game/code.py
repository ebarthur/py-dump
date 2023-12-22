import random
import time

# ANSI color codes for better visualization
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"

# Global variable for high score
high_score = 0

# Define difficulty levels
difficulty_levels = {
    'easy': {'hidden_room_chance': 0.1, 'bonus_points_range': (5, 15)},
    'medium': {'hidden_room_chance': 0.2, 'bonus_points_range': (10, 20)},
    'hard': {'hidden_room_chance': 0.3, 'bonus_points_range': (15, 25)}
}

# Function to print text with optional typing effect
def type_text(text, delay=0.03, input_prompt=False, color=Colors.RESET):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Colors.RESET)

    if input_prompt:
        return input()

# Function to calculate Fibonacci sequence up to the nth term
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Function to display the game introduction
def display_intro():
    type_text("Welcome to the Infinite Fibonacci Room Adventure Game!", color=Colors.BOLD)
    type_text("The goal is to reach the end with the highest possible score.", color=Colors.BOLD)
    type_text(''*4)
    print(f"You start in Room 1 with 0 points.")
    type_text(f"Current High Score: {high_score}", color=Colors.CYAN)

# Function to play the main game
def play_game(difficulty):
    global high_score  # Access the global high score variable
    current_room = 1
    total_points = 0

    # Get difficulty parameters
    params = difficulty_levels.get(difficulty, difficulty_levels['medium'])

    # Main game loop
    while True:
        time.sleep(1)
        print(f"\nCurrent Room: {current_room}")
        print(f"Total Points: {total_points}")

        # Introduce a chance of discovering a hidden room based on difficulty
        if random.random() <= params['hidden_room_chance']:
            hidden_points = random.randint(*params['bonus_points_range'])
            print(f"You discovered a hidden room and earned {hidden_points} bonus points!", color=Colors.GREEN)
            total_points += hidden_points

        # Randomize the order of doors
        doors = random.sample([1, 2], 2)
        time.sleep(0.75)
        type_text(''*4)
        print(f"You see two doors in front of you:")
        print('-'*40)
        time.sleep(0.75)
        type_text(f"Door leading to the next Fibonacci room", color=Colors.GREEN)
        print()
        type_text(f"Danger! Door that might end your journey", color=Colors.RED)
        print('-'*40)
        time.sleep(1)
        choice = type_text("Choose a door (1 or 2): ", input_prompt=True)

        if choice == str(doors[0]):
            # Earn points based on the Fibonacci sequence
            points_earned = fibonacci(current_room)
            type_text(f"\nYou earned {points_earned} points in this room.", color=Colors.YELLOW)
            total_points += points_earned
            current_room += 1
        elif choice == str(doors[1]):
            type_text("\nOh no! You chose the dangerous door, and your journey ends here.", color=Colors.RED)
            type_text(f"You earned a total of {total_points} points.")

            # Check if the player beat the high score
            if total_points > high_score:
                high_score = total_points
                type_text(f"Congratulations! You've set a new high score: {high_score} points.", color=Colors.GREEN)
            else:
                type_text("Better luck next time!", color=Colors.RED)

            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")

# Function to ask the player if they want to play again
def play_again():
    while True:
        choice = type_text("Do you want to play again? (yes/no): ", input_prompt=True).lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

# Main function to initiate the game
def main():
    while True:
        display_intro()

        # Ask for difficulty level
        difficulty = type_text("Choose a difficulty level (easy/medium/hard): ", input_prompt=True).lower()

        # Validate the difficulty level
        if difficulty not in difficulty_levels:
            print("Invalid difficulty level. Defaulting to medium.")

        play_game(difficulty)

        if not play_again():
            exit_choice = type_text("Press 'e' to exit or any other key to play again: ", input_prompt=True).lower()
            if exit_choice == 'e':
                print("\nThanks for playing! Goodbye!")
                break
            else:
                print("\nLet's play again!")

# Execute the main function if this script is run
if __name__ == "__main__":
    main()
