from abstract_menu_item import AbstractMenuItem
from menu_item_stats import MenuItemStats
from food import Food
from drink import Drink


class MenuItemManager:
    """ creates menu item manager """

    def __init__(self, restaurant_name):

        self._validate_parameter(restaurant_name, "restaurant_name")

        self._restaurant_name = restaurant_name

        self._menu = []

        self._next_available_id = int(0)

    def add_menu_item(self, menu_item):
        """adds a menu item to the menu list"""

        self._validate_parameter(menu_item, "menu_item")

        self._next_available_id += 1
        menu_item.set_id(self._next_available_id)

        if self.menu_exist(menu_item.get_id()) is False:
            self._menu.append(menu_item)

        return self._next_available_id

    def menu_exist(self, id):

        self._validate_parameter(id, "id")

        for menu in self._menu:
            if menu.get_id() == id:
                return True

        return False

    def remove_menu_item(self, id):

        self._validate_parameter(id, "id")

        if self.menu_exist(id) is True:
            for menu_item in self._menu:
                if menu_item.get_id() is id:
                    self._menu.remove(menu_item)

    def get_by_id(self, id):

        self._validate_parameter(id, "id")

        for menu_item in self._menu:
            if menu_item.get_id() == id:
                return menu_item

    def get_all_by_type(self, item_type):

        self._validate_parameter(item_type, "item_type")
        self._validate_type(item_type)

        menu_list = []
        for menu_item in self._menu:
            if menu_item.get_type() == item_type:
                menu_list.append(menu_item.menu_item_description())
        return menu_list

    def get_all(self):

        return self._menu

    def get_all_menu_item(self):

        menu_list = []

        for i in range(len(self._menu)):
            menu_list.append(self._menu[i].get_menu_item_name())

        return menu_list

    def update(self, menu_item):

        self._validate_parameter(menu_item, "menu_item")

        id = menu_item.get_id()

        if self.menu_exist(id) is False:
            raise ValueError("id does not exist")
        for index, menu_items in enumerate(self._menu, 0):
            if menu_items.get_id() == id:
                self._menu[index] = menu_item
                break

    def get_menu_item_stats(self):

        """ gets menu item stats """
        total_num_menu_items = int(0)
        num_foods = int(0)
        num_drinks = int(0)
        avg_price_food = float(0)
        avg_price_drink = float(0)
        item_price = float(0)
        food_price_list = []
        drink_price_list = []

        for menu_item in self._menu:
            total_num_menu_items += 1
            if menu_item.get_type() == "food":
                num_foods += 1
            if menu_item.get_type() == "drink":
                num_drinks += 1

        for menu_item in self._menu:
            if menu_item.get_type() == "drink":
                item_price = menu_item.get_price()
                drink_price_list.append(item_price)
                avg_price_drink = sum(drink_price_list) / len(drink_price_list)

        for menu_item in self._menu:
            if menu_item.get_type() == "food":
                item_price = menu_item.get_price()
                food_price_list.append(item_price)
                avg_price_food = sum(food_price_list) / len(food_price_list)

        stats = MenuItemStats(total_num_menu_items, num_foods, num_drinks, avg_price_food, avg_price_drink)

        return stats

    @staticmethod
    def _validate_parameter(value, name):
        """Private method to validate inputs

        Args:
            value: Input to be validated
            name: Name of input

        Raises:
            ValueError: If value is undefined
            ValueError: If value is not given
        """

        if value is None:
            raise ValueError("%s cannot be undefined" % (name))

        if value is "":
            raise ValueError("%s cannot be empty" % (name))

    @staticmethod
    def _validate_type(value):
        """Private method to validate player type

        Args:
            value (string): Type of player (either "Forward" or "Goalie")

        Raises:
            ValueError: If value is neither "Forward" or "Goalie"
        """

        if (value is "food") or (value is "drink"):
            return
        else:
            raise ValueError("Player Type must be Forward or Goalie")
