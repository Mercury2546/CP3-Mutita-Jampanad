price = int(input("Please Enter Your Price : "))
def vatCalculate(totalPrice):
    result = price + (price*7/100)
    return result

print(vatCalculate(price))