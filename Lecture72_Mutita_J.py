menuList = []

def showBill():
    print("-----------------")
    print("     My Food     ")
    print("-----------------")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
def totalBill():
    total = 0
    for number in range(len(menuList)):
        total = total + menuList[number][1]
    print("-----------------")
    print("Total is %d THB" % (total))
    print("-----------------")
    print("    Thank you    ")
while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName, int(menuPrice)])

showBill()
totalBill()