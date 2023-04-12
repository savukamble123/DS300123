import json
from Admin import *
from Customer import *
while True:
    print("1 : Admin Login")
    print("2 : User Login")
    print("3 : Exit")

    val = input("Enter Your Selction : ")

# ------------------------------------------Admin Login----------------------------------------------
    if val == "1":
        fp = open("adminLogin.json",'r+')
        content = json.load(fp)
        username = input("Enter Username : ")
        password = input("Enter Password : ")
        if content["username"] == username and content["password"] == password:
            while True:
                print("---------------------ADMIN VIEW DATA-----------------------")
                print("1 : Add food items")
                print("2 : Edit food items")
                print("3 : View food list")
                print("4 : Remove food item")
                print("5 : Logout as admin")

                val2 = input("Enter your selection : ")
                if val2 == "1":
                    food_name = input("Enter food name : ")
                    quantity = input("Enter quantity : ")
                    price = float(input("Enter food price : "))
                    discount = float(input("Enter discount value : "))
                    stock = int(input("Enter stock availability : "))
                    add_food("FoodData.json", food_name, quantity, price, discount, stock)
                    print(f"Food named {food_name} added successfully")
                elif val2 == "2":
                    food_ID = input("Enter food ID : ")
                    edit_food("FoodData.json", food_ID)
                    print(f"Food ID {food_ID} updated successfully\n")
                elif val2 == "3":
                    show_food("FoodData.json")
                elif val2 == "4":
                    id = input("Enter the Food ID to remove data : ")
                    remove_food('FoodData.json' , id)
                    print(f"Food ID {id} data removed successfully\n")
                elif val2 == "5":
                    print("-------------------Admin Logout Successfully !!!------------------------\n")
                    break
                    
                else:
                    print("------Invalid selection!!!-----\n")
        else:
            print("--------Wrong Username and Password-----------\n")
        fp.close()

# --------------------------USER LOGIN PAGE-----------------------------

    elif val == "2":
        print("\n1 : Register Here")
        print("2 : Login Here")
        print("3 : Exit The page\n")

        val3 = input("Enter your choice : ")

        if val3 == "1":
            username = input("Enter fullname : ")
            email = input("Enter email ID : ")
            password = input("Enter password : ")
            address = input("Enter address : ")
            phn_number = int(input("Enter Phone number : "))
            register_user("CustomerData.json", username, email, password, address, phn_number)
            print(f"User registered successfully!!")
        elif val3 == "2":
            email = input("Enter user email ID : ")
            password = input("Enter user password : ")
            file = open("CustomerData.json", 'r+')
            content = json.load(file)

            for i in range(len(content)):
                if content[i]['Email'] == email and content[i]["Password"] == password:
                    while True:
                        print(f"\n----------------Welcome to our shop  {content[i]['Full_name']}----------------------")
                        print("1 : Place order")
                        print("2 : Order History")
                        print("3 : Update profile")
                        print("4 : Logout")

                        val4 = input("Enter your choice : ")

                        if val4 == "1":
                            place_order("FoodData.json", "CustomerData.json")
                        elif val4 == "2":
                            order_history('CustomerData.json', email)
                        elif val4 == "3":
                            update_user_profile('CustomerData.json')
                        elif val4 == "4":
                            print("User logout successfully\n")
                            break

                        else:
                            print("Invalid selection\n")
                else:
                    print("Worng username and password!!!\n")
        elif val3 == "3":
            break
        else:
            print("Invalid selection!!!\n")

    elif val == "3":
        print("Visit again!!!!!")
        break

                