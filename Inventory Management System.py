'''Mahdy 240101411: file - low stock = inventory
Mahmoud Esmat 240103284: search - sell
Mahmoud Hany: 240101818 add item - user auth.'''

import json, getpass, os

def users_data():
    with open("Admin_Users.json", "r") as file:
        admin_users =json.load(file)
    
    with open("Users.json", "r") as file:
        users =json.load(file)
    
    return admin_users,users 

admin_users,users = users_data()

def load_inventory():
    with open("Storage.json", "r") as file:
        items = json.load(file)
        return items
    
items = load_inventory()

def save_inventory(items):
    with open("Storage.json", "w") as file:
        json.dump(items, file, indent=2)

def save_users(admin_users, users):
    with open("Admin_Users.json", "w") as file:
        json.dump(admin_users, file, indent=2)
    
    with open("Users.json", "w") as file:
        json.dump(users, file, indent=2)

def manage_users(admin_users, users):
    UserServ = input("1. Normal user\n2. Admin user\n3. Return back to the main list\nEnter choice (1-3): ")
    
    while not UserServ.isdigit() or int(UserServ) not in [1, 2, 3]:
        UserServ = input("Invalid choice! Please enter a valid option (1-3): ")
    UserServ = int(UserServ)

    if UserServ == 1:
        os.system('cls')
        Nuser = input("1. Show users\n2. Add user\n3. Delete user\nEnter choice (1-3): ")

        while not Nuser.isdigit() or int(Nuser) not in [1, 2, 3]:
            Nuser = input("Invalid choice! Please enter a valid option (1-3): ")
        Nuser = int(Nuser)

        if Nuser == 1:
            os.system('cls')
            found = False
            for user_name, user_details in users.items():
                print(f"User found: {user_name}\npassword: {user_details['pass']}")
                found = True
            if not found:
                print("List is empty.")

        elif Nuser == 2:
            os.system('cls')
            new_user = input("Enter username: ")
            os.system('cls')
            if new_user not in users:
                new_pass = input("Enter password: ")
                new_name = input("Enter user name: ")
                os.system('cls')
                users[new_user] = {"pass": new_pass, "name": new_name}
                print(f"User {new_user} added successfully")
            else:
                print(f"User {new_user} is already in users")

        elif Nuser == 3:
            os.system('cls')
            del_Nuser = input("Enter username: ")
            os.system('cls')
            if del_Nuser in users:
                confirm = input(f"Are you sure you want to delete user {del_Nuser}? (yes/no): ")
                os.system('cls')
                if confirm.lower() == 'yes':
                    users.pop(del_Nuser)
                    print(f"User {del_Nuser} deleted successfully")
                else:
                    print("User deletion canceled.")
            else:
                print(f"User {del_Nuser} not found.")

    elif UserServ == 2:
        os.system('cls')
        Auser = input("1. Show users\n2. Add user\n3. Delete user\nEnter choice (1-3): ")

        while not Auser.isdigit() or int(Auser) not in [1, 2, 3]:
            Auser = input("Invalid choice! Please enter a valid option (1-3): ")
        Auser = int(Auser)

        if Auser == 1:
            os.system('cls')
            found = False
            for user_name, user_details in admin_users.items():
                print(f"Admin user found: {user_name}\npassword: {user_details['pass']}")
                found = True
            if not found:
                print("List is empty.")

        elif Auser == 2:
            os.system('cls')
            new_user = input("Enter username: ")
            os.system('cls')
            if new_user not in admin_users:
                new_pass = input("Enter password: ")
                new_name = input("Enter user name: ")
                os.system('cls')
                admin_users[new_user] = {"pass": new_pass, "name": new_name}
                print(f"Admin user {new_user} added successfully")
            else:
                print(f"Admin user {new_user} is already in users")

        elif Auser == 3:
            os.system('cls')
            del_Auser = input("Enter username: ")
            os.system('cls')
            if del_Auser in admin_users:
                confirm = input(f"Are you sure you want to delete admin {del_Auser}? (yes/no): ")
                os.system('cls')
                if confirm.lower() == 'yes':
                    admin_users.pop(del_Auser)
                    print(f"Admin user {del_Auser} deleted successfully")
                else:
                    print("Admin deletion canceled.")
            else:
                print(f"Admin user {del_Auser} not found.")

    else:
        os.system('cls')
    return admin_users, users


def admin_service(items):
    while True:
        serv = input(f"Welcome {admin_users[user_name]["name"]}\n1. Add item\n2. Search\n3. Show the inventory\n4. Sell\n5. Show low stock\n6. Manage users\n7. Exit\nEnter choice (1-7): ")
            
        while not serv.isdigit() or int(serv) not in [1, 2, 3, 4, 5, 6, 7]:
            serv = input("Invalid choice! Please enter a valid option (1-7): ")
        serv = int(serv)
            
        if serv == 1:
            os.system('cls')
            item_name = input("Enter the name of the item: ").lower()

            if item_name not in items:
                New_item_price = float(input("Enter item price: "))
                New_item_quantity = int(input("Enter item quantity: "))
                New_item_company = input("Enter item company: ").lower()
                    
                items[item_name] = {"price": New_item_price, "quantity": New_item_quantity, "company": New_item_company}
                os.system('cls')
                print(f"Item {item_name} added successfully.")
                    
            else:
                os.system('cls')
                update_serv = input("1. Change item price\n2. Add quantity\n3. Change company name\n4. Delete the item\n5. Return back to the main list\nEnter choice (1-4): ")
                        
                while not update_serv.isdigit() or int(update_serv) not in [1, 2, 3, 4, 5]:
                    update_serv = input("Invalid choice! Please enter a valid option (1-5): ")
                update_serv = int(update_serv)

                if update_serv == 1:
                    os.system('cls')
                    Change_item_price = float(input("Enter new item price: "))
                    items[item_name]["price"] = Change_item_price
                    print("Price changed successfully.")
                        
                elif update_serv == 2:
                    os.system('cls')
                    Add_item_quantity = int(input("Enter additional item quantity: "))
                    items[item_name]["quantity"] += Add_item_quantity
                    print("Quantity added successfully.")

                elif update_serv == 3:

                    Change_item_company = (input("Enter new company name: "))
                    items[item_name]["company"] = Change_item_company
                    print("Company changed successfully.")

                elif update_serv == 4:
                    os.system('cls')
                    confirm = input(f"Are you sure you want to delete item {item_name}? (yes/no): ")
                    os.system('cls')
                    if confirm.lower() == 'yes':
                        items.pop(item_name)
                        print(f"item {item_name} deleted successfully")
                    else:
                        print("Item deletion canceled.")

                elif update_serv == 5:
                    os.system('cls')
                    continue
                       
        elif serv == 2:
            os.system('cls')
            search_serv = input("What is the filter you want to search by\n1. Item name\n2. Company name\n3. Quantity\n4. Return back to the main list\nEnter choice (1-4): ")

            while not search_serv.isdigit() or int(search_serv) not in [1, 2, 3, 4]:
                search_serv = input("Invalid choice! Please enter a valid option (1-4): ")
            search_serv = int(search_serv)

            if search_serv == 1:
                os.system('cls')
                Search_item_name = input("Enter the name of the item: ").lower()
                os.system('cls')
                if Search_item_name in items:
                    print(f"Item found\nItem: {Search_item_name} - Price: {items[Search_item_name]['price']} - Quantity: {items[Search_item_name]['quantity']} - Company: {items[Search_item_name]['company']}")
                else:
                    print("Item not found.")
                    continue

            elif search_serv == 2:
                os.system('cls')
                search_company = input("Enter the company name: ").lower()
                os.system('cls')
                found = False
                print(f"Items from company {search_company}:")
                for item_name, item_details in items.items():
                    if "company" in item_details and search_company == item_details["company"].lower():
                        print(f"Item found: {item_name} - Price: {item_details['price']} - Quantity: {item_details['quantity']} - Company: {item_details['company']}")
                        found = True       

                if not found:
                    print("Item not found.")

            elif search_serv == 3:
                os.system('cls')
                search_quantity = input("Enter the quantity: ")
                while not search_quantity.isdigit():
                    search_quantity = input("Please enter a valid quantity (number): ")
                search_quantity = int(search_quantity)
                os.system('cls')
                found = False
                print(f"Items with quantity {search_quantity}:")
                for item_name, item_details in items.items():
                    if "quantity" in item_details and item_details["quantity"] == search_quantity:
                        price = item_details.get("price", "N/A")
                        company = item_details.get("company", "Unknown")

                        print(f"Item: {item_name} - Price: {price} - Quantity: {item_details['quantity']} - Company: {company}")
                        found = True

                if not found:
                    print(f"No items found with {search_quantity} quantity.")
                    continue
                    
            
            elif search_serv ==4 :
                os.system('cls')
                continue 

        elif serv == 3:
            os.system('cls')
            print("The inventory:")
            found = False
            for item_name, item_details in items.items():
                print(f"Item found: {item_name} - Price: {item_details['price']} - Quantity: {item_details['quantity']} - Company: {item_details['company']}")
                found = True
            if not found:
                print("Inventory is empty.")
                
        elif serv == 4:
                os.system('cls')
                item_name = input("Enter the name of the item: ").lower()
                    
                if item_name in items:
                    Remove_item_quantity = int(input("Enter sold item quantity: "))
                    if Remove_item_quantity > 0:
                
                        if Remove_item_quantity <= items[item_name]["quantity"]:
                            items[item_name]["quantity"] -= Remove_item_quantity
                            Total = items[item_name]["price"] * Remove_item_quantity
                            print("Total:", Total)
                            cus = float(input("Enter customer money: "))
                            if cus >= Total:
                                remaining = cus - Total
                                os.system('cls')
                                print(f"Remaining: {remaining}\nItem sold successfully.")
                                print(f"The remaining quantity of {item_name} is {items[item_name]["quantity"]}")

                                if items[item_name]["quantity"] <= 5:
                                    print(f"There is low stock of:\nItem: {item_name} - Price: {items[item_name]['price']} - Quantity: {items[item_name]['quantity']} - Company: {items[item_name]['company']}")
                                
                            else:
                                os.system('cls')
                                print("customer money not enough")
                            
                        else:
                            os.system('cls')
                            print("Stock not enough.")

                    else:
                        os.system('cls')
                        print("Invalid quantity")

                else:
                    os.system('cls')
                    print("Item not found.")
                    continue
                    
        elif serv == 5:
            os.system('cls')
            found = False
            print("There is low stock of:")
            for item_name, item_details in items.items():
                if "quantity" in item_details and item_details["quantity"] <= 5:
                    price = item_details.get("price", "N/A")
                    company = item_details.get("company", "Unknown")
                    print(f"Item: {item_name} - Price: {price} - Quantity: {item_details['quantity']} - Company: {company}")
                    found = True

            if not found:
                os.system('cls')
                print("The stock is good")
                continue

        elif serv == 6:
            os.system('cls')
            manage_users(admin_users, users)
            save_users(admin_users, users)

        elif serv == 7:
            os.system('cls')
            save_inventory(items)
            print("Exit successfully.")
            break


def user_service(items):
    while True:
        serv = input(f"Welcome {users[user_name]["name"]}\n1. Search\n2. Sell\n3. Exit\nEnter choice (1-3): ")
            
        while not serv.isdigit() or int(serv) not in [1, 2, 3]:
            serv = input("Invalid choice! Please enter a valid option (1-3): ")
        serv = int(serv)

        if serv == 1:
            os.system('cls')
            search_serv = input("What is the filter you want to search by\n1. Item name\n2. Company name\n3. Return back to the main list\nEnter choice (1-3): ")

            while not search_serv.isdigit() or int(search_serv) not in [1, 2, 3]:
                search_serv = input("Invalid choice! Please enter a valid option (1-3): ")
            search_serv = int(search_serv)

            if search_serv == 1:
                os.system('cls')
                Search_item_name = input("Enter the name of the item: ").lower()
                os.system('cls')
                if Search_item_name in items:
                    print(f"Item found:\nItem: {Search_item_name} - Price: {items[Search_item_name]['price']} - Quantity: {items[Search_item_name]['quantity']} - Company: {items[Search_item_name]['company']}")
                else:
                    print("Item not found.")
                    continue

            elif search_serv == 2:
                os.system('cls')
                search_company = input("Enter the company name: ").lower()
                os.system('cls')
                found = False
                print(f"Items from company {search_company}:")
                for item_name, item_details in items.items():
                    if "company" in item_details and search_company == item_details["company"].lower():
                        print(f"Item found: {item_name} - Price: {item_details['price']} - Quantity: {item_details['quantity']} - Company: {item_details['company']}")
                        found = True       

                if not found:
                    print("Item not found.")

        elif serv == 2:
                os.system('cls')
                item_name = input("Enter the name of the item: ").lower()
                    
                if item_name in items:
                    Remove_item_quantity = int(input("Enter sold item quantity: "))
                    if Remove_item_quantity > 0:
                        if Remove_item_quantity <= items[item_name]["quantity"]:
                            items[item_name]["quantity"] -= Remove_item_quantity
                            Total = items[item_name]["price"] * Remove_item_quantity
                            print("Total:", Total)
                            cus = float(input("Enter customer money: "))
                            if cus >= Total:
                                os.system('cls')
                                remaining = cus - Total
                                print(f"Remaining: {remaining}\nItem sold successfully.")

                                if items[item_name]["quantity"] <= 5:
                                    os.system('cls')
                                    print(f"There is low stock of:\nItem: {item_name} - Price: {items[item_name]['price']} - Quantity: {items[item_name]['quantity']} - Company: {items[item_name]['company']}")
  
                            else:
                                os.system('cls')
                                print("customer money not enough")
                            
                        else:
                            os.system('cls')
                            print("Stock not enough.")

                    else:
                        os.system('cls')
                        print("Invalid quantity")
                        
                else:
                    os.system('cls')
                    print("Item not found.")
                    continue

        elif serv == 3:
            os.system('cls')
            save_inventory(items)                    
            print("Exit successfully.")
            break

while True:
    user_name = input("Enter your username: ")
    # password = input("Enter your password: ")
    password = getpass.getpass("Enter your password: ")

    if user_name in admin_users and password == admin_users[user_name]["pass"]:
        os.system('cls')
        admin_service(items)
        break

    elif user_name in users and password == users[user_name]["pass"]:
        os.system('cls')
        user_service(items)
        break

    else:
        os.system('cls')
        print("Invalid username or password")