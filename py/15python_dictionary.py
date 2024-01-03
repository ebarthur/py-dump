# Python dictionary is a collection of key value pair of data.
# It is ordered and mutable.
# It allows duplicate members
fruits = {}

print(fruits) # {}
print(type(fruits)) # <class 'dict'>

student_info = {'name': 'John',
                'email': 'johndoe@student.com',
                'age': 18
}

student_info['name'] = 'Devin'
print(student_info) # {'name': 'Devin', 'email': 'johndoe@student.com', 'age': 18}

# Dictionary Methods

# Copy -- Returns a copy of the dictionary
new_student_info = student_info.copy()
print(new_student_info) # {'name': 'Devin', 'email': 'johndoe@student.com', 'age': 18}
new_student_info['age'] = 21
print(new_student_info) # {'name': 'Devin', 'email': 'johndoe@student.com', 'age': 21}

# Clear -- Removes all the elements from the dictionary

new_student_info.clear()
print(new_student_info) # {}

# Pop -- Removes the element with the specified key
student_info.pop('age')
print(student_info) # {'name': 'Devin', 'email': 'johndoe@student.com'}

# Keys -- Returns a list containing the dictionary's keys

print(student_info.keys()) # dict_keys(['name', 'email', 'age'])

# Values -- Returns a list containing the dictionary's values
print(student_info.values()) # dict_values(['Devin', 'johndoe@student.com', 21])