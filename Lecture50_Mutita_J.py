def addNumber(x, y):
    print(x, "+", y, "=", x+y)

def minusNumber(x, y):
    print(x, "-", y, "=", x-y)

def multiplyNumber(x, y):
    print(x, "x", y, "=", x*y)

def divideNumber(x, y):
    print(x, "/", y, "=", x/y)

number1 = int(input("First Number : "))
number2 = int(input("Second Number : "))

addNumber(number1, number2)
minusNumber(number1, number2)
multiplyNumber(number1, number2)
divideNumber(number1, number2)