import random
import time

# Global variable for high score
high_score = 0

def type_text(text, delay=0.03, input_prompt=False):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

    if input_prompt:
        return input()

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

def display_intro():
    type_text("Welcome to the Infinite Fibonacci Room Adventure Game!")
    type_text("The goal is to reach the end with the highest possible score.")
    type_text(''*4)
    print(f"You start in Room 1 with 0 points.")
    type_text(f"Current High Score: {high_score}")

def play_game():
    global high_score  # Access the global high score variable
    current_room = 1
    total_points = 0

    while True:
        time.sleep(1)
        print(f"\nCurrent Room: {current_room}")
        print(f"Total Points: {total_points}")

        # Introduce a chance of discovering a hidden room
        if random.randint(1, 10) == 1:
            hidden_points = random.randint(5, 20)
            print(f"You discovered a hidden room and earned {hidden_points} bonus points!")
            total_points += hidden_points

        doors = random.sample([1, 2], 2)  # Randomize the order of doors
        time.sleep(0.75)
        type_text(''*4)
        print(f"You see two doors in front of you:")
        print('-'*30)
        time.sleep(0.75)
        print(f"Door leading to the next Fibonacci room")
        print()
        print(f"Danger! Door that might end your journey")
        print('-'*30)
        time.sleep(1)
        choice = type_text("Choose a door (1 or 2): ", input_prompt=True)

        if choice == str(doors[0]):
            points_earned = fibonacci(current_room)
            type_text(f"\nYou earned {points_earned} points in this room.")
            total_points += points_earned
            current_room += 1
        elif choice == str(doors[1]):
            type_text("\nOh no! You chose the dangerous door, and your journey ends here.")
            type_text(f"You earned a total of {total_points} points.")

            # Check if the player beat the high score
            if total_points > high_score:
                high_score = total_points
                type_text(f"Congratulations! You've set a new high score: {high_score} points.")
            else:
                type_text("Better luck next time!")

            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")

def play_again():
    while True:
        choice = type_text("Do you want to play again? (yes/no): ", input_prompt=True).lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

def main():
    while True:
        display_intro()
        play_game()

        if not play_again():
            exit_choice = type_text("Press 'e' to exit or any other key to play again: ", input_prompt=True).lower()
            if exit_choice == 'e':
                print("\nThanks for playing! Goodbye!")
                break
            else:
                print("\nLet's play again!")

if __name__ == "__main__":
    main()
