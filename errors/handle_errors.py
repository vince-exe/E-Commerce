from utilities.enums import *
from person.person import Person


def conn_lost_msg():
    print("\nThe application has lost the connection with the server")

    input("\nPress any key to continue...")
    return


def add_prod_errors(error, prod_info):
    if error == get_value(DatabaseErrors.CONNECTION_LOST):
        print(f"\nCan't add the product: {prod_info[0]} the application lost the connection with the server :(")

        input("\nPress any key to continue...")
        return

    elif error == get_value(DatabaseErrors.NAME_ALREADY_EXIST):
        print(f'\nThere is already a product named: {prod_info[0]}')

        input("\nPress any key to continue...")
        return

    elif error == get_value(DatabaseErrors.DATA_ERROR):
        print(f"\nCan't add this product with name: {prod_info[0]}")

        input("\nPress any key to continue...")
        return

    else:
        print(f'\nSuccessfully added the product: {prod_info[0]}')

        input("\nPress any key to continue...")
        return


def db_conn_errors(error, database):
    if error is None:
        print("\nThe server is unreachable")

        input("\nPress any key to continue...")
        exit(-1)

    elif error == get_value(DatabaseErrors.ACCESS_DENIED):
        print("\nSomething went wrong with username and password")

        input("\nPress any key to continue...")
        exit(-1)

    elif error == get_value(DatabaseErrors.DB_EXCEPTION):
        print(f'\nThere is no database with the name: {database.db_name}')

        input("\nPress any key to continue...")
        exit(-1)

    elif error == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        exit(-1)

    # all the controls went fine.
    print(f'\nSuccessfully connected to the database [{database.db_name}]')
    return error


def prod_searched_errors(product, product_name):
    if product == -1:
        conn_lost_msg()
        return False

    elif not len(product):
        print(f"\nNo product named: {product_name}")

        input("\nPress any key to continue...")
        return False

    elif product == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return False

    return True


def customer_searched_errors(customer_searched, customer_name):
    if customer_searched == -1:
        conn_lost_msg()
        return False

    elif not len(customer_searched):
        print(f"\nNo customer named: {customer_name}")

        input("\nPress any key to continue...")
        return False

    elif customer_searched == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return False

    return True


def add_person_errors(person, info_customer):
    if person is None:
        print(f'\nSuccessfully registered, log in to use the application!!')

        input("\nPress any key to continue...")
        return True

    elif person == get_value(DatabaseErrors.CONNECTION_LOST):
        print(f"\nCan't sign up the application has lost the connection with the server")

        input("\nPress any key to continue...")
        return False

    elif person == get_value(DatabaseErrors.EMAIL_ALREADY_EXIST):
        print(f'\nThere is already an user with the email: {info_customer[2]}')

        input("\nPress any key to continue...")
        return False


def add_customer_errors(person):
    if person == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return False


def prod_bought_errors(product, money):
    if product is None:
        print("\nThe product doesn't exist")

        input("\nPress any key to continue...")
        return False

    elif product == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connectio with the server")

        input("\nPress any key to exit...")
        return False

    elif money < product[2]:
        print("\nYou don't have enough money")

        input("\nPress any key to continue...")
        return False

    return True


def view_orders_errors(order):
    if order == -1:
        print("\nYou don't have orders")

        input("\nPress any key to continue...")
        return False

    elif not len(order):
        print("\nYou don't have any orders")

        input("\nPress any key to continue...")
        return False

    elif order == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return False

    return True


def search_orders_errors(orders, order_name):
    if orders == -1:
        conn_lost_msg()
        return False

    elif not len(orders):
        print(f"\nThere isn't any orders with the product: {order_name}")

        input("\nPress any key to continue...")
        return False

    elif orders == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return False

    return True


def signin_customer_errors(login_cred, database, cursor):
    db_cred = database.get_customer_info(cursor, login_cred[0])

    if db_cred is None:
        print("\nSomething went wrong with username and password")

        input("\nPress any key to continue...")
        return False

    elif db_cred == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return False

    # check the password of the database and the password of the login
    elif db_cred[1] == login_cred[1]:
        print(f"\nIt's nice to see you again {db_cred[2]}")

        input("\nPress any key to continue...")
        return Person(db_cred[2], db_cred[3], db_cred[0], db_cred[1], db_cred[4], db_cred[5])

    print("\nSomething went wrong with username and password")

    input("\nPress any key to continue...")
    return False


def signin_super_root_errors(login_cred, super_root):
    if super_root == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return False

    elif login_cred[0] == super_root[0] and login_cred[1] == super_root[1]:
        print("\nlogged in as super root")

        input("\nPress any key to continue...")
        return True

    print("\nSomething went wrong with username or password")

    input("\nPress any key to continue...")
    return False


def signin_root_errors(log_in_cred, db_cred):
    # check if the connection has lost
    if db_cred is None:
        print("\nSomething went wrong with username or password")

        input("\nPress any key to continue...")
        return False

    elif db_cred == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return False

    # check email and password
    elif log_in_cred[0] == db_cred[1] and log_in_cred[1] == db_cred[2]:
        print(f"\nIt's nice to see you {db_cred[0]}")

        input("\nPress any key to continue...")
        return True

    print("\nSomething went wrong with the username or password")

    input("\nPress any key to continue...")
    return False


def rmv_errors(removed_product):
    if removed_product == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return False

    return True


def update_name_product_errors(error, prod_name):
    if error == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return

    elif error == get_value(DatabaseErrors.DATA_ERROR):
        print(f"\nCan't update the product with the name: {prod_name}")

        input("\nPress any key to continue...")
        return


def update_qnt_errors(error):
    if error == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return

    elif error == get_value(DatabaseErrors.DATA_ERROR):
        print("\nCan't add the new quantity")

        input("\nPress any key to continue...")
        return


def update_price_errors(error):
    if error == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return
