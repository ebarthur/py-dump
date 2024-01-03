# A class is a blue-print for creating objects.
class bakingPan:
    pass

bread1 = bakingPan()
# flour, sugar, special_ingredient
bread1.flour = 'Soft'
bread1.sugar = 20
bread1.special_ingredient = 'wheat'

print(bread1.flour) # Soft
print(bread1.sugar) # 20

#----------------------------

bread2 = bakingPan()
bread2.flour = 'Hard'
bread2.sugar = 10
bread2.special_ingredient = 'coconut'

print(bread2.flour) # Hard
print(bread2.sugar) # 10
