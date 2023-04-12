import json
from json.decoder import JSONDecodeError

# ---------------------------ADD FOOD ITEMS------------------------>>>
def add_food(filename, food_name, quantity, price, discount, stock):
    
    food = {}
    food_ID = len(food) + 1
    food_items = {'Food_Name' : food_name,
                  'Quantity' : quantity,
                  'Price': price,
                  'Discount' : discount,
                  'Stock': stock}
    
    try:
        file = open('FoodData.json', 'r+')
        data = json.load(file)
        food_ID = len(data) + 1
        food[food_ID] = food_items
        data.update(food)
            
    except json.decoder.JSONDecodeError:
        data = {}
        food[food_ID] = food_items
        data.append(food)
    file.seek(0)
    file.truncate()
    json.dump(data, file, indent=4)
    file.close()
    return 'Success'
        
        
# -------------------------EDIT FOOD----------------------->>>  
def edit_food(filename, food_ID):
    
    with open('FoodData.json') as file:
        content = json.load(file)
        if food_ID in content.keys():
            print("What you want to update in food item??")
            print("1) Food name")
            print("2) Food Quantity")
            print("3) Food price")
            print("4) Discount on food")
            print("5) Stock availability")

            y = input('Enter your choice : ')
            if y == "1":
                content[food_ID]["Food_Name"] = input('Enter Updated name :')
                print("\n Updated Successfully \n")
            elif y == "2":
                content[food_ID]["Quantity"] = input('Enter Updated quantity :')
                print("\n Updated Successfully \n")
            elif y == "3":
                content[food_ID]["Price"] = input('Enter Updated price :')
                print("\n Updated Successfully \n")
            elif y == "4":
                content[food_ID]["Discount"] = input('Enter Updated discount value :')
                print("\n Updated Successfully \n")
            elif y == "5":
                content[food_ID]["Stock"] = input('Enter Updated stock :')
                print("\n Updated Successfully \n")
            else:
                print('Invalid selection')
        else:
            print('Invalid Food ID') 
    file = open(filename, 'w')
    json.dump(content, file, indent=4)
    file.close()
    return 'Success'
    

#------------------------------REMOVE FOOD ITEM-------------------->>>
def remove_food(filename , id):
    file = open(filename, 'r+')
    data = json.load(file)
    
    for i in data:
        if i == id:
            del data[id]
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)
            file.close()
            return 'Success'
    return 'Please enter valid food ID'



#------------------------SHOW FOOD--------------------->>>
def show_food(filename):
    try:
        file = open('FoodData.json')
        content = json.load(file)
        print("-------------Menu------------")
    
        for i in content:
            print(f'Food ID : {i}')
            print(f"Food Name : {content[i]['Food_Name']}")
            print(f"Quantity : {content[i]['Quantity']}")
            print(f"Price : {content[i]['Price']}")
            print(f"Discount : {content[i]['Discount']}")
            print(f"Stock : {content[i]['Stock']}")
            print('----------------------------------------')
        file.close()
        return True
    except json.JSONDecodeError:
        content = {}
        return 'No food available'
