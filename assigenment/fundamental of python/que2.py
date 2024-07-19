#  Write a Python program to get the Factorial number of given number.

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

num = int(input("Enter a non-negative number: "))
if num < 0:
  print("Factorial is not defined for negative numbers.")
else:
  print("Factorial of", num, "is", factorial(num))

