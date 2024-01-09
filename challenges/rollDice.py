# Write a function to return a random number from 1 to 6
import random

def rollDice():
    dice = [1, 2, 3, 4, 5, 6]
    numberOfShuffles = 100
    for _ in range(numberOfShuffles):
        random.shuffle(dice)
        
    return dice[0]

print(rollDice())
print(rollDice())
print(rollDice())
print(rollDice())
print(rollDice())