# Write a Python program to get a single string from two given strings, separated by a space and swap
# the first two characters of each string. 

string1 = input("Enter string1 : ")
string2 = input("Enter string2 : ")

str1_swap = string1[:3] + string2[3:]
str2_swap = string2[:3] + string1[3:]

result = str1_swap + " " + str3_swap
print(result)
