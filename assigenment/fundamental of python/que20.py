# Write a Python function that takes a list of words and returns the length of the longest one.

list = ['priyanka','shimpi','krishna','pari','kiran']
lenght = 0

for words in list:
    if len(words) > lenght:
        lenght = len(words)
print(lenght)        
