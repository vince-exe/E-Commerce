from utilities.enums import *
from errors.handle_errors import signin_super_root_errors, signin_root_errors
from datetime import date

import os

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


def get_money(min_, max_):
    money = -1.00
    while money < min_ or money > max_:
        money = float(input("\nInsert the amount of money: "))

    return money


def get_info_admin(database):
    log_credentials = (get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)),
                       get_psw(get_value(CredentialsOptions.PSW_MAX_LEN)))

    db_credential = database.get_admin_info(log_credentials[0])

    return signin_root_errors(log_credentials, db_credential)


def get_info_person():
    log_credentials = [
                       input("\nInsert the First Name: "),
                       input("\nInsert the Last Name: "),
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


def get_super_root_info(database):
    log_credentials = (get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)),
                       get_psw(get_value(CredentialsOptions.PSW_MAX_LEN)))

    db_credentials = database.get_super_root()

    return signin_super_root_errors(log_credentials, db_credentials)


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


def get_order_id():
    id_ = -1
    while id_ < 0:
        try:
            id_ = int(input("\nInsert the id of the order: "))

        except ValueError:
            print("\nId must be a number")

    return id_


def get_product_info():
    os.system('cls||clear')
    info = [
            input("\nInsert the name: "),
            float(get_price(get_value(PriceOptions.MIN), get_value(PriceOptions.MAX))),
            int(get_qnt(get_value(QntOptions.MIN), get_value(QntOptions.MAX)))
            ]

    return info


def get_id_product():
    id_ = -1
    while id_ <= 0:
        try:
            id_ = int(input("\nInsert the product id: "))

        except ValueError:
            print("\nId must be a number!!")

    return id_


def get_id_root():
    id_ = -1
    while id_ <= 1:
        try:
            os.system('cls||clear')
            id_ = int(input("\nInsert the id: "))

            if id_ == 1:
                input("\nCan not effectuate any action on the super root id!!\n\nPress any key to continue...")

        except ValueError:
            input("\nId must be a number!!\n\nPress any key to continue...")

    return id_


def get_prod_qnt():
    qnt = -1
    while qnt <= 0:
        try:
            os.system('cls||clear')
            qnt = int(input("\nInsert the quantity: "))

        except ValueError:
            input("\nQuantity must be a number!")

    return qnt


def get_prod_price(max_):
    price = 0
    while price <= 0 or price > max_:
        try:
            os.system('cls||clear')
            price = float(input("\nInsert the price: "))

        except ValueError:
            input("\nPrice must be a number!")

    return price


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


def print_admins(admin_list):
    for admin in admin_list:
        print(f'''
* - - - - - - - - - - - - - *
Id: {admin[0]}\n
First Name: {admin[1]}\n
Last Name: {admin[2]}\n
Email: {admin[3]}\n
Password: {admin[4]}\n
Money: {admin[5]}
* - - - - - - - - - - - - - *
              ''')
