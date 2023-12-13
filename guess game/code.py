import random
rules = "The System will select a number between 0 to 10 and you have to guess what number it is. You have 3 chances"

print(rules)

def repeat():
    secret_number = random.randrange(0,10)
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count+=1

        if guess == secret_number:
            print("Congrats. You Won!")
            try_again = input("Would you like to try again? 'Y' or 'N': ").lower()

            if try_again == 'y':

                repeat()
                
            elif try_again == 'n':
                to_exit = input("Enter 'E' to exit: ").lower()
                
                if to_exit == 'e':
                    exit()

        elif guess_count < guess_limit and guess!= secret_number:
            print("Sorry. Try again.")

        elif guess_count == guess_limit and guess != secret_number:
            print("Sorry, You Failed")

            try_again = input("Would you like to try again? 'Y' or 'N': ").lower()

            if try_again == 'y':
                repeat()

            elif try_again == 'n':

                to_exit = input("Enter 'E' to exit: ").lower()
                if to_exit == 'e':
                    exit()

repeat()
