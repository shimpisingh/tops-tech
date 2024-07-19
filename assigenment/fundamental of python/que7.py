#Write a Python program to find whether a given number is even or odd,
#print out an appropriate message to the user
# Taking user input
# Calculate the remainder when the number is divided by 2
num = int(input("Enter a number: "))

if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))
