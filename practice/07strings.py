# Python string and methods


# When to use single or double quotation marks
# 'University of Texas'
print("'University of Texas'")

# "University of Southern California"
print('"University of Southern California"')

# Ghana's Premier University
print("Ghana's Premier University")


# Indexing: Python indexing starts from 0
school = "Achimota School"
# Index   0123456789...
print(school[0]) # A
print(school[9]) # S
print(school[-1]) # Negative indexing starts from right to left: "l"
print(school[:]) # Slicing: "Achimota School"
print(school[3:]) # "imota School"


# len function: returns the length (number of elements/characters)
location = "San Francisco Bay"
print(len(location)) # 17


# STRING METHODS

# Capitalize -- Converts the first character to uppercase
major = 'computer engineering'
print(major.capitalize()) # 'Computer engineering'


# Count -- Returns the number of times a specified character occurs in a string
print(major.count('e')) # 4. Counts the number of times the letter 'e' appears in the data


# Find -- Searches the string for a specified value and returns the position (index) of where it was found
course = 'Discrete Math'

print(course.find('a')) # 10
print(course.find('s')) # 2


# Index -- Searches the string for a specified value and returns the position of where it was found
print(course.index('a')) # 10
print(course.index('s')) # 2


# Replace -- Replaces a specified value with another
capitalCity = 'Salt Lake City'

print(capitalCity.replace('Salt', 'Sugar')) # 'Sugar Lake City'
print(capitalCity.replace('Lake', '')) # 'Salt City'


# Lower -- Converts a string into lower case
print(capitalCity.lower()) #s 'salt lake city'


# Upper -- Converts a string into upper case
team = 'golden state warriors'
print(team.upper()) # 'GOLDEN STATE WARRIORS


# Isalnum -- Returns True if all characters in the string are alphanumeric
password = 'blackmamba24'
print(password.isalnum()) # True


# Isdigit -- Returns True if all characters in the string are digits
pass1 = 'joe23'
pass2 = '145'

print(pass1.isdigit()) # False
print(pass2.isdigit()) # True


# Isspace -- Returns True if all characters in the string are whitespaces
family = ' '
print(family.isspace()) # True


# Split -- Splits the string at the specified separator, and returns a list
dept = 'Human Resource Management'
print(dept.split()) # ['Human', 'Resource', 'Management']
print(len(dept.split())) # 3

message = 'You are about to die at the hands of the children of Thanos'

word = message.split()
word_count = len(word)

print(word) # ['You', 'are', 'about', 'to', 'die', 'at', 'the', 'hands', 'of', 'the', 'children', 'of', 'Thanos']
print(word_count) # 13


# Startswith -- Returns true if the string starts with the specified value
pet = 'Chihuahua'
print(pet.startswith('C')) # True
print(pet.startswith('c')) # False


# Endswith -- Returns true if the string ends with the specified value
print(pet.endswith('a')) # True
print(pet.endswith('u')) # False

#Example
file_name = 'code.py'
print(file_name.endswith('.py')) # True





