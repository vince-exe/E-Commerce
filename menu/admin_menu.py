from utilities.utils import *

from errors.handle_errors import *

import os


def view_customers_menu(database):
    limit = 5

    while True:
        try:
            os.system('cls||clear')
            option = int(input("\n1)Show Customers (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                customers = database.get_customers(limit)

                if customers == get_value(DatabaseErrors.CONNECTION_LOST):
                    input("""\nThe application has lost the connection with the database
                                  \n\nPress any key to continue...""")

                elif not len(customers):
                    input("\nThere are no customers registered\n\nPress any key to continue...")

                else:
                    print_customers(customers)
                    input("\nPress any key to continue...")
                    limit += 5

            elif option == 2:
                return

            else:
                try:
                    input(f'\n{option} is not a valid option\n\nPress any key to continue...')

                except KeyboardInterrupt:
                    database.shut_down()

        except ValueError:
            input("\nOption must be a number!!\n\nPress any key to continue...")


def view_products_menu(database):
    limit = 5
    while True:
        try:
            os.system('cls||clear')

            option = int(input("\n1)View Products (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                products = database.get_products(limit)
                if products == get_value(DatabaseErrors.CONNECTION_LOST):
                    try:
                        input("""\nThe application has lost the connection with the server
                                  \n\nPress any key to continue...""")

                    except KeyboardInterrupt:
                        database.shut_down()

                else:
                    try:
                        print_products(products)
                        input("\nPress any key to continue...")
                        limit += 5

                    except KeyboardInterrupt:
                        database.shut_down()

            elif option == 2:
                return

            else:
                try:
                    input(f'\n{option} is not a valid option\n\nPress any key to continue...')

                except KeyboardInterrupt:
                    database.shut_down()

        except ValueError:
            input("\nOption must be a number!!\n\nPress any key to continue...")


def view_product_searched(database, prod_name):
    limit = 5

    while True:
        try:
            os.system('cls||clear')
            option = int(input("\n1)View Products (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                if not prod_searched_errors(database.get_product_searched(prod_name, limit), prod_name):
                    return

                else:
                    print_products(database.get_product_searched(prod_name, limit))
                    input("\n\nPress any key to continue...")
                    limit += 5

            elif option == 2:
                return

            else:
                input(f'\n{option} is not an option\n\nPress any key to continue...')

        except ValueError:
            print("\nOption must be a number\n\nPress any key to continue...")


def delete_product_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input("\n1)Delete Product"
                               "\n2)Exit"
                               "\n\nInsert option (1 /2): "
                               )
                         )

            if option == 1:
                while True:
                    try:
                        os.system('cls||clear')
                        id_ = int(input("\nInsert the product id: "))
                        break
                    except ValueError:
                        input("\nId must be a number!!\n\nPress any key to continue...")

                del_prod = database.delete_product(id_)
                if rmv_errors(del_prod):
                    input(f"\nSuccessfully removed the product with id: {id_}\n\nPress any key to continue...")

            elif option == 2:
                return

            else:
                input(f'\n{option} is not a valid option\n\nPress any key to continue...')

        except ValueError:
            input("\nOption must be a number!!\n\nPress any key to continue...")


def delete_customer_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input("\n1)Delete Customer"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "
                               )
                         )

            if option == 1:
                while True:
                    try:
                        id_ = int(input("\nInsert the customer id: "))
                        break
                    except ValueError:
                        input("\nId must be a number!!\n\nPress any key to continue...")

                if rmv_errors(database.delete_customer(id_)):
                    input(f"\nSuccessfully removed the customer with id: {id_}\n\nPress any key to continue...")

            elif option == 2:
                return

            else:
                input(f"\n{option} is not a valid option\n\nPress any key to continue...")

        except ValueError:
            input("\nOption must be a number!!\n\nPress any key to continue...")


def search_customer_menu(database, customer_name):
    limit = 5

    while True:
        try:
            os.system('cls||clear')
            option = int(input("\n1)View Customer"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                if customer_searched_errors(database.get_customer_searched(customer_name, limit),
                                            customer_name):

                    print_customers(database.get_customer_searched(customer_name, limit))
                    input("\n\nPress any key to continue...")
                    limit += 5

                else:
                    return

            elif option == 2:
                return

            else:
                input(f"\n{option} is not a valid option\n\nPress any key to continue...")

        except ValueError:
            input("\nOption must be a number!!\n\nPress any key to continue...")


def modify_product(database):
    prod_id = get_id_product()

    while True:
        try:
            os.system('cls||clear')
            option = int(input("\n1)Change Name"
                               "\n2)Change Quantity"
                               "\n3)Change Price"
                               "\n4)Exit"
                               "\n\nInsert option (1 / 4): "))

            if option == 1:
                os.system('cls||clear')
                prod_name = input("\nInsert the new name: ")
                update_name_product_errors(database.update_name_product(prod_id, prod_name), prod_name)

            elif option == 2:
                update_qnt_errors(database.update_qnt_product(prod_id, get_prod_qnt()))

            elif option == 3:
                database.update_price_product(prod_id, get_prod_price(get_value(PriceOptions.MAX)))

            elif option == 4:
                return

            else:
                input(f'\n{option} is not an option...')

        except ValueError:
            input("\nOption must be a number!!")


def admin_menu(database):
    while True:
        os.system('cls||clear')
        try:
            option = int(input(("\n1)View All Customers"
                                "\n2)View All Products"
                                "\n3)Add Product"
                                "\n4)Modify Product"
                                "\n5)Search Product (info)"
                                "\n6)Delete Product"
                                "\n7)Delete Customer"
                                "\n8)Search Customer"
                                "\n9)Exit"
                                "\n\nInsert option (1 / 9): "
                                )))

            if option == get_value(AdminOptions.VIEW_CUSTOMERS):  # View Customers
                view_customers_menu(database)

            elif option == get_value(AdminOptions.VIEW_PRODUCTS):  # View Products
                view_products_menu(database)

            elif option == get_value(AdminOptions.ADD_PRODUCT):  # Add Product
                prod_info = get_product_info()
                add_prod_errors(database.add_product(prod_info), prod_info)

            elif option == get_value(AdminOptions.MODIFY_PRODUCT):  # Modify Product
                input("\n\nNote: The application doesn't check if you are using the correct id..")
                modify_product(database)

            elif option == get_value(AdminOptions.SEARCH_PRODUCT):  # Search Product
                prod_name = input("\nInsert the name of the product: ")
                view_product_searched(database, prod_name)

            elif option == get_value(AdminOptions.DELETE_PRODUCT):  # Delete Product
                input("\n\nNote: The application doesn't check if you are using the correct id..")
                delete_product_menu(database)

            elif option == get_value(AdminOptions.DELETE_CUSTOMER):  # Delete Customer
                input("\n\nNote: The application doesn't check if you are using the correct id..")
                delete_customer_menu(database)

            elif option == get_value(AdminOptions.SEARCH_CUSTOMER):  # Search Customer
                customer_name = input("\nInsert the customer name: ")
                search_customer_menu(database, customer_name)

            elif option == get_value(AdminOptions.EXIT):  # Exit
                return

            else:
                input(f"{option} is not a valid option...")

        except ValueError:
            input("\nOption must be a number!")

        except KeyboardInterrupt:
            database.shut_down()
