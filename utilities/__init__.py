from utilities.setups import *

DEFAULT_HOST = 'localhost'

option_list = ['y', 'yes', 'Y', 'YES', 'YeS', 'YEs']

info = ['localhost', 'root', 'mySQLroot45.&ciao#.', 'ecommerce']

VALUE_ERROR_MSG = "Option must be a string!!"

LOG_AS_ADMIN = 1
LOG_AS_CUSTOMER = 2

EXIT = 3
EXIT_ADMIN_LOG = 2

SIGN_IN = 1
SIGN_UP = 2


def check_answer(option):
    if option in option_list:
        return True

    return False


def check_validity(log_in_cred, db_cred):
    if db_cred is None:
        return False

    # check the password
    elif log_in_cred[1] != db_cred[3]:
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


def get_info_admin(database, cursor):
    credentials = (get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)), get_psw(get_value(CredentialsOptions.PSW_MAX_LEN)))
    root_cred = database.get_admin_info(cursor, 'person', f'email = "{credentials[0]}"')

    if not check_validity(credentials, root_cred):
        print(f'\nSomething went wrong with username or password')
        return False
    else:
        print(f"\nIt's nice to see you {root_cred[0]}")
        return True


def initial_customer_menu():
    exit_ = False

    while not exit_:
        try:
            option = int(input("\n1)Sign In\n2)Sign Up\n3)exit\n\nInsert option (1 / 3): "))

            if option == SIGN_IN:
                pass
            elif option == SIGN_UP:
                pass
            elif option == EXIT:
                return False
            else:
                print(f"\n{option} is not a valid option!!")

        except ValueError:
            print(f"\n{VALUE_ERROR_MSG}")


def admin_menu():
    exit_ = False
    while not exit_:
        try:
            option = int(input(("\n1)View All Customers"
                                "\n2)View All Products"
                                "\n3)Add Product"
                                "\n4)Add Admin"
                                "\n5)Search Product (info)"
                                "\n6)Delete Product"
                                "\n7)Delete Customer"
                                "\n8)Search Customer"
                                "\n9)Exit"
                                "\n\nInsert option (1 / 9): "
                                )))

            if option == get_value(AdminOptions.VIEW_CUSTOMERS):
                pass

            elif option == get_value(AdminOptions.VIEW_PRODUCTS):
                pass

            elif option == get_value(AdminOptions.ADD_PRODUCT):
                pass

            elif option == get_value(AdminOptions.ADD_ADMIN):
                pass

            elif option == get_value(AdminOptions.SEARCH_PRODUCT):
                pass

            elif option == get_value(AdminOptions.DELETE_PRODUCT):
                pass

            elif option == get_value(AdminOptions.DELETE_CUSTOMER):
                pass

            elif option == get_value(AdminOptions.SEARCH_CUSTOMER):
                pass

            elif option == get_value(AdminOptions.EXIT):
                exit_ = True
                break

            else:
                print(f"{option} must be a number!!")

        except ValueError:
            print("\nOption can't be a string!!")


def initial_admin_menu(database, cursor):
    exit_ = False

    while not exit_:
        try:
            option = int(input("\n1)Sign In\n2)Exit\n\nInsert option (1 / 2): "))

            if option == SIGN_IN:
                if get_info_admin(database, cursor):
                    admin_menu()

            elif option == EXIT_ADMIN_LOG:
                return False
            else:
                print(f"\n{option} is not a valid option!!")

        except ValueError:
            print(f"\n{VALUE_ERROR_MSG}")


def general_menu(database, cursor):
    exit_ = False

    while not exit_:
        try:
            option = int(input("\n1)Log as Admin\n2)Log as Customer\n3)Exit\n\nInsert option (1 / 3): "))

            if option == LOG_AS_ADMIN:
                if not initial_admin_menu(database, cursor):
                    return False

            elif option == LOG_AS_CUSTOMER:
                if not initial_customer_menu():
                    return False

            elif option == EXIT:
                return False
            else:
                print(f"\n{option} is not a correct option!!")

        except ValueError:
            print(f"\n{VALUE_ERROR_MSG}")
