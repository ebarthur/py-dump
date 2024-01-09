# Write a function to reverse the string
# The input string is given as an array of s
def reverse(s):
    l = 0
    r = len(s) - 1
    
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
        
    return s

print(reverse(['B','R','Y','A','N']))