# Write a funciton to print out the factorials of a number

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)



print(factorial(5)) #120