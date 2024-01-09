# Given a number n
# Iterate from 1 to n

# If the current value is divisible by 3, print 'fizz' 
# If the current value is divisible by 5, print 'Buzz'
# If the current value is divisible by 3 & 5, print 'FizzBuzz'

def fizzBuzz(n):
    for i in range(1,n):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        # else:
        #     print("Number is not divisible by neither 3 nor 5")
            

fizzBuzz(20)