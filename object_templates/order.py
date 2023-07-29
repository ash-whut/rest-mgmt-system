from object_templates.menu_item import MenuItem
from datetime import datetime
from helpers.program_functions import displayMenu

class Order:
    def __init__(self) -> None:
        self.number_of_items = 0
        self.total_cost = 0.0
        self.items = []
        self.timestamp = datetime.now()

    def add_item(self, item: MenuItem) -> None:
        self.number_of_items += 1
        self.total_cost += item.get_price()
        self.items.append(item)

    def display_current_order(self):
        print()
        displayMenu(self.items)
        print()
        print("Total Cost: $", self.total_cost, space = "", end = "\n")
        
    def get_month(self) -> int:
        return self.timestamp.month
    
    def get_day(self):
        return self.timestamp.day
    
    def get_total_cost(self) -> float:
        return self.total_cost

    def get_number_of_items(self) -> int:
        return self.get_number_of_items