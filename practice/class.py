# class BakingPan:
#     def myFunction():
#         print('This is my baking pan function')

# bread1 = BakingPan()

# BakingPan.myFunction() # This is my baking pan function

class BakingPan:
    unit_price = 5
    def __init__(self, flour, sugar, special_ingredient):
        self.flour = flour
        self.sugar = sugar
        self.special_ingredient = special_ingredient
        
    def bread_name(self):
            return f'{self.unit_price} pieces of {self.special_ingredient} bread'
        
        
    def total_price(self, quantity):
        total = quantity * self.unit_price
        return f'Total Price of {self.unit_price} pieces of {self.special_ingredient} bread = GHC {total}'
    
bread1 = BakingPan('Soft', 20, 'Wheat') 
bread2 = BakingPan('Hard', 10, 'Banana')

print(bread1.sugar) # 20
print(bread1.flour) # Soft
print(bread1.special_ingredient) # Wheat
    
print(bread2.special_ingredient) # Banana
print(bread1.bread_name()) # 5 pieces of Wheat bread
print(bread2.bread_name()) # 5 pieces of Banana bread

print(bread1.total_price(16)) # Total Price of 5 pieces of Wheat bread = GHC 80
