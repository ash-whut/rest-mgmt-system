import os
import json
import pickle
from datetime import datetime

def add_order(order) -> None:
    with open("./records/orders_placed.dat", "rb+") as file:
        currSize = os.path.getsize("./records/orders_placed.dat")
        
        if (currSize == 0):
            record = json.loads("./records/orders_template.json")
            record["orders"].append(order)
            record["number_of_orders"] += 1

        else:
            record = pickle.load("./records/orders_placed.dat")
            record["orders"].append(order)
            record["number_of_orders"] += 1

def get_monthly_income(month: int) -> float:
    with open("./records/orders_placed.dat", "rb+") as file:
        currSize = os.path.getsize("./records/orders_placed.dat")
        
        if (currSize == 0):
            print("Orders haven't been placed yet. Please add at least one order and try again.")

        else:
            record = pickle.load("./records/orders_placed.dat")
            total_monthly_income = 0.0
            for order in record.orders:
                if order.get_month() == month:
                    total_monthly_income += order.get_total_cost()
            
            if total_monthly_income == 0:
                return -1
            
            else:
                return total_monthly_income
            
def get_income_today() -> float:
    with open("./records/orders_placed.dat", "rb+") as file:
        currSize = os.path.getsize("./records/orders_placed.dat")
        
        if (currSize == 0):
            print("Orders haven't been placed yet. Please add at least one order and try again.")

        else:
            record = pickle.load("./records/orders_placed.dat")
            total_daily_income = 0.0
            for order in record.orders:
                if order.get_day() == datetime.now().day:
                    total_daily_income += order.get_total_cost()
            
            if total_daily_income == 0:
                return -1
            
            else:
                return total_daily_income