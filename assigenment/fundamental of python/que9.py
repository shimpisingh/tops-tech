#  Write a Python program to sum of three given integers. However, iftwo values are equal sum will be zero.


def sum_three(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c

