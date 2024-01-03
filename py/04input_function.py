# Python input function
from getpass import getpass # Hover on getpass to get the use of the module

name = input("Enter your name: ") #Takes input from user
password = getpass("Eenter your password: ") # getpass hides input to secure personal details.
print(f'You entered {name}') #Prints out user's input. 
print(password)

