# Loop
# A 'for loop' is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a string or a set)

# For loop
name = 'Aninakwa'
    #   01234567
    
for i in name:
    print(i) # Print out every character in the variable 'name'

# Loop through List
fruits = ['mango', 'banana', 'apple', 'orange', 'pineapple']

for fruit in fruits:
    print(fruit)                    # mango
                                    # banana
                                    # apple
    if fruit == 'apple':
        break

numbers = [1, 2, 3] 
total = 0

for x in numbers:
    total += x
    
print(total) # 6

# Loop through multiple Lists simultaneously using zip nethod
names = ['John', 'Dave', 'Ryan']
scores = [90, 80, 98]

for x, y in zip(names, scores):
    print(f'{x} scored {y}')
    # John scored 90
    # Dave scored 80
    # Ryan scored 98

# range method and loops
for x in range(10):
    print(x) # 0, 1, 2, 3, .... , 9

for y in range(3, 13):
    print(y) # 3, 4, 5, 6, .... , 12

for z in range(0, 101, 4):
    print(z) # 0, 4, 8, 12, 16, 20, 24, .... , 100
    
# Loop through Dictionary

# Exercise
# 1. Find all the even numbers in a range
# 2. Find the sum of all elements in a list
# 3. Find the factorial of a number

# 1
for even_numbers in range(0, 21, 2):    
    print(even_numbers) # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
    
    
prime = [2, 3, 5, 7, 11, 13, 17, 23]
total = 0

# 2
for i in prime:
    total += i
print(total)    # 81

# 3
import math
x = int(input('This function returns the factorial of any number\nEnter number: '))

print(math.factorial(x))

# While loops
limit = 3
count = 0

while count < limit:
    data = input('Enter your number: ')
    if data.isnumeric():
        print(f'{data} is numeric')
        break
    
    else:
        if count < 1:
            print('Wrong input')
            
        elif count == 1:
            print('Wrong input. This is your last chance')
    count += 1