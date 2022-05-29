from utilities.enums import *
from person.person import Person
from datetime import date

option_list = ['y', 'yes', 'Y', 'YES', 'YeS', 'YEs']


def get_date():
    year = date.today().year

    month = int(date.today().month)
    tmp_month = month

    if month <= 9:
        month = f'0{tmp_month}'
    else:
        tmp_month = str(month)
        month = tmp_month

    day = int(date.today().day)
    tmp_day = day

    if day <= 9:
        day = f'0{tmp_day}'
    else:
        tmp_day = str(day)
        day = tmp_day

    complete_date = f'{year}/{month}/{day}'
    return complete_date


def clear_screen():
    print("\n" * 15)


def get_value(enum_value):
    return enum_value.value


def get_name_surname(max_, string):
    name = ""
    while len(name) <= 0 or len(name) > max_:
        name = input(f"\n{string}")

    return name


def get_money(min_, max_):
    money = -1.00
    while money < min_ or money > max_:
        money = float(input("\nInsert the amount of money: "))

    return money


def get_info_admin(database, cursor):
    log_credentials = (get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)),
                       get_psw(get_value(CredentialsOptions.PSW_MAX_LEN)))

    db_credential = database.get_admin_info(cursor, log_credentials[0])

    return handle_root_conn_errors(log_credentials, db_credential)


def get_info_customer():
    log_credentials = [
                       get_name_surname(get_value(CredentialsOptions.EMAIL_MAX_LEN), "First Name: "),
                       get_name_surname(get_value(CredentialsOptions.EMAIL_MAX_LEN), "Last Name: "),
                       get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)),
                       get_psw(get_value(CredentialsOptions.PSW_MAX_LEN)),
                       get_money(get_value(MoneyOptions.MIN), get_value(MoneyOptions.MAX))
                       ]

    return log_credentials


def get_psw_email_customer():
    log_credentials = [
                      get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)),
                      get_psw(get_value(CredentialsOptions.PSW_MAX_LEN))
                      ]

    return log_credentials


def get_super_root_info(database, cursor):
    log_credentials = (get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)),
                       get_psw(get_value(CredentialsOptions.PSW_MAX_LEN)))

    db_credentials = database.get_super_root(cursor)

    return handle_super_root_log(log_credentials, db_credentials)


def handle_sign_in_customer(login_cred, database, cursor):
    db_cred = database.get_customer_info(cursor, login_cred[0])

    if db_cred is None:
        print("\nSomething went wrong with username and password")

        input("\nPress any key to continue...")
        return False

    elif db_cred == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return False

    # check the password of the database and the password of the login
    elif db_cred[1] == login_cred[1]:
        print(f"\nIt's nice to see you again {db_cred[2]}")

        input("\nPress any key to continue...")
        return Person(db_cred[2], db_cred[3], db_cred[0], db_cred[1], db_cred[4], db_cred[5])

    print("\nSomething went wrong with username and password")

    input("\nPress any key to continue...")
    return False


def handle_super_root_log(login_cred, super_root):
    if super_root == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return False

    elif login_cred[0] == super_root[0] and login_cred[1] == super_root[1]:
        print("\nlogged in as super root")

        input("\nPress any key to continue...")
        return True

    print("\nSomething went wrong with username or password")

    input("\nPress any key to continue...")
    return False


def handle_root_conn_errors(log_in_cred, db_cred):
    # check if the connection has lost
    if db_cred is None:
        print("\nSomething went wrong with username or password")

        input("\nPress any key to continue...")
        return False

    elif db_cred == get_value(DatabaseErrors.CONNECTION_LOST):
        print(f"\nThe application has lost the connection with the server :(")

        input("\nPress any key to continue...")
        return False

    # check email and password
    elif log_in_cred[0] == db_cred[1] and log_in_cred[1] == db_cred[2]:
        print(f"\nIt's nice to see you {db_cred[0]}")

        input("\nPress any key to continue...")
        return True

    print("\nSomething went wrong with the username or password")

    input("\nPress any key to continue...")
    return False


def handle_rmv_errors(removed_product):
    if removed_product == get_value(DatabaseErrors.CONNECTION_LOST):
        print(f"\nThe application has lost the connection with the server :(")

        input("\nPress any key to continue...")
        return False

    return True


def get_email(max_len):
    while True:
        email_ = input("\nInsert the email: ")

        if email_.endswith("@gmail.com") and len(email_) < max_len:
            return email_


def get_psw(max_len):
    psw = ''
    while len(psw) <= 0 or len(psw) > max_len:
        psw = input("\nInsert the password: ")

    return psw


def get_qnt(min_, max_):
    qnt = -1
    while qnt < min_ or qnt > max_:
        try:
            qnt = int(input("\nInsert the quantity: "))
        except ValueError:
            print("\nQuantity must be a number")

    return qnt


def get_price(min_, max_):
    price = -1.0

    while price < min_ or price > max_:
        try:
            price = float(input("\nPrice: "))
        except ValueError:
            print("\nPrice must be a number!!")

    return price


def get_product_info():
    info = [
            input("\nInsert the name: "),
            float(get_price(get_value(PriceOptions.MIN), get_value(PriceOptions.MAX))),
            int(get_qnt(get_value(QntOptions.MIN), get_value(QntOptions.MAX)))
            ]

    return info


def check_answer(option):
    if option in option_list:
        return True

    return False


def print_products(products_list):
    for product in products_list:
        if product[3] <= 0:
            print(f'''
* - - - - - - - - - - - - - *
Id: {product[0]}\n
Name: {product[1]}\n
Price: {product[2]}\n
Quantity: Out of stock
* - - - - - - - - - - - - - *
            ''')
        else:
            print(f'''
* - - - - - - - - - - - - - *
Id: {product[0]}\n
Name: {product[1]}\n
Price: {product[2]}\n
Quantity: {product[3]}
* - - - - - - - - - - - - - *
            ''')


def print_customers(customer_list):
    for customer in customer_list:
        print(f'''
* - - - - - - - - - - - - - *
Id: {customer[0]}\n
First Name: {customer[1]}\n
Last Name: {customer[2]}\n
Email: {customer[3]}\n
Password: {customer[4]}\n
Money: {customer[5]}
* - - - - - - - - - - - - - *
            ''')


def print_orders(orders_list):
    for order in orders_list:
        print(f'''
* - - - - - - - - - - - - - *
First Name: {order[0]}\n
Last Name: {order[1]}\n
Product Name: {order[2]}\n
Date: {order[3]}\n
Order Id: {order[4]}\n
Product Id: {order[5]}
* - - - - - - - - - - - - - *
              ''')


def handle_product_errors(error, prod_info):
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


def handle_db_conn_errors(error, database):
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
        print('\nThe application lost the connection with the server')

        input("\nPress any key to continue...")
        exit(-1)

    # all the controls went fine.
    print(f'\nSuccessfully connected to the database [{database.db_name}]')
    return error


def handle_product_searched(product, product_name):
    if product == -1:
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
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


def handle_customer_searched_errors(customer_searched, customer_name):
    if customer_searched == -1:
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
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


def handle_add_person_errors(person, info_customer):
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


def handle_add_customer(person):
    if person == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return False


def handle_product_bought(product, money):
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


def handle_view_orders(order):
    if order == -1:
        print("\nYou don't have orders")

        input("\nPress any key to continue...")
        return False

    elif order == get_value(DatabaseErrors.CONNECTION_LOST):
        print("\nThe application has lost the connection with the server")

        input("\nPress any key to continue...")
        return False

    return True
