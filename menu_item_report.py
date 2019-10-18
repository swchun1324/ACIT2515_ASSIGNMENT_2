from menu_item_manager import MenuItemManager
from abstract_menu_item import AbstractMenuItem
from food import Food
from drink import Drink
import datetime




def print_report(menu_item_manager):
    """ prints report for repair shop """
    stats = menu_item_manager.get_menu_item_stats()
    print("  Foods: %d " % stats.get_num_foods())
    print("Food Description: %s" % menu_item_manager.get_all_by_type("food"))
    print("Drink Description: %s" % menu_item_manager.get_all_by_type("drink"))
    print("All menu items: %s " % menu_item_manager.get_all_menu_item())
    print("  Drinks: %d " % stats.get_num_drinks())
    print("  Average price of food: %f " % stats.get_avg_price_food())
    print("  Average price of drink: %f " % stats.get_avg_price_drink())

    
    


def main():
    barley_bread = Food("barley bread", 12, datetime.date(2018, 8, 8), 12.99, 149, "India", "Barley", "small", True)

    mango_lasi3 = Drink("mango lasis", 10, datetime.date(2017, 9, 12), 12.99, 80, "lasi producer ltd", 129.99, False, False)
    print(mango_lasi3.menu_item_description())
    mango_lasi3.set_id(2)

    kashmir_dosa = MenuItemManager("kashmir dosa")
    kashmir_dosa.add_menu_item(barley_bread)


    kashmir_dosa.add_menu_item(mango_lasi3)


    print_report(kashmir_dosa)

    print(kashmir_dosa.menu_exist(3))


if __name__ == "__main__":
    main()


