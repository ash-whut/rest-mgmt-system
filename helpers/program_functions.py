from prettytable import PrettyTable

def displayMenu(menu: list) -> None:
    menu_disp = PrettyTable()
    menu_disp.field_names = ["Serial Number", "Item Name", "Price"]
    count = 1

    for item in menu:
        menu_disp.add_row([count, item.get_name(), item.get_price()])
        count += 1
    
    print(menu_disp) 