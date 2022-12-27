menuList = []
priceList = []

def showBill():
    print("-----------------")
    print("     My Food     ")
    print("-----------------")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
def totalBill():
    total = 0
    for price in priceList:
        total = total + int(price)
    print("-----------------")
    print("Total is %d THB" %(total))
    print("-----------------")
    print("    Thank you    ")
print("If you want to exit, please enter %s" %("exit."))
while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please Enter Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
totalBill()