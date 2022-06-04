from utilities.enums import *

from person.person import Person


def conn_lost_msg():
    input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RED}{Colors.BOLD}The application has lost the connection"
          f" with the server"
          f"{Colors.RESET}\n\nPress any key to continue...")
    return


def add_prod_errors(error, prod_info):
    if error == DatabaseErrors.CONNECTION_LOST:
        input(f"\n{Colors.RED}{Colors.BOLD}ERROR: {Colors.RESET}Can't add the product: [{prod_info[0]}]"
              f" the application lost the connection with the server :(\n\nPress any key to continue...")
        return

    elif error == DatabaseErrors.NAME_ALREADY_EXIST:
        input(f'{Colors.RED}{Colors.BOLD}\nERROR:  {Colors.RESET}There is already a product named: [{prod_info[0]}]'
              f'\n\nPress any key to continue...')
        return

    elif error == DatabaseErrors.DATA_ERROR:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Can't add this product with name: {prod_info[0]}\n\n"
              f"Press any key to continue...")
        return

    else:
        input(f'{Colors.GREEN}{Colors.BOLD}\nSuccessfully added the product: {Colors.RESET}[{prod_info[0]}]\n\n'
              f'Press any key to continue...')
        return


def db_conn_errors(error, database):
    if error is None:
        input(f"{Colors.RED}{Colors.BOLD}\n\t\t\t\t\tERROR: {Colors.RESET}The server is unreachable"
              f"\n\n\t\t\t\t\t  Press any key to continue...")
        exit(-1)

    elif error == DatabaseErrors.ACCESS_DENIED:
        input(f"{Colors.RED}{Colors.BOLD}\n\t\t\t\tERROR: {Colors.RESET}Something went wrong with username and password"
              f"\n\n\t\t\t\t\t      Press any key to continue...")
        exit(-1)

    elif error == DatabaseErrors.DB_EXCEPTION:
        input(f'{Colors.RED}{Colors.BOLD}\n\t\t\t\tERROR: {Colors.RESET}There is no database with the name: [{database.db_name}]'
              f'\n\n\t\t\t\t\t  Press any key to continue...')
        exit(-1)

    elif error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        exit(-1)

    # all the controls went fine.
    input(f'\n\t\t\t\t{Colors.GREEN}{Colors.BOLD}Successfully connected to the database'
          f' [{database.db_name}]..{Colors.RESET}')
    return error


def prod_searched_errors(product, product_name):
    if product == -1:
        conn_lost_msg()
        return False

    elif not len(product):
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}No product named: [{product_name}]"
              f"\n\nPress any key to continue...")
        return False

    elif product == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    return True


def customer_searched_errors(customer_searched, customer_name):
    if customer_searched == -1:
        conn_lost_msg()
        return False

    elif not len(customer_searched):
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}No customer named: [{customer_name}]"
              f"\n\nPress any key to continue...")
        return False

    elif customer_searched == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    return True


def add_person_errors(person, info_customer):
    if person is None:
        input(f'{Colors.GREEN}{Colors.BOLD}\nSuccessfully registered, log in to use the application!!{Colors.RESET}'
              f'\n\nPress any key to continue....')
        return True

    elif person == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    elif person == DatabaseErrors.EMAIL_ALREADY_EXIST:
        input(f'{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}There is already an user with the email:'
              f' [{info_customer[2]}]\n\nPress any key to continue...')
        return False

    elif person == DatabaseErrors.DATA_ERROR:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}First Name or Last Name too long"
              f"\n\nPress any key to continue...")
        return False


def add_customer_errors(person):
    if person == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False


def prod_bought_errors(product, money):
    if product is None:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}The product doesn't exist"
              f"\n\nPress any key to continue...")
        return False

    elif product == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    elif money < product[2]:
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}You don't have enough money"
              f"\n\nPress any key to continue...")
        return False

    return True


def view_orders_errors(order):
    if order == -1:
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}You don't have orders"
              f"\n\nPress any key to continue...")
        return False

    elif not len(order):
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}You don't have any orders"
              f"\n\nPress any key to continue...")
        return False

    elif order == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    return True


def search_orders_errors(orders, order_name):
    if orders == -1:
        conn_lost_msg()
        return False

    elif not len(orders):
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}There isn't any orders with the product: "
              f"[{order_name}]\n\nPress any key to continue...")
        return False

    elif orders == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    return True


def signin_customer_errors(login_cred, database):
    db_cred = database.get_customer_info(login_cred[0])

    if db_cred is None:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Something went wrong with username and password"
              f"\n\nPress any key to continue...")
        return False

    elif db_cred == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    # check the password of the database and the password of the login
    elif db_cred[1] == login_cred[1]:
        input(f"{Colors.GREEN}{Colors.BOLD}\nWELCOME: {Colors.RESET}[{db_cred[2]}]\n\nPress any key to continue...")
        return Person(db_cred[2], db_cred[3], db_cred[0], db_cred[1], db_cred[4], db_cred[5])

    input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Something went wrong with username and password"
          f"\n\nPress any key to continue...")
    return False


def signin_super_root_errors(login_cred, super_root):
    if super_root == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    elif login_cred[0] == super_root[0] and login_cred[1] == super_root[1]:
        input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully logged in as {Colors.RESET}[Super Root]"
              f"\n\nPress any key to continue...")
        return True

    input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Something went wrong with username or password"
          f"\n\nPress any key to continue...")
    return False


def signin_root_errors(log_in_cred, db_cred):
    # check if the connection has lost
    if db_cred is None:
        input(f"{Colors.RED}{Colors.BOLD}\nSomething went wrong with {Colors.RESET}username{Colors.RED}"
              f"{Colors.BOLD} or {Colors.RESET}password\n\nPress any key to continue...")

        return False

    elif db_cred == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    # check email and password
    elif log_in_cred[0] == db_cred[1] and log_in_cred[1] == db_cred[2]:
        input(f"{Colors.GREEN}{Colors.BOLD}\nWelcome: {Colors.RESET}{db_cred[0]}\n\nPress any key to continue...")
        return True

    input(f"{Colors.RED}{Colors.BOLD}\nSomething went wrong with the {Colors.RESET}username{Colors.RED}"
          f"{Colors.RED}{Colors.BOLD} or {Colors.RESET}password\n\nPress any key to continue...")

    return False


def rmv_errors(removed_product):
    if removed_product == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    return True


def update_name_product_errors(error, prod_name):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    elif error == DatabaseErrors.DATA_ERROR:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Can't update the product with the name: [{prod_name}]"
              f"\n\nPress any key to continue...")
        return

    elif error == DatabaseErrors.NAME_ALREADY_EXIST:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}There is already a product named: [{prod_name}]"
              f"\n\nPress any key to continue...")
        return

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully updated the product name"
          f"\n\n{Colors.RESET}Press any key to continue...")


def update_qnt_errors(error):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    elif error == DatabaseErrors.DATA_ERROR:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Can't add the new quantity"
              f"\n\nPress any key to continue...")
        return


def update_price_errors(error):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return


def add_admin_errors(error, info):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    elif error == DatabaseErrors.DATA_ERROR:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}First Name or Last Name too long"
              f"\n\nPress any key to continue...")
        return False

    elif error == DatabaseErrors.EMAIL_ALREADY_EXIST:
        print(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}There is already a person with the email: "
              f"[{info[2]}]"
              f"\n\nPress any key to continue...")
        return False

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully added the New Root{Colors.RESET}\n\nPress any key to continue...")
    return True


def print_admin_errors(error):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    elif not len(error):
        print(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}There are no admins!")
        return False

    return True


def delete_admin_errors(error, id_):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    elif error == DatabaseErrors.NO_ADMIN_FOUND:
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}No admin has the id: [{id_}]"
              f"\n\nPress any key to continue...")
        return

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully removed the admin with id: {Colors.RESET}[{id_}]"
          f"\n\nPress any key to continue...")


def search_admin_errors(error, admin_name):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return False

    elif len(error) == 0:
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}No admin found with the name: [{admin_name}]"
              f"\n\nPress any key to continue...")
        return False

    return True


def update_firstname_person(error, first_name):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    elif error == DatabaseErrors.DATA_ERROR:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Can't update the admin with this name: [{first_name}]"
              f"\n\nPress any key to continue...")
        return

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully update the First Name{Colors.RESET}"
          f"\n\nPress any key to continue...")


def update_lastname_person(error, last_name):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    elif error == DatabaseErrors.DATA_ERROR:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Can't update the admin with this last name: [{last_name}]"
              f"\n\nPress any key to continue...")
        return

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully update the Last Name{Colors.RESET}"
          f"\n\nPress any key to continue...")


def update_email_person(error, email):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    elif error == DatabaseErrors.EMAIL_ALREADY_EXIST:
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}There is already a person with the email: [{email}]"
              f"\n\nPress any key to continue...")
        return

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully update the email{Colors.RESET}"
          f"\n\nPress any key to continue...")


def update_password_person(error):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully update the password{Colors.RESET}"
          f"\n\nPress any key to continue...")


def update_money_person(error):
    if error == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully updated the money{Colors.RESET}\n\nPress any key to continue...")
