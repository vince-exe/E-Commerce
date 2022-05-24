import enum

option_list = ['y', 'yes', 'Y', 'YES', 'YeS', 'YEs']


def clear_screen():
    print("\n" * 15)


def get_value(enum_value):
    return enum_value.value


def get_info_admin(database, cursor):
    log_credentials = (get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)),
                       get_psw(get_value(CredentialsOptions.PSW_MAX_LEN)))

    db_credential = database.get_admin_info(cursor, log_credentials[0])

    return handle_root_conn_errors(log_credentials, db_credential)


def get_super_root_info(database, cursor):
    log_credentials = (get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)),
                       get_psw(get_value(CredentialsOptions.PSW_MAX_LEN)))

    db_credentials = database.get_super_root(cursor)

    return handle_super_root_log(log_credentials, db_credentials)


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
    info = []
    info.append(input("\nInsert the name: "))
    info.append(float(get_price(get_value(PriceOptions.MIN), get_value(PriceOptions.MAX))))
    info.append(int(get_qnt(get_value(QntOptions.MIN), get_value(QntOptions.MAX))))

    return info


def check_answer(option):
    if option in option_list:
        return True

    return False


def print_products(products_list):
    for product in products_list:
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
Password: {customer[4]}
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


class StringOptions(enum.Enum):
    MAX_LEN_STRING = 256
    MIN_LEN_STRING = 0


class CredentialsOptions(enum.Enum):
    EMAIL_MAX_LEN = 20
    PSW_MAX_LEN = 32


class AdminOptions(enum.Enum):
    VIEW_CUSTOMERS = 1
    VIEW_PRODUCTS = 2
    ADD_PRODUCT = 3
    SEARCH_PRODUCT = 4
    DELETE_PRODUCT = 5
    DELETE_CUSTOMER = 6
    SEARCH_CUSTOMER = 7
    EXIT = 8
    EXIT_LOG = 2


class SuperRootOptions(enum.Enum):
    ADD_ADMIN = 1
    DELETE_ADMIN = 2
    SEARCH_ADMIN = 3
    MODIFY_ADMIN = 4
    EXIT = 5


class PriceOptions(enum.Enum):
    MIN = 0.99
    MAX = 9999.00


class QntOptions(enum.Enum):
    MIN = 1
    MAX = 9999


class DatabaseErrors(enum.Enum):
    NAME_ALREADY_EXIST = 0
    CONNECTION_LOST = -1
    ACCESS_DENIED = -2
    DB_EXCEPTION = -3
    DATA_ERROR = -4


class GeneralOptions(enum.Enum):
    SIGN_IN = 1
    SIGN_UP = 2
    EXIT = 3


class GeneralMenuOptions(enum.Enum):
    LOG_AS_ADMIN = 1
    LOG_AS_CUSTOMER = 2
    EXIT = 3
