from utilities.utils import *
from errors.handle_errors import *


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

    while True:
        try:
            option = int(input("\n1)View Products (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                if not prod_searched_errors(database.get_product_searched(cursor, prod_name, limit), prod_name):
                    return
                else:
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
                               "\n\nInsert option (1 /2): "
                               )
                         )

            if option == 1:
                while True:
                    try:
                        id_ = int(input("\nInsert the product id: "))
                        break
                    except ValueError:
                        print("\nId must be a number")

                del_prod = database.delete_product(cursor, connection, id_)
                if rmv_errors(del_prod):
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
                               "\n\nInsert option (1 / 2): "
                               )
                         )

            if option == 1:
                while True:
                    try:
                        id_ = int(input("\nInsert the customer id: "))
                        break
                    except ValueError:
                        print("\nId must be a number!!")

                deleted_customer = database.delete_customer(cursor, connection, id_)
                if rmv_errors(deleted_customer):
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

    if not customer_searched_errors(database.get_customer_searched(cursor, customer_name, limit), customer_name):
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


def modify_product(database, connection, cursor):
    prod_id = get_id_product()

    while True:
        try:
            option = int(input("\n1)Change Name"
                               "\n2)Change Quantity"
                               "\n3)Change Price"
                               "\n4)Exit"
                               "\n\nInsert option (1 / 4): "))

            if option == 1:
                database.update_name_product(cursor, connection, prod_id, input("\nInsert the new name: "))

            elif option == 2:
                database.update_qnt_product(cursor, connection, prod_id, get_prod_qnt())

            elif option == 3:
                database.update_price_product(cursor, connection, prod_id, get_prod_price(get_value(PriceOptions.MAX)))

            elif option == 4:
                return

            else:
                print(f'\n{option} is not an option')

        except ValueError:
            print("\nOption must be a number!!")


def admin_menu(database, cursor, connection):
    while True:
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
                view_customers_menu(cursor, database)

            elif option == get_value(AdminOptions.VIEW_PRODUCTS):  # View Products
                view_products_menu(cursor, database)

            elif option == get_value(AdminOptions.ADD_PRODUCT):  # Add Product
                prod_info = get_product_info()
                add_prod_errors(database.add_product(cursor, prod_info, connection), prod_info)

            elif option == get_value(AdminOptions.MODIFY_PRODUCT):  # Modify Product
                modify_product(database, connection, cursor)

            elif option == get_value(AdminOptions.SEARCH_PRODUCT):  # Search Product
                prod_name = input("\nInsert the name of the product: ")
                view_product_searched(database, cursor, prod_name)

            elif option == get_value(AdminOptions.DELETE_PRODUCT):  # Delete Product
                print("\n\nNote: The application doesn't check if you are using the correct id")
                delete_product_menu(database, cursor, connection)

            elif option == get_value(AdminOptions.DELETE_CUSTOMER):  # Delete Customer
                print("\n\nNote: The application doesn't check if you are using the correct id")
                delete_customer_menu(database, connection, cursor)

            elif option == get_value(AdminOptions.SEARCH_CUSTOMER):  # Search Customer
                customer_name = input("\nInsert the customer name: ")
                search_customer_menu(database, cursor, customer_name)

            elif option == get_value(AdminOptions.EXIT):  # Exit
                return

            else:
                print(f"{option} must be a number!!")

        except ValueError:
            print("\nOption can't be a string!!")
