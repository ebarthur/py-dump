# Import the random module for generating random numbers
import random

# Display the rules of the game
rules = "The System will select a number between 0 to 10, and you have to guess what number it is. You have 3 chances"
print(rules)

# Define a function to repeat the game
def repeat():
    # Generate a random number between 0 and 10
    secret_number = random.randrange(0, 10)
    guess_count = 0
    guess_limit = 3  # Set the maximum number of guesses allowed

    # Start a loop for the player to make guesses
    while guess_count < guess_limit:
        guess = int(input("Guess: "))  # Get the player's guess
        guess_count += 1  # Increment the guess count

        # Check if the guess is correct
        if guess == secret_number:
            print("Congrats. You Won!")
            try_again = input("Would you like to try again? 'Y' or 'N': ").lower()

            # If the player wants to try again, call the repeat function
            if try_again == 'y':
                repeat()
            # If the player chooses not to try again, provide an option to exit
            elif try_again == 'n':
                to_exit = input("Enter 'E' to exit: ").lower()
                
                # If the player enters 'E', exit the program
                if to_exit == 'e':
                    exit()

        # If the guess is incorrect and more attempts are available
        elif guess_count < guess_limit and guess != secret_number:
            print("Sorry. Try again.")
        
        # If all attempts are used and the guess is still incorrect
        elif guess_count == guess_limit and guess != secret_number:
            print("Sorry, You Failed")

            try_again = input("Would you like to try again? 'Y' or 'N': ").lower()

            # If the player wants to try again, call the repeat function
            if try_again == 'y':
                repeat()
            # If the player chooses not to try again, provide an option to exit
            elif try_again == 'n':
                to_exit = input("Enter 'E' to exit: ").lower()
                # If the player enters 'E', exit the program
                if to_exit == 'e':
                    exit()

# Call the repeat function to start the game
repeat()
