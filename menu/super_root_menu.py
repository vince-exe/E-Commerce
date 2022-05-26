from utilities.utils import *
from utilities.enums import *


def super_root_menu():
    while True:
        try:
            option = int(input("\n1)Add Admin"
                               "\n2)Delete Admin"
                               "\n3)Search Admin"
                               "\n4)Modify Admin"
                               "\n5)Exit"
                               "\n\nInsert option (1 / 5): "))

            if option == get_value(SuperRootOptions.ADD_ADMIN):
                pass

            elif option == get_value(SuperRootOptions.DELETE_ADMIN):
                pass

            elif option == get_value(SuperRootOptions.SEARCH_ADMIN):
                pass

            elif option == get_value(SuperRootOptions.MODIFY_ADMIN):
                pass

            elif option == get_value(SuperRootOptions.EXIT):
                return

            else:
                print(f'\n{option} is not an option')

        except ValueError:
            print("\nOption must be a number!!")