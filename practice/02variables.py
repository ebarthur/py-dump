# A variable is a placeholder for storing data in the computer memory
name = "Vaughn Adams"
print(name)

# VARIABLE NAMING RULES
# 1. Use descriptive names
# 2. Cannot use white spaces and hyphen in between names
# 3. Use underscore
# 4. Use camelCase notation
# 5. Cannot start with a number but can have a number in it
# 6. Cannot use reserved keywords
# 7. Python is case-sensitive

# 1. Using descriptive names
school = 'Cardinal Hayes High School'

# 2. For instance use firstname or first_name and not first name or first-name
firstname = "Vaughn" 

#3. Using underscores
last_name = 'Adams'

# 4. Use camelCase notation. 
''''camelCase is a typographical convention
 in which an initial capital is used for the first letter of a word forming the
 second element of a closed compound'''
indexNumber = 11012545
schoolInfo = ()

# 5. Cannot start with a number but can have a number in it
application2 = 'Specter Litt Law Firm' # and not 2application
# 1stnumber is not accepted
call4help = +15684584154

# 6. Cannot use reserved keywords
'''Python has a set of keywords that are reserved words 
that cannot be used as variable names, function names, or any other identifiers'''
from keyword import kwlist 
print(kwlist) #prints all reserved keywords

# 7. Python is case-sensitive
food = "Bread"
Food = "Cake" #Food and food are different variable names

# Multiple Assignment or Unpacking
x=10
y=20
z=30
x, y, z = 10, 20, 30 # This is multiple assignment
print(x)
