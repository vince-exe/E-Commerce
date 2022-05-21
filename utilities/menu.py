from utilities.utils import *

info = ['localhost', 'root', 'mySQLroot45.&ciao#.', 'ecommerce']


def initial_customer_menu():
    exit_ = False

    while not exit_:
        try:
            option = int(input("\n1)Sign In\n2)Sign Up\n3)exit\n\nInsert option (1 / 3): "))

            if option == get_value(GeneralOptions.SIGN_IN):
                pass

            elif option == get_value(GeneralOptions.SIGN_UP):
                pass

            elif option == get_value(GeneralOptions.EXIT):
                return False

            else:
                print(f"\n{option} is not a valid option!!")

        except ValueError:
            print("\nOption must be a number!!")


def admin_menu(database, cursor, connection):
    exit_ = False
    while not exit_:
        try:
            option = int(input(("\n1)View All Customers"
                                "\n2)View All Products"
                                "\n3)Add Product"
                                "\n4)Add Admin"
                                "\n5)Search Product (info)"
                                "\n6)Delete Product"
                                "\n7)Delete Customer"
                                "\n8)Search Customer"
                                "\n9)Exit"
                                "\n\nInsert option (1 / 9): "
                                )))

            if option == get_value(AdminOptions.VIEW_CUSTOMERS):  # view all the customers
                pass

            elif option == get_value(AdminOptions.VIEW_PRODUCTS):  # view all the products
                pass

            elif option == get_value(AdminOptions.ADD_PRODUCT):  # add a product
                prod_info = get_product_info()
                handle_product_errors(database.add_product(cursor, prod_info, connection), prod_info)

            elif option == get_value(AdminOptions.ADD_ADMIN):  # add an admin
                pass

            elif option == get_value(AdminOptions.SEARCH_PRODUCT):  # search a product
                pass

            elif option == get_value(AdminOptions.DELETE_PRODUCT):  # delete a product
                pass

            elif option == get_value(AdminOptions.DELETE_CUSTOMER):  # delete a customer
                pass

            elif option == get_value(AdminOptions.SEARCH_CUSTOMER):  # search a customer
                pass

            elif option == get_value(AdminOptions.EXIT):  # exit
                exit_ = True
                break

            else:
                print(f"{option} must be a number!!")

        except ValueError:
            print("\nOption can't be a string!!")


def initial_admin_menu(database, cursor, connection):
    exit_ = False

    while not exit_:
        try:
            option = int(input("\n1)Sign In\n2)Exit\n\nInsert option (1 / 2): "))

            if option == get_value(GeneralOptions.SIGN_IN):
                if get_info_admin(database, cursor):
                    admin_menu(database, cursor, connection)

            elif option == get_value(AdminOptions.EXIT_LOG):
                return False

            else:
                print(f"\n{option} is not a valid option!!")

        except ValueError:
            print("\nOption must be a number")


def general_menu(database, cursor, connection):
    exit_ = False

    while not exit_:
        try:
            option = int(input("\n1)Log as Admin\n2)Log as Customer\n3)Exit\n\nInsert option (1 / 3): "))

            if option == get_value(GeneralMenuOptions.LOG_AS_ADMIN):
                if not initial_admin_menu(database, cursor, connection):
                    return False

            elif option == get_value(GeneralMenuOptions.LOG_AS_CUSTOMER):
                if not initial_customer_menu():
                    return False

            elif option == get_value(GeneralMenuOptions.EXIT):
                return False
            else:
                print(f"\n{option} is not a correct option!!")

        except ValueError:
            print("\nOption must be a number")
