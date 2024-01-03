import random
import time

def type_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# print multiline instruction with typing effect
type_text('Winning rules of the game ROCK PAPER SCISSORS are :\n'
    + "Rock vs Paper -> Paper wins \n"
    + "Rock vs Scissors -> Rock wins \n"
    + "Paper vs Scissors -> Scissor wins \n")

while True:
    type_text("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from the user
    choice = int(input("Enter your choice: "))

    # OR is the short-circuit operator
    # if any one of the conditions is true
    # then it returns True value

    # looping until the user enters an invalid input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

    # initialize the value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # print user choice
    type_text('User choice is \n' + choice_name)
    type_text('Now it\'s Computers Turn....')

    # Computer chooses randomly any number
    # among 1, 2, and 3. Using randint method
    # of the random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # initialize the value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'rocK'
    elif comp_choice == 2:
        comp_choice_name = 'papeR'
    else:
        comp_choice_name = 'scissoR'
    type_text("Computer choice is \n" + comp_choice_name)
    type_text(choice_name + ' Vs ' + comp_choice_name)

    # we need to check for a draw
    if choice == comp_choice:
        type_text('It\'s a Draw', end="")
        result = "DRAW"
    # condition for winning
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        type_text('paper wins =>', end="")
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        type_text('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        type_text('Scissors wins =>', end="")
        result = 'Scissors'

    # Printing either user or computer wins or draw
    if result == 'DRAW':
        type_text("<== It's a tie ==>")
    elif result == choice_name:
        type_text("<== User wins ==>")
    else:
        type_text("<== Computer wins ==>")
    type_text("Do you want to play again? (Y/N)")
    # if the user input n or N then the condition is True
    ans = input().lower()
    if ans == 'n':
        break

# after coming out of the while loop
# we print thanks for playing
type_text("Thanks for playing")
