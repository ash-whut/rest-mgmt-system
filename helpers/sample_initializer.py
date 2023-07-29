import json
from object_templates.menu_item import MenuItem

def sample_initializer(path = "./records/sample_items.json") -> list:
    with open(path, "r") as read_content:
        init_dict = json.load(read_content)
        array_of_items = []

        for key in init_dict.keys():
            item_name = key
            item_price = init_dict[key]
            item = MenuItem(item_name, item_price)
            array_of_items.append(item)

        return array_of_items