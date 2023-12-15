# Python conditional statement if else elif
voting_age = 18
age = (input('Enter your age: '))

if age.isnumeric():          
    if int(age) >= voting_age:
        print('You are qualified to vote')
        
    elif int(age) < voting_age:
        print('You are not qualified to vote')

else:
    print('Invalid input\nTry again')


# EXERCISE

# Program takes two inputs and checks which of the inputs is greater
rule = input("THIS PROGRAM TAKES TWO VALUES AND CHECKS WHICH ONE IS GREATER\nPress 'S' to start: ").lower()

if rule == 's':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 > num2:
        print(f'{num1} is greater than {num2}')

    elif num1 < num2:
        print(f'{num2} is greater than {num1}')

    else:
        print(f'{num1} is equal to {num2}')      

else:
    exit()

# Check Odd or Even numbers

# Grade check results:
# User input score and grade displays in the terminal
