
class MenuItemStats():
    """ Statistics on a Restaurant Menu """
    def __init__(self, total_num_menu_items , num_foods, num_drinks, avg_price_food, avg_price_drink):
        """ Initialize the data values """

        self._total_num_menu_items = total_num_menu_items
        self._num_foods = num_foods
        self._num_drinks = num_drinks
        self._avg_price_food = avg_price_food
        self._avg_price_drink = avg_price_drink


    def _get_total_num_menu_items(self):
        """ returns  total number of menu  items """
        return self._total_num_menu_items

    def _get_num_foods(self):
        """ returns total number of foods  """
        return self._num_foods

    def _get_num_drinks(self):
        """ returns total number of drinks  """
        return self._num_drinks

    def _get_avg_price_food(self):
        """ returns average price of food  """
        return self._avg_price_food

    def _get_avg_price_drink(self):
        """ returns average price of drink  """
        return self._avg_price_drink
    