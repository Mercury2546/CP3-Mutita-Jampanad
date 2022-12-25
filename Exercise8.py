userName = input("Username : ")
passWord = input("Password : ")
if userName == "admin" and passWord == "1234":
    print("Successfully Logged in.")

    def menu():
        print("-----------------------------")
        print("         SUPERMARKET         ")
        print("-----------------------------")
        print(" [1] Apple           20THB   ")
        print(" [2] Banana          30THB   ")
        print(" [3] Bottle of Water 15THB   ")
        print(" [4] Grape           45THB   ")
        print(" [5] Cake            56THB   ")
        print("-----------------------------")

        def result(total):
            print("-----------------------------")
            print("Total is", total, "THB")
            print("-----------------------------")
            print("        Thank You :D         ")

        choice = int(input("Please Enter Your Choice : "))
        if choice == 1:
            quantity = int(input("Please Enter the quantity : "))
            price = quantity * 20
            result(price)

        elif choice == 2:
            quantity = int(input("Please Enter the quantity : "))
            price = quantity * 30
            result(price)

        elif choice == 3:
            quantity = int(input("Please Enter the quantity : "))
            price = quantity * 15
            result(price)

        elif choice == 4:
            quantity = int(input("Please Enter the quantity : "))
            price = quantity * 45
            result(price)

        elif choice == 5:
            quantity = int(input("Please Enter the quantity : "))
            price = quantity * 56
            result(price)

        else:
            print("Wrong Choice! ")
    menu()
else:
    print("Wrong Password!")



