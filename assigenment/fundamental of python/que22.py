#Write a Python program to get a string made of the first 2 and the last
#2 chars from a given a string. If the string length is less than 2, return
#instead of the empty string

def string_both_ends(s):
    if len(s) < 2:
        return ''
    return s[0:2] + s[-2:]

print(string_both_ends('w3resource'))  
print(string_both_ends('w3')) 
print(string_both_ends('w')) 
