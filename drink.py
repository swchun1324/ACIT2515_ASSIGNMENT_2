from abstract_menu_item import AbstractMenuItem


class Drink(AbstractMenuItem):
    """ creates drink """

    def __init__(self, id, menu_item_name, menu_item_no, date_added, price, calories, manufacturer, size, is_fizzy, is_hot):
        super().__init__(self, id, menu_item_name, menu_item_no, date_added, price, calories)
        self._manufacturer= manufacturer
        self._size= size
        self._is_fizzy= is_fizzy
        self._is_hot= is_hot

    def menu_item_description(self):
        if self._is_fizzy is True:
            return "%s is a fizzy drink item with menu index %s added on %s with the price of %s, containing %s calories made by %s and is %s ml " % (self._menu_item_name, self._menu_item_no, self._date_added, self._price, self._calories, self._manufacturer, self._size) 
        elif self._is_fizzy is False:
            return "%s is a non-fizzy drink item with menu index %s added on %s with the price of %s, containing %s calories made by %s and is %s ml " % (self._menu_item_name, self._menu_item_no, self._date_added, self._price, self._calories, self._manufacturer, self._size)
        elif self._is_hot is True:
            return "%s is a hot drink item with menu index %s added on %s with the price of %s, containing %s calories made by %s and is %s ml " % (self._menu_item_name, self._menu_item_no, self._date_added, self._price, self._calories, self._manufacturer, self._size)
        elif self._is_hot is False:
            return "%s is a cold drink item with menu index %s added on %s with the price of %s, containing %s calories made by %s and is %s ml " % (self._menu_item_name, self._menu_item_no, self._date_added, self._price, self._calories, self._manufacturer, self._size)
    
    def get_type(self):
        """ returns menu item type """
        MENU_ITEM_TYPE = "drink" 
        return MENU_ITEM_TYPE

    def get_manufacturer(self):
        return self._manufacturer
    def get_size(self):
        return self._size



