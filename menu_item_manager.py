from abstract_menu_item import AbstractMenuItem
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

    
    def get(self, id):

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
                
                    
    def get_menu_item_stats(self):
        """ gets menu item stats """
        pass
    

    def update(self, menu_item):
        pass
    
    def remove_menu_item_by_id(self, id):
        pass






