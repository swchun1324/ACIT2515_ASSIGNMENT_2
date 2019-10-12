from abstract_menu_item import AbstractMenuItem
from menu_item_stats import MenuItemStats
from food import Food
from drink import Drink

class MenuItemManager:
    """ creates menu item manager """    
    def __init__(self, restaurant_name):
        self._restaurant_name= restaurant_name
        self._menu = []

    def add_menu_item(self, menu_item):
        """adds a menu item to the menu list"""   
        self._menu.append(menu_item)

    
    def get_by_id(self, id):
        for menu_item in self._menu:
            if menu_item.get_id() == id:
                return menu_item
    
    def get_all_by_type(self):
        menu_list = []
        for menu_item in self._menu:
            if menu_item.get_type() == type:
                menu_list.append(menu_item.menu_item_description())
        return menu_list                

        

    def get_all(self):

        menu_list = []
        for menu_item in self._menu:
            menu_list.append(menu_item)

        return menu_list 
                
                
    

    def update(self, menu_item):
        pass
    

    def remove_menu_item_by_id(self, menu_item):
        if menu_item in self._menu:
            if menu_item.get_id() == id:
                self._menu.remove(menu_item)


    def get_menu_item_stats(self):

        """ gets menu item stats """
        total_num_menu_items = int(0)
        num_foods = int(0)
        num_drinks = int(0)

        for menu_item in self._menu:
            total_num_menu_items += 1
            if menu_item.get_type() == "food":
                num_foods += 1
            if menu_item.get_type() == "drink":
                num_drinks += 1

        for menu_item in self._menu:
            price_list = []
            if menu_item.get_type == "food":
                item_price = menu_item.get_price()
                price_list.append(item_price)
                avg_price_food = float(sum(price_list)/len(price_list))

            elif menu_item.get_type == "drink":
                item_price = menu_item.get_price()
                price_list.append(item_price)
                avg_price_drink = float(sum(price_list)/len(price_list))
                
        stats = MenuItemStats(total_num_menu_items,num_foods, num_drinks, avg_price_food, avg_price_drink)

        return stats







