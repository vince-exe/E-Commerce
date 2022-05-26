from utilities.utils import *
from utilities.enums import *


def customer_menu():
    while True:
        try:
            option = int(input("\n1)View All Products"
                               "\n2)Search Product"
                               "\n3)Buy Product"
                               "\n4)Check Credit"
                               "\n5)Add Credit"
                               "\n6)View Orders"
                               "\n7)Delete Orders"
                               "\n8)Search Order"
                               "\n9)Exit"
                               "\n\nInsert option (1 / 9): "))

            if option == get_value(CustomerOptions.VIEW_PRODUCTS):
                pass

            elif option == get_value(CustomerOptions.SEARCH_PRODUCT):
                pass

            elif option == get_value(CustomerOptions.BUY_PRODUCT):
                pass

            elif option == get_value(CustomerOptions.CHECK_CREDIT):
                pass

            elif option == get_value(CustomerOptions.ADD_CREDIT):
                pass

            elif option == get_value(CustomerOptions.VIEW_ORDERS):
                pass

            elif option == get_value(CustomerOptions.DELETE_ORDERS):
                pass

            elif option == get_value(CustomerOptions.SEARCH_ORDERS):
                pass

            elif option == get_value(CustomerOptions.EXIT):
                return

            print(f"\n{option} is not a valid option")

        except ValueError:
            print("\nOption must be a number")
