from utilities.utils import *
from utilities.enums import *

info = ['localhost', 'root', 'MySQL85.#(6@', 'ecommerce']


def initial_customer_menu(database, cursor, connection):
    while True:
        try:
            option = int(input("\n1)Sign In"
                               "\n2)Sign Up"
                               "\n3)exit"
                               "\n\nInsert option (1 / 3): "))

            if option == get_value(GeneralOptions.SIGN_IN):
                if handle_sign_in_customer(get_psw_email_customer(), database, cursor):
                    customer_menu()

            elif option == get_value(GeneralOptions.SIGN_UP):
                info_customer = get_info_customer()

                if handle_add_person_errors(database.add_person(cursor, info_customer, connection), info_customer):
                    handle_add_customer(database.add_customer(cursor, connection, info_customer[2]))

            elif option == get_value(GeneralOptions.EXIT):
                return

            else:
                print(f"\n{option} is not a valid option!!")

        except ValueError:
            print("\nOption must be a number!!")


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


def view_customers_menu(cursor, database):
    limit = 5

    while True:
        try:
            option = int(input("\n1)Show Customers (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                customers = database.get_customers(cursor, limit)

                if customers == get_value(DatabaseErrors.CONNECTION_LOST):
                    print("\nThe application has lost the connection with the database")
                else:
                    print_customers(customers)
                    limit += 5

            elif option == 2:
                return

            else:
                print(f'\n{option} is not a valid option')

        except ValueError:
            print("\nOption must be a number!!")


def view_products_menu(cursor, database):
    limit = 5
    while True:
        try:
            option = int(input("\n1)View Products (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                products = database.get_products(cursor, limit)
                if products == get_value(DatabaseErrors.CONNECTION_LOST):
                    print("\nThe application has lost the connection with the server")

                else:
                    print_products(products)
                    limit += 5

            elif option == 2:
                return

            else:
                print(f'\n{option} is not a valid option')

        except ValueError:
            print("\nOption must be a number!!")


def view_product_searched(database, cursor, prod_name):
    limit = 5

    if not handle_product_searched(database.get_product_searched(cursor, prod_name, limit), prod_name):
        return

    while True:
        try:
            option = int(input("\n1)View Products (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                print_products(database.get_product_searched(cursor, prod_name, limit))
                limit += 5

            elif option == 2:
                return

            else:
                print(f'\n{option} is not an option')

        except ValueError:
            print("\nOption must be a number")


def delete_product_menu(database, cursor, connection):
    while True:
        try:
            option = int(input("\n1)Delete Product"
                               "\n2)Exit"
                               "\n\nNote: The application doesn't check if the removed product was in the database,"
                               "so delete using the correct id"
                               "\n\nInsert option (1 /2): "
                               )
                         )

            if option == 1:
                id_ = 0
                while True:
                    try:
                        id_ = int(input("\nInsert the product id: "))
                        break
                    except ValueError:
                        print("\nId must be a number")

                del_prod = database.delete_product(cursor, connection, id_)
                if handle_rmv_errors(del_prod):
                    print(f"\nSuccessfully removed the product with id: {id_}")

            elif option == 2:
                return

            else:
                print(f'\n{option} is not a valid option')

        except ValueError:
            print("\nOption must be a number!!")


def delete_customer_menu(database, connection, cursor):
    while True:
        try:
            option = int(input("\n1)Delete Customer"
                               "\n2)Exit"
                               "\n\nNote: the application doesn't check if the customer was in the database,"
                               "so delete the customer using the correct id"
                               "\n\nInsert option (1 / 2): "
                               )
                         )

            if option == 1:
                id_ = 0
                while True:
                    try:
                        id_ = int(input("\nInsert the customer id: "))
                        break
                    except ValueError:
                        print("\nId must be a number!!")

                deleted_customer = database.delete_customer(cursor, connection, id_)
                if handle_rmv_errors(deleted_customer):

                    database.delete_person(cursor, connection, id_)
                    print(f"\nSuccessfully removed the customer with id: {id_}")

            elif option == 2:
                return

            else:
                print(f"\n{option} is not a valid option")

        except ValueError:
            print("\nOption must be a number!!")


def search_customer_menu(database, cursor, customer_name):
    limit = 5

    if not handle_customer_searched_errors(database.get_customer_searched(cursor, customer_name, limit), customer_name):
        return

    while True:
        try:
            option = int(input("\n1)View Customer"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                print_customers(database.get_customer_searched(cursor, customer_name, limit))
                limit += 5

            elif option == 2:
                return

            else:
                print(f"\n{option} is not a valid option")

        except ValueError:
            print("\nOption must be a number!!")


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


def admin_menu(database, cursor, connection):
    while True:
        try:
            option = int(input(("\n1)View All Customers"
                                "\n2)View All Products"
                                "\n3)Add Product"
                                "\n4)Search Product (info)"
                                "\n5)Delete Product"
                                "\n6)Delete Customer"
                                "\n7)Search Customer"
                                "\n8)Exit"
                                "\n\nInsert option (1 / 8): "
                                )))

            if option == get_value(AdminOptions.VIEW_CUSTOMERS):  # view all the customers
                view_customers_menu(cursor, database)

            elif option == get_value(AdminOptions.VIEW_PRODUCTS):  # view all the products
                view_products_menu(cursor, database)

            elif option == get_value(AdminOptions.ADD_PRODUCT):  # add a product
                prod_info = get_product_info()
                handle_product_errors(database.add_product(cursor, prod_info, connection), prod_info)

            elif option == get_value(AdminOptions.SEARCH_PRODUCT):  # search a product
                prod_name = input("\nInsert the name of the product: ")
                view_product_searched(database, cursor, prod_name)

            elif option == get_value(AdminOptions.DELETE_PRODUCT):  # delete a product
                delete_product_menu(database, cursor, connection)

            elif option == get_value(AdminOptions.DELETE_CUSTOMER):  # delete a customer
                delete_customer_menu(database, connection, cursor)

            elif option == get_value(AdminOptions.SEARCH_CUSTOMER):  # search a customer
                customer_name = input("\nInsert the customer name: ")
                search_customer_menu(database, cursor, customer_name)

            elif option == get_value(AdminOptions.EXIT):  # exit
                return

            else:
                print(f"{option} must be a number!!")

        except ValueError:
            print("\nOption can't be a string!!")


def initial_admin_menu(database, cursor, connection):
    while True:
        try:
            option = int(input("\n1)Sign In (Standard Admin)"
                               "\n2)Sign In (Super Admin)"
                               "\n3)Exit"
                               "\n\nInsert option (1 / 3): "))

            if option == 1:
                if get_info_admin(database, cursor):
                    admin_menu(database, cursor, connection)

            elif option == 2:
                if get_super_root_info(database, cursor):
                    super_root_menu()

            elif option == 3:
                return

            else:
                print(f"\n{option} is not a valid option!!")

        except ValueError:
            print("\nOption must be a number")


def general_menu(database, cursor, connection):
    while True:
        try:
            option = int(input("\n1)Log as Admin"
                               "\n2)Log as Customer"
                               "\n3)Exit"
                               "\n\nInsert option (1 / 3): "))

            if option == get_value(GeneralMenuOptions.LOG_AS_ADMIN):
                initial_admin_menu(database, cursor, connection)

            elif option == get_value(GeneralMenuOptions.LOG_AS_CUSTOMER):
                initial_customer_menu(database, cursor, connection)

            elif option == get_value(GeneralMenuOptions.EXIT):
                return False

            else:
                print(f"\n{option} is not a correct option!!")

        except ValueError:
            print("\nOption must be a number")
