# Create a New Year's countdown

# 5
# 4
# 3
# 2
# 1
# Happy New Year!
import time

def newYearCountDown(seconds):
    for second in range(seconds, 0, -1):
        print(second)
        time.sleep(1)
    print("Happy New Year!")
        
newYearCountDown(5)