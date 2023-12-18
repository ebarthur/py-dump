# class BakingPan:
#     def myFunction():
#         print('This is my baking pan function')

# bread1 = BakingPan()

# BakingPan.myFunction() # This is my baking pan function

class BakingPan:
    def __init__(self, flour, sugar, special_ingredient):
        self.flour = flour
        self.sugar = sugar
        self.special_ingredient = special_ingredient
        
bread1 = BakingPan('Soft', 20, 'Wheat')
bread2 = BakingPan('Hard', 10, 'Banana')

print(bread1.sugar) # 20
print(bread1.flour) # Soft
print(bread1.special_ingredient) # Wheat
    
print(bread2.special_ingredient) # Banana