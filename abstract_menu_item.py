import datetime

class AbstractMenuItem:
    """ creates menu item """ 
    
    def __init__(self, menu_item_name, menu_item_no, date_added, price, calories )

    self._manu_item_name = menu_item_name
    self._manu_item_no = menu_item_no
    self._date_added = date_added
    self._price = price
    self._calories = calories

    def get_menu_item_name(self):
        """ returns menu item name """ 
        return self._manu_item_name
  