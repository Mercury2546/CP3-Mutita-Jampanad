def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
        userSelected = menuSelect()
        if userSelected == 1:
            totalPrice = float(input("Please Enter Price of Product : "))
            print("Price(Vat7%) =", vatCalculator(totalPrice), "THB")
        elif userSelected == 2:
            print("Price(Vat7%) =", priceCalculator(), "THB")
        else:
            print("Wrong Choice!")
    else:
        print("Incorrect!")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()