import mysql.connector.errors

from utilities.utils import *
from utilities.enums import *

from menu.admin_menu import view_products_menu
from menu.admin_menu import view_product_searched


def buy_product(database, prod_name, cursor, person, connection):
    product = database.get_product_bought(cursor, prod_name)

    if not handle_product_bought(product, prod_name, person.get_money()):
        return

    if database.rmv_qnt_product(cursor, connection, prod_name) == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return

    else:
        person.remove_money(product[2])
        return


def add_money(database, cursor, connection, person, credit):
    person.add_money(credit)

    if database.customer_add_money(cursor, connection, person.get_money(), person.get_id()):
        print(f"\nSuccessfully added {credit} to the account")

        input("\nPress any key to continue...")
        return

    person.remove_money(credit)
    print("\nCan't add money to the account, the application has lost the connection with the server")

    input("\nPress any key to continue...")
    return


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
                print(f"\nYour credit amounts to: {person.get_money()}")
                input("\nPress any key to continue...")

            elif option_ == get_value(CustomerOptions.ADD_CREDIT):
                credit = get_money(get_value(MoneyOptions.MIN), get_value(MoneyOptions.MAX))
                add_money(database, cursor, connection, person, credit)

            elif option_ == get_value(CustomerOptions.VIEW_ORDERS):
                pass

            elif option_ == get_value(CustomerOptions.DELETE_ORDERS):
                pass

            elif option_ == get_value(CustomerOptions.SEARCH_ORDERS):
                pass

            elif option_ == get_value(CustomerOptions.EXIT):
                return

            else:
                print(f"\n{option_} is not a valid option")

        except ValueError:
            print("\nOption must be a number")
