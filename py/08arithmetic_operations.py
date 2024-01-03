# Python arithmetic operations + - * / // % **

# Addition +
x = 10
y = 5

result = x + y
print(result) # 15
print(6+4) # 10

a = '7'
b = '8'

print(a+b) # 78: Concatenation


# Subtraction -
q = 10
r = 7

print(q+r) # 17


# Multiplication *
m = 10
n = 3

print(m*n) # 30


# Division /
print(m/n) # 3.3333333

# Floor Division //
floor = m//n

print(type(floor)) # <class 'int'>
print (floor) # 3


# Power **
x = 3
y = 2

result = x ** y
print(result) # 9


# Modulus %
x = 10
y = 2

result = x % y # 10mod2
print(result) # 0


# Order of precedence-> (BODMAS)
expression1 = 10+10/2+5
expression2 = (10+10)/2+5

print(expression1) # 20.0
print(expression2) # 15.0


# Math functions

# round
x = 17
y = 3

print(x/y)        # 5.6666666
print(round(x/y)) # 6
print(round(x/y, 4)) # 5.6667


# absolute value
x = 10
y = -10

print(abs(y)) # 10


# Interactive program

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
result = number1 + number2

print(f'Sum of {number1} and {number2} = {result}')

# Converting datatypes
x = float(8)

print(x) # 8.0
print(type(x)) # <class 'float'>

y = bool('True') # This is a string

print(y) # True
print(type(y)) # <class 'bool'>
 

# Try 
# Write a program that accepts two values from the user in the 
# terminal and performs a modulus operation

# Input function, formatted string, arithmetic operators
# Enter first value: 
# Enter second value: 
# The mod of 10mod2 =


#Solution

# Get user input for the first value
first_value = float(input("Enter the first value: "))

# Get user input for the second value, ensuring it's not zero
while True:
    second_value = float(input("Enter the second value (non-zero): "))
    if second_value != 0:
        break
    else:
        print("Second value cannot be zero. Please enter a non-zero value.")

# Calculate the modulus
mod_result = first_value % second_value

# Print the result
print(f"The mod of {first_value} mod {second_value} = {mod_result}")
