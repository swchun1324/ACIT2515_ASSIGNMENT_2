import datetime

class AbstractMenuItem:
    """ creates menu item """ 
    
    def __init__(self,  menu_item_name, menu_item_no, date_added, price, calories):
        self._id = None
        self._menu_item_name = menu_item_name
        self._menu_item_no = menu_item_no
        self._date_added = date_added
        self._price = price
        self._calories = calories


    def set_id(self, menu_item_id):
        """ sets menu item id"""
        self._id = menu_item_id 


    def get_id(self):
        """ returns menu item id """
        return self._id


    def get_menu_item_name(self):
        """ returns menu item name """ 
        return self._menu_item_name

    def get_menu_item_no(self):
        """ returns menu  item no """
        return self._menu_item_no

    def get_date_added(self):
        """ returns date added """
        return self._date_added
    
    def menu_item_description(self):
        raise NotImplementedError("abstract method")

    def set_price(self, price):
        """ sets menu item price """
        self._price = price

    def get_price(self):
        """ returns menu item price """
        return self._price

    def get_type(self):
        raise NotImplementedError("abstract method")    


    @staticmethod
    def _validate_menu_item_type(item_type):
        if (item_type == "food") or (item_type == "drink"):
            return 
        else:
            raise ValueError("Menu item must be of type food or drink")
