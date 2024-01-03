# Python tuple is a collection which is ordered.
# A tuple is not mutable
# It allows duplicate members
fruits= ('Mango', 'Apple', 'Banana')

print(type(fruits)) # <class 'tuple'>
print(fruits) # ('Mango', 'Apple', 'Banana')
print(fruits[0]) # Mango

# Count
# Index
print(fruits.count('Banana')) # 1
print(fruits.index('Apple'))  # 1

# Tuple does not allow assignment of items
# It is not MUTABLE


# Unpack Tuple
x, *y = (2, 0, 9)

print(y) # [0, 9] It unpacked into a list
print(x) # 2