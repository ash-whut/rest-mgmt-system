import os
import json
import pickle
from object_templates.menu_item import MenuItem
from helpers.sample_initializer import sample_initializer
from helpers.program_functions import displayMenu
from object_templates.order import Order
from helpers.dat_handler import add_order, get_income_today

while True:
    menu = sample_initializer()

    print("\nWelcome to XYZ Restaurant. Please enter the number corresponding to the action you would like to perform or type in anything else to exit\n")

    print("1 - Display Menu")
    print("2 - New Order")
    print("3 - Display Bill")
    print("4 - Total Income of the day")
    print("5 - Add new item to the menu")
    print("6 - Remove item from the menu")
    print("7 - Enter Feedback Score")
    print("8 - Average Customer Rating\n")

    choice = input("Please enter choice: ")

    if choice == "1":
        print()
        displayMenu(menu)
    
    elif choice == "2":
        ordering = True
        order = Order()

        while ordering:
            dish = input("Please enter name of the item from the menu (case sensitive) or say \'end\' to finish ordering: ")

            if dish == "end":
                ordering = False

                if order.number_of_items != 0:
                    order.display_current_order()
                    add_order(order)

            elif dish not in json.load(open("./records/sample_items.json", "r")).keys():
                print()
                print(f"{dish} is not available in our menu. Please make sure the item is:\n 1) In our menu\n 2) Matches the exact spelling as given in our menu (spelling is also case sensitive)")
                print()
                
            else:
                order.add_item(MenuItem(dish, json.load(open("./records/sample_items.json", "r"))[dish]))
                order.display_current_order()

    elif choice == "3":
        try:
            if (pickle.load(open("./records/orders_placed.dat", "rb"))["number_of_orders"] == 0):
                print()
                print("Order hasn't been started/created yet")
                print()            
            else:
                print()
                pickle.load(open("./records/orders_placed.dat", "rb"))["orders"][-1].display_current_order()
                print()
        except FileNotFoundError:
            print()
            print("Orders haven't been created yet. Please create at least one order and try again.")

    elif choice == "4":
        try:
            if (get_income_today() == 0):
                print()
                print("No Sales Today")

            else:
                print()
                print("Total Income today: ", get_income_today())
                print()

        except FileNotFoundError:
            print()
            print("Orders haven't been created yet. Please create at least one order and try again.")

    elif choice == "5":
        item_name = input("Please enter the name of the item you would like to add: ")
        price = float(input("Please enter the cost of the item you would like to enter: "))
        
        print()
        print("Old Menu")
        print()
        displayMenu(menu)
        print()
        print()

        with open("./records/sample_items.json", "r") as file:
            record = json.load(file)
            record[item_name] = price

        with open("./records/sample_items.json", "w") as file:
            json.dump(record, file)        

        menu = sample_initializer()

        print("New Menu")
        print()
        displayMenu(menu)
        print()

    elif choice == "6":
        item_name = input("Please enter the name of the item you would like to add: ")

        if (item_name not in json.load(open("./records/sample_items.json", "r")).keys()):
            print()
            print(f"{item_name} does not exist in the menu. Please make sure the item is:\n 1) In our menu\n 2) Matches the exact spelling as given in our menu (spelling is also case sensitive)")

        else:        
            print()
            print("Old Menu")
            print()
            displayMenu(menu)
            print()
            print()

            with open("./records/sample_items.json", "r") as file:
                record = json.load(file)
                del record[item_name]
                
            with open("./records/sample_items.json", "w") as file:
                json.dump(record, file)

            menu = sample_initializer()

            print("New Menu")
            print()
            displayMenu(menu)
            print()        
    
    elif choice == "7":
        rating = float(input("Please enter a value between 0-5 (inclusive): "))

        if ((rating >= 0) and (rating <= 5)):
            with open("./records/ratings.dat", "wb+") as file:
                currSize = os.path.getsize("./records/ratings.dat")
                if (currSize == 0):
                    data = {"total_rating": rating, "number_of_ratings": 1}
                    pickle.dump(data, file)

                else:
                    record = pickle.load(file)
                    record["total_rating"] = record["total_rating"] + rating
                    record["number_of_ratings"] += 1

        else:
            print("Rating needs to be a number between 0 and 5. Please try again with an appropriare value.") 

    elif choice == "8":
        try:
            with open("./records/ratings.dat", "rb") as file:
                currSize = os.path.getsize("./records/ratings.dat")
                if (currSize == 0):
                    print("Ratings have not been entered yet.")
                    print()

                else:
                    record = pickle.load(file)
                    print("Average Rating: ", record["total_rating"] / record["number_of_ratings"])     
                    print()
        except FileNotFoundError:
            print()
            print("Ratings have not been provided yet. Please rate the restaurant at least once and try again.")

    else:
        exit()