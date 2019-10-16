from menu_item_manager import MenuItemManager
from abstract_menu_item import AbstractMenuItem
from food import Food
from drink import Drink
import datetime




def print_report(menu_item_manager):
    """ prints report for repair shop """
    stats = menu_item_manager.get_menu_item_stats()
    print("  Foods: %d " % stats.get_num_foods())
    print("Description: %s" % menu_item_manager.get_all_by_type("food"))
    print("Description: %s" % menu_item_manager.get_all_by_type("drink"))
    print("  Drinks: %d " % stats.get_num_drinks())
    print("  Average price of food: %f " % stats.get_avg_price_food())
    
    


def main():
    barley_bread = Food("barley_bread", 12, datetime.date(2018, 8, 8), 12.99, 149, "India", "Barley", "small", True)
    chilly_samosa = Food("chilly_samosa", 2, datetime.date(2018, 8, 8), 4.99, 149, "India", "vegetables", "small", True)

    mango_lasi = Drink("mango_lasi", 8, datetime.date(2017, 9, 12), 4.99, 80, "lasi producer ltd", 129.99, False, False)



    kashmir_dosa = MenuItemManager("kashmir dosa")
    kashmir_dosa.add_menu_item(barley_bread)
    kashmir_dosa.add_menu_item(chilly_samosa)
    kashmir_dosa.add_menu_item(mango_lasi)



    print_report(kashmir_dosa)




if __name__ == "__main__":
    main()


