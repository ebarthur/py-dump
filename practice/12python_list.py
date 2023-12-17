# Python list is a collection which is ordered and mutable.
# It allows duplicate members

countries = ['Ghana', 'Nigeria', 'Germany', 'France', 'China']

print(countries) # ['Ghana', 'Nigeria', 'Germany', 'France', 'China']
print(type(countries)) # <class 'list'>

print(countries[1]) # Nigeria
countries[1] = 'Haiti'
print(countries[1]) # Haiti (Mutable)

# len function
print(len(countries)) # 5

# LIST METHODS
# Append -- Adds an element at the end of the list
countries.append('Jamaica')

print(countries) # ['Ghana', 'Haiti', 'Germany', 'France', 'China', 'Jamaica']

# Clear -- Removes all the elements from the list
# countries.clear()
# print(countries) # []

# Copy -- Returns a copy of the list
new_countries= countries.copy()

print(new_countries) # It prints out a copy of the 'countries' list

# Count -- Returns the number of elements with the specified value
print(countries.count('Germany')) # 0 because the `clear` method is implemented and so the list is empty. Comment previous methods out

# Index -- Returns the index of the first element with the specified value

print(countries.index('France')) # 3

# Sort -- Sorts the list

scores = [90, 89, 77, 90, 40, 60, 50, 43]

scores.sort()
print(scores) # [40, 43, 50, 60, 77, 89, 90, 90]

scores.sort(reverse=True)
print(scores) # [90, 90, 89, 77, 60, 50, 43, 40]

# Reverse -- Reverses the order of the list
scores.reverse
print(scores) # Try it on your own

# Remove -- Removes the first item with the specified value
scores.remove(90)

print(scores) # [90, 89, 77, 60, 50, 43, 40]

# Pop -- Removes the element at the specified position
countries.pop()
print(countries) # ['Ghana', 'Haiti', 'Germany', 'France', 'China'] It pops out the last item if position is not specified

countries.pop(1)
print(countries) # ['Ghana', 'Germany', 'France', 'China']