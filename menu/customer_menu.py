from utilities.utils import *
from utilities.enums import *

from menu.admin_menu import view_products_menu
from menu.admin_menu import view_product_searched


def buy_product(database, prod_name, cursor, person, connection):
    product = database.get_product_bought(cursor, prod_name)

    if not handle_product_bought(product, person.get_money()):
        return

    check = database.rmv_qnt_product(cursor, connection, prod_name)

    if check == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return

    elif check == get_value(DatabaseErrors.OUT_OF_STOCK):
        print("\nthe product is out of stock")

        input("\nPress any key to continue...")
        return

    person.remove_money(product[2])
    database.customer_change_money(cursor, connection, person.get_money(), person.get_id())

    customer_id = database.get_customer_id(cursor, person.get_id())
    database.create_my_order(cursor, connection, customer_id[0])
    database.create_prod_ordered(cursor, connection, product[0], customer_id[0])

    print(f"\nSuccessfully ordered the product: {product[1]}")
    input("\nPress any key to continue...")


def add_money(database, cursor, connection, person, credit):
    person.add_money(credit)

    if database.customer_change_money(cursor, connection, person.get_money(), person.get_id()):
        print(f"\nSuccessfully added {credit} to the account")

        input("\nPress any key to continue...")
        return

    person.remove_money(credit)
    print("\nCan't add money to the account, the application has lost the connection with the server")

    input("\nPress any key to continue...")
    return


def view_orders(database, cursor, person):
    limit = 5

    customer_id = database.get_customer_id(cursor, person.get_id())
    if customer_id == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return

    while True:
        try:
            option = int(input("\n1)View Orders (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                try:
                    order = database.get_orders(cursor, customer_id[0], limit)

                    if handle_view_orders(order):
                        print_orders(order)
                        limit += 5
                    else:
                        return

                except TypeError:
                    print("\nThe application has lost the connection with the server")

                    input("\nPress any key to continue...")
                    return

            elif option == 2:
                return

            else:
                print(f'\n{option} is not an option')

        except ValueError:
            print("\nOption must be a number")


def search_order_menu(database, cursor, prod_name, person):
    customer_id = database.get_customer_id(cursor, person.get_id())

    if customer_id == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress an key to continue...")
        return

    limit = 5
    while True:
        try:
            option = int(input("\n1)View Orders"
                               "\n2)Exit"
                               "\n\nInsert an option (1 / 2): "))

            if option == 1:
                orders = database.get_orders_searched(cursor, customer_id[0], prod_name, limit)

                if handle_search_orders(orders, prod_name):
                    print_orders(orders)
                    limit += 5
                else:
                    return

            elif option == 2:
                return

            else:
                print(f'\n{option} is not a valid option')

        except ValueError:
            print("\nOption must be a number!!")


def delete_customer_order(database, cursor, connection):
    id_ = get_order_id()

    if database.delete_order(cursor, connection, id_) == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return

    print(f"\nSuccessfully removed the order with id: {id_}")


def customer_menu(cursor, database, connection, person):
    while True:
        try:
            option_ = int(input("\n1)View All Products"
                                "\n2)Search Product"
                                "\n3)Buy Product"
                                "\n4)Check Credit"
                                "\n5)Add Credit"
                                "\n6)View Orders"
                                "\n7)Delete Orders"
                                "\n8)Search Order"
                                "\n9)Exit"
                                "\n\nInsert option (1 / 9): "))

            if option_ == get_value(CustomerOptions.VIEW_PRODUCTS):
                view_products_menu(cursor, database)

            elif option_ == get_value(CustomerOptions.SEARCH_PRODUCT):
                prod_name = input("\nInsert the name of the product: ")
                view_product_searched(database, cursor, prod_name)

            elif option_ == get_value(CustomerOptions.BUY_PRODUCT):
                prod_name = input("\nInsert the name of the product: ")
                buy_product(database, prod_name, cursor, person, connection)

            elif option_ == get_value(CustomerOptions.CHECK_CREDIT):
                print(f"\nYour credit amounts to: {round(person.get_money(), 2)}")
                input("\nPress any key to continue...")

            elif option_ == get_value(CustomerOptions.ADD_CREDIT):
                credit = get_money(get_value(MoneyOptions.MIN), get_value(MoneyOptions.MAX))
                add_money(database, cursor, connection, person, credit)

            elif option_ == get_value(CustomerOptions.VIEW_ORDERS):
                view_orders(database, cursor, person)

            elif option_ == get_value(CustomerOptions.DELETE_ORDERS):
                print("\nNote: the application doesn't check if the order exist, so use the correct id")
                delete_customer_order(database, cursor, connection)

            elif option_ == get_value(CustomerOptions.SEARCH_ORDERS):
                product_name = input("\nInsert the product name: ")
                search_order_menu(database, cursor, product_name, person)

            elif option_ == get_value(CustomerOptions.EXIT):
                return

            else:
                print(f"\n{option_} is not a valid option")

        except ValueError:
            print("\nOption must be a number")
