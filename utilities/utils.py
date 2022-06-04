from utilities.enums import *

from errors.handle_errors import signin_super_root_errors, signin_root_errors

from datetime import date

import os, json

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
        money = float(input(f"{Colors.BLU}{Colors.BOLD}\nMoney: {Colors.RESET}"))

    return money


def get_info_admin(database):
    log_credentials = (get_email(CredentialsOptions.EMAIL_MAX_LEN),
                       get_psw(CredentialsOptions.PSW_MAX_LEN))

    db_credential = database.get_admin_info(log_credentials[0])

    return signin_root_errors(log_credentials, db_credential)


def get_info_person():
    log_credentials = [
                       input(f"{Colors.BLU}{Colors.BOLD}\nFirst Name: {Colors.RESET}"),
                       input(f"{Colors.BLU}{Colors.BOLD}\nLast Name: {Colors.RESET}"),
                       get_email(CredentialsOptions.EMAIL_MAX_LEN),
                       get_psw(CredentialsOptions.PSW_MAX_LEN),
                       get_money(MoneyOptions.MIN, MoneyOptions.MAX)
                       ]

    return log_credentials


def get_psw_email_customer():
    log_credentials = [
                      get_email(CredentialsOptions.EMAIL_MAX_LEN),
                      get_psw(CredentialsOptions.PSW_MAX_LEN)
                      ]

    return log_credentials


def get_super_root_info(database):
    log_credentials = (get_email(CredentialsOptions.EMAIL_MAX_LEN),
                       get_psw(CredentialsOptions.PSW_MAX_LEN))

    db_credentials = database.get_super_root()

    return signin_super_root_errors(log_credentials, db_credentials)


def get_email(max_len):
    while True:
        email_ = input(f"{Colors.BLU}{Colors.BOLD}\nEmail: {Colors.RESET}")

        if email_.endswith("@gmail.com") and len(email_) < max_len:
            return email_


def get_psw(max_len):
    psw = ''
    while len(psw) <= 0 or len(psw) > max_len:
        psw = input(f"{Colors.BLU}{Colors.BOLD}\nPassword: {Colors.RESET}")

    return psw


def get_qnt(min_, max_):
    qnt = -1
    while qnt < min_ or qnt > max_:
        try:
            qnt = int(input(f"{Colors.BLU}{Colors.BOLD}\nInsert the quantity: {Colors.RESET}"))
        except ValueError:
            print(f"{Colors.RED}{Colors.BOLD}\nQuantity must be a number!!{Colors.RESET}")

    return qnt


def get_price(min_, max_):
    price = -1.0

    while price < min_ or price > max_:
        try:
            price = float(input(f"{Colors.BLU}{Colors.BOLD}\nPrice: {Colors.RESET}"))
        except ValueError:
            print(f"{Colors.RED}{Colors.BOLD}\nPrice must be a number!!{Colors.RESET}")

    return price


def get_order_id():
    id_ = -1
    while id_ < 0:
        try:
            id_ = int(input(f"{Colors.BLU}{Colors.BOLD}\nOrder Id: {Colors.RESET}"))

        except ValueError:
            print(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Id must be a number")

    return id_


def get_product_info():
    os.system('cls||clear')
    info = [
            input(f"{Colors.BLU}{Colors.BOLD}\nProduct Name: {Colors.RESET}"),
            float(get_price(PriceOptions.MIN, PriceOptions.MAX)),
            int(get_qnt(QntOptions.MIN, QntOptions.MAX))
            ]

    return info


def get_id_product():
    id_ = -1
    while id_ <= 0:
        try:
            id_ = int(input(f"{Colors.BLU}{Colors.BOLD}\nProduct Id: {Colors.RESET}"))

        except ValueError:
            print(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Id must be a number!!")

    return id_


def get_id_root():
    id_ = -1
    while id_ <= 1:
        try:
            os.system('cls||clear')
            id_ = int(input(f"{Colors.BLU}{Colors.BOLD}\nId: {Colors.RESET}"))

            if id_ == 1:
                input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}"
                      f"Can not effectuate any action on the super root id!!\n\nPress any key to continue...")

        except ValueError:
            input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Id must be a number!!"
                  f"\n\nPress any key to continue...")

    return id_


def get_prod_qnt():
    qnt = -1
    while qnt <= 0:
        try:
            os.system('cls||clear')
            qnt = int(input(f"{Colors.BLU}{Colors.BOLD}\nNew Quantity: {Colors.RESET}"))

        except ValueError:
            input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Quantity must be a number!")

    return qnt


def get_prod_price(max_):
    price = 0
    while price <= 0 or price > max_:
        try:
            os.system('cls||clear')
            price = float(input(f"\n{Colors.BLU}{Colors.BOLD}New Price: {Colors.RESET}"))

        except ValueError:
            input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Price must be a number!")

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
{Colors.GREEN}{Colors.BOLD}Id: {Colors.RESET}{product[0]}\n
{Colors.BLU}{Colors.BOLD}Name{Colors.RESET}: {product[1]}\n
{Colors.GREEN}{Colors.BOLD}Price: {Colors.RESET}{product[2]}\n
{Colors.BLU}{Colors.BOLD}Quantity: {Colors.RESET}Out of stock
* - - - - - - - - - - - - - *
            ''')
        else:
            print(f'''
* - - - - - - - - - - - - - *
{Colors.GREEN}{Colors.BOLD}Id: {Colors.RESET}{product[0]}\n
{Colors.BLU}{Colors.BOLD}Name: {Colors.RESET}{product[1]}\n
{Colors.GREEN}{Colors.BOLD}Price: {Colors.RESET}{product[2]}\n
{Colors.BLU}{Colors.BOLD}Quantity: {Colors.RESET}{product[3]}
* - - - - - - - - - - - - - *
            ''')


def print_customers(customer_list):
    for customer in customer_list:
        print(f'''
* - - - - - - - - - - - - - *
{Colors.GREEN}{Colors.BOLD}Id: {Colors.RESET}{customer[0]}\n
{Colors.BLU}{Colors.BOLD}First Name: {Colors.RESET}{customer[1]}\n
{Colors.GREEN}{Colors.BOLD}Last Name: {Colors.RESET}{customer[2]}\n
{Colors.BLU}{Colors.BOLD}Email: {Colors.RESET}{customer[3]}\n
{Colors.GREEN}{Colors.BOLD}Password: {Colors.RESET}{customer[4]}\n
{Colors.BLU}{Colors.BOLD}Money: {Colors.RESET}{customer[5]}
* - - - - - - - - - - - - - *
            ''')


def print_orders(orders_list):
    for order in orders_list:
        print(f'''
* - - - - - - - - - - - - - *
{Colors.GREEN}{Colors.BOLD}First Name: {Colors.RESET}{order[0]}\n
{Colors.BLU}{Colors.BOLD}Last Name: {Colors.RESET}{order[1]}\n
{Colors.GREEN}{Colors.BOLD}Product Name: {Colors.RESET}{order[2]}\n
{Colors.BLU}{Colors.BOLD}Date: {Colors.RESET}{order[3]}\n
{Colors.GREEN}{Colors.BOLD}Order Id: {Colors.RESET}{order[4]}\n
{Colors.BLU}{Colors.BOLD}Product Id: {Colors.RESET}{order[5]}
* - - - - - - - - - - - - - *
              ''')


def print_admins(admin_list):
    for admin in admin_list:
        print(f'''
* - - - - - - - - - - - - - *
{Colors.GREEN}{Colors.BOLD}Id: {Colors.RESET}{admin[0]}\n
{Colors.BLU}{Colors.BOLD}First Name: {Colors.RESET}{admin[1]}\n
{Colors.GREEN}{Colors.BOLD}Last Name: {Colors.RESET}{admin[2]}\n
{Colors.BLU}{Colors.BOLD}Email: {Colors.RESET}{admin[3]}\n
{Colors.GREEN}{Colors.BOLD}Password: {Colors.RESET}{admin[4]}\n
{Colors.BLU}{Colors.BOLD}Money: {Colors.RESET}{admin[5]}
* - - - - - - - - - - - - - *
              ''')


def print_logo():
    os.system('cls||clear')
    print(f"""\n{Colors.MAGENTA}{Colors.BOLD}
            ███████╗        █████╗   █████╗  ███╗   ███╗ ███╗   ███╗ ███████╗ ██████╗   █████╗  ███████╗
            ██╔════╝       ██╔══██╗ ██╔══██╗ ████╗ ████║ ████╗ ████║ ██╔════╝ ██╔══██╗ ██╔══██╗ ██╔════╝
            █████╗  █████╗ ██║  ╚═╝ ██║  ██║ ██╔████╔██║ ██╔████╔██║ █████╗   ██████╔╝ ██║  ╚═╝ █████╗
            ██╔══╝  ╚════╝ ██║  ██╗ ██║  ██║ ██║╚██╔╝██║ ██║╚██╔╝██║ ██╔══╝   ██╔══██╗ ██║  ██╗ ██╔══╝
            ███████╗       ╚█████╔╝ ╚█████╔╝ ██║ ╚═╝ ██║ ██║ ╚═╝ ██║ ███████╗ ██║  ██║ ╚█████╔╝ ███████╗
            ╚══════╝        ╚════╝   ╚════╝  ╚═╝     ╚═╝ ╚═╝     ╚═╝ ╚══════╝ ╚═╝  ╚═╝  ╚════╝  ╚══════╝
    {Colors.RESET}""")
