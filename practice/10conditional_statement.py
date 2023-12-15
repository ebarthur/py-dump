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


def repeat():
    while rule == 's': 
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))

        if num1 > num2:
            print(f'{num1} is greater than {num2}')

        elif num2 > num1:
            print(f'{num2} is greater than {num1}')

        elif num1 == num2:
            print(f'{num1} is equal to {num2}')

        go_again = input('Do you want to try again?\n (y) or (n): ').lower()
        if go_again == 'y':
            repeat()

        else: 
            to_exit = input('Press (E) to exit: ').lower()
            if to_exit == 'e':
                exit()
                                    
repeat()                        

#Check Odd or Even numbers
rule = 'THIS PROGRAM CHECKS WHETHER A NUMBER IS EVEN OR ODD'
print(rule)

num = int(input('Enter number: '))
if num % 2 == 0:
    print(f'{num} is an even number')
elif num % 2 != 0:
    print(f'{num} is an odd number')

# Grade check results:
# User input score and grade displays in the terminal

def calculate_grade(score):
    if 0 <= score <= 100:
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        elif score >= 50:
            return 'E'
        else:
            return 'F'
    else:
        return 'Invalid score. Please enter a score between 0 and 100'
    
user_score = int(input('Enter the score: '))
result = calculate_grade(user_score)
print("Grade:", result)

calculate_grade(user_score)