"""Codes for calculating a factorial of a number"""

def calcFactorial(num):
    if num == 1:
        return 1
    else:
        return num * calcFactorial(num - 1)
