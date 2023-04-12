import json


def register_user(user_file, username, email, password, address, phn_number):
    """
    Register page only for new customer in the shop
    first customer have to register themselves after that they can  login 
    and purchase the food from the shop
    """
    
    user = {'Full_name': username, 
           'Email': email, 
           'Password' : password,
           'Address': address,
           'Phone Number' : phn_number,
           'Order History' : []
           }
    try:
        file = open("CustomerData.json", 'r+')
        content = json.load(file)
        for i in range(len(content)):
            if content[i]['Email'] == email:
                return 'User already exists'
            
            else:
                content.append(user)
    except json.decoder.JSONDecodeError:
        content = []
        content.append(user)
        
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    return 'Registered successfully!'
    

def place_order(foodfile, Userfile):
    """
    User can place the order and the data store in the order history section 
    """
    file = open("FoodData.json", 'r+')
    content = json.load(file)
    if len(content) != 0:
        menu = []
        for items in content:
            menu.append([items, content[items]['Food_Name'], content[items]['Quantity'], content[items]['Price']])
        for menu_list in menu:
            print(menu_list)
            
        while True:
            with open("CustomerData.json") as file1:
                content1 = json.load(file1)
                
            for i in content1:
                print("Enter 1 to place order \nEnter 2 to Exit")
                x = input('Enter your choice : ')
                if x == '1':
                    print('Enter the food ID you want to ordered separated by the comma')
                    y = input().split(",")
                    for j in y:
                        z = int(j)
                        if z <= len(menu):
                            i['Order History'].append(menu[z-1])
                        else:
                            print("We don't have this food item")
                    print('List of food you selected : \n')
                    for k in i['Order History']:
                        print(k)

                
            file1 = open("CustomerData.json", 'w')
            json.dump(content1, file1, indent=4)
            file1.close()
            break
        
    else:
        print("Sorry! no food available")

    file.close()
    return "Success"
            
# place_order("FoodData.json", "CustomerData.json")

def order_history(filename, email):
    """
    whichever food  is placed by customer the whole data store in this section 
    so he can view his history
    """
    file = open("CustomerData.json", 'r+')
    content = json.load(file)
    Total_Bill = 0
    for i in content:
        if i["Email"] == email:
            if len(i["Order History"]) != 0:
                print("------------ORDER HISTORY------------\n")
                print(i["Order History"] ,"\n")
                print("Total bill of Food  = " , (i["Order History"][0][3]) + (i["Order History"][1][3]) )
            else:
                print(f"You haven't ordered yet")
            return True
    file.close()
    return False
        
# order_history("CustomerData.json", "savita@gmail.com")

def update_user_profile(filename):
    """
    Customer can update his data like name , phone number 
    """
    file = open("CustomerData.json", 'r+')
    content = json.load(file)
    
    for i in content:
        print('What you want to update??')
        print("1) Update Name")
        print("2) Update password")
        print("3) Update address")
        print("4) Update Phone number")
        print("5) Exit")
        val = input('Enter your choice : ')
        
        if val == "1":
            i["Full_name"] = input('Enter updated name : ')
            print("Updated successfully")
        elif val == "2":
            i["Password"] = input("Enter updated password : ")
        elif val == "3":
            i["Address"] = input("Enter new address : ")
        elif val == "4":
            i["Phone Number"] = input("Enter new phone number : ")
        else:
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return True
