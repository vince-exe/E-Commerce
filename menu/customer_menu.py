from utilities.utils import *

from errors.handle_errors import *

from menu.admin_menu import view_products_menu
from menu.admin_menu import view_product_searched


def buy_product(database, prod_name, person):
    product = database.get_product_bought(prod_name)

    if not prod_bought_errors(product, person.get_money()):
        return

    check = database.rmv_qnt_product(prod_name)

    if check == get_value(DatabaseErrors.CONNECTION_LOST):
        input("\nThe application has lost the connection with the server\n\nPress any key to continue...")
        return

    elif check == get_value(DatabaseErrors.OUT_OF_STOCK):
        input("\nthe product is out of stock\n\nPress any key to continue...")
        return

    person.remove_money(product[2])
    database.customer_change_money(person.get_money(), person.get_id())

    customer_id = database.get_customer_id(person.get_id())
    database.create_my_order(customer_id[0])
    database.create_prod_ordered(product[0], customer_id[0])

    input(f"\nSuccessfully ordered the product: {product[1]}\n\nPress any key to continue...")


def add_money(database, person, credit):
    person.add_money(credit)

    if database.customer_change_money(person.get_money(), person.get_id()):
        input(f"\nSuccessfully added {credit} to the account\n\nPress any key to continue...")
        return

    person.remove_money(credit)
    print("\nCan't add money to the account, the application has lost the connection with the server")
    input("\nPress any key to continue...")
    return


def view_orders(database, person):
    limit = 5

    customer_id = database.get_customer_id(person.get_id())
    if customer_id == get_value(DatabaseErrors.CONNECTION_LOST):
        input("\nThe application has lost the connection with the server\n\nPress any key to continue...")
        return

    while True:
        try:
            os.system('cls||clear')

            option = int(input("\n1)View Orders (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                try:
                    order = database.get_orders(customer_id[0], limit)

                    if view_orders_errors(order):
                        print_orders(order)
                        input("\n\nPress any key to continue...")
                        limit += 5
                    else:
                        return

                except TypeError:
                    input("\nThe application has lost the connection with the server\n\nPress any key to continue...")
                    return

            elif option == 2:
                return

            else:
                input(f'\n{option} is not an option\n\nPress any key to continue...')

        except ValueError:
            input("\nOption must be a number\n\nPress any key to continue...")


def search_order_menu(database, prod_name, person):
    customer_id = database.get_customer_id(person.get_id())

    if customer_id == get_value(DatabaseErrors.CONNECTION_LOST):
        input("\nThe application has lost the connection with the server\n\nPress any key to continue...")
        return

    limit = 5
    while True:
        try:
            os.system('cls||clear')

            option = int(input("\n1)View Orders"
                               "\n2)Exit"
                               "\n\nInsert an option (1 / 2): "))

            if option == 1:
                orders = database.get_orders_searched(customer_id[0], prod_name, limit)

                if search_orders_errors(orders, prod_name):
                    print_orders(orders)
                    input("\n\nPress any key to continue...")
                    limit += 5
                else:
                    return

            elif option == 2:
                return

            else:
                input(f'\n{option} is not a valid option\n\nPress any key to continue...')

        except ValueError:
            input("\nOption must be a number!!\n\nPress any key to continue...")


def delete_customer_order(database):
    id_ = get_order_id()

    if database.delete_order(id_) == get_value(DatabaseErrors.CONNECTION_LOST):
        input("\nThe application has lost the connection with the server\n\nPress any key to continue...")
        return

    input(f"\nSuccessfully removed the order with id: {id_}\n\nPress any key to continue...")


def customer_menu(database, person):
    while True:
        try:
            os.system('cls||clear')
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

            if option_ == get_value(CustomerOptions.VIEW_PRODUCTS):  # View Orders
                view_products_menu(database)

            elif option_ == get_value(CustomerOptions.SEARCH_PRODUCT):  # Search Product
                prod_name = input("\nInsert the name of the product: ")
                view_product_searched(database, prod_name)

            elif option_ == get_value(CustomerOptions.BUY_PRODUCT):  # Buy Product
                prod_name = input("\nInsert the name of the product: ")
                buy_product(database, prod_name, person)

            elif option_ == get_value(CustomerOptions.CHECK_CREDIT):  # Check Credit
                input(f"\nYour credit amounts to: {round(person.get_money(), 2)}\n\nPress any key to continue...")

            elif option_ == get_value(CustomerOptions.ADD_CREDIT):  # Add Credit
                credit = get_money(get_value(MoneyOptions.MIN), get_value(MoneyOptions.MAX))
                add_money(database, person, credit)

            elif option_ == get_value(CustomerOptions.VIEW_ORDERS):  # View Orders
                view_orders(database, person)

            elif option_ == get_value(CustomerOptions.DELETE_ORDERS):  # Delete Orders
                input("\nNote: the application doesn't check if you are using a correct id..")
                delete_customer_order(database)

            elif option_ == get_value(CustomerOptions.SEARCH_ORDERS):  # Search Orders
                product_name = input("\nInsert the product name: ")
                search_order_menu(database, product_name, person)

            elif option_ == get_value(CustomerOptions.EXIT):  # Exit
                return

            else:
                input(f"\n{option_} is not a valid option\n\nPress any key to continue...")

        except ValueError:
            input("\nOption must be a number\n\nPress any key to continue...")
