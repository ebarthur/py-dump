# Python set is a collection which is unordered and not mutable.
# It does not allow duplicate members
fruits = {'Mango', 'Banana', 'Apple'}

# It is not mutable so you can't do fruits[0] = 'Guava'
print(fruits) # {'Banana', 'Apple', 'Mango'} there is no order so you can't assign index to sets.
print(type(fruits)) # <class 'set'>

vegetables = ['Cucumber', 'Carrot', 'Cabbage'] # This is a list
# Let's do some typecasting
new_vegetables = set(vegetables)
print(new_vegetables) # {'Carrot', 'Cucumber', 'Cabbage'}
print(type(new_vegetables)) # <class 'set'>

old_vegetables = tuple(new_vegetables)
print(old_vegetables) # ('Carrot', 'Cucumber', 'Cabbage')
print(type(old_vegetables)) # <class 'tuple'>

# Union and Intersection
first_score = {30, 40, 50}
second_score = {20, 70, 80} 

print(first_score.intersection(second_score)) # set()
print(first_score & second_score) # set() This is also intersection

print(first_score.union(second_score)) # {80, 50, 20, 70, 40, 30}
print(first_score | second_score) # {80, 50, 20, 70, 40, 30} This is also union

# Difference
print(first_score.difference(second_score)) # {40, 50, 30}
# This prints out every element in the first set that is not in the second set 

print(second_score.difference(first_score)) # {80, 20, 70}
# This prints out every element in the second_score set that is not in the first_score set

first_score.add(10)
print(first_score)