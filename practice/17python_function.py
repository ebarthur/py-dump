# A function is a block of reusable code 
# Place a parenthesis() in front of the function name to call / invoke it
def myFunction():
    print('My name is John Doe')
    print('I am 19 years old')
    
myFunction() # This is how you call the function
# Parameters vs Argument
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
def schoolInfo(name, age): # (name, age) are parameters
    print(f'My name is {name}')
    print(f'I am {age}')
    
schoolInfo('Kwame', 21) # My name is Kwame \n I am 21
    

# Functions with Parameters and Argument
def Addition(x, y):
    z = x + y    
    print(f'Sum is {z}')

Addition(2, 3) # Sum is 5

# Important to be mindful of indentation    

# *args and **kwargs

# *args
def addition(*args):
    total = 0
    for numbers in args:
        total += numbers
    print(f'The sum is {total}')

addition(8, 6, 15, 7) # The sum is 36

# **kwargs
def myFunction(**kwargs):
    for keys, values in kwargs.items():
        print(f'{keys} = {values}')
        
myFunction(name = 'Awal', age = 20)


# -----------------------------------------

def myFunction(name):
    '''
    This function returns the name passed in as an argument
    '''
    statement = f'My name is {name}'
    return statement

print(myFunction('Jeffery Wellington')) # My name is Jeffery Wellington
