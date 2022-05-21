import enum

option_list = ['y', 'yes', 'Y', 'YES', 'YeS', 'YEs']


def get_value(enum_value):
    return enum_value.value


def get_info_admin(database, cursor):
    credentials = (get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN)), get_psw(get_value(CredentialsOptions.PSW_MAX_LEN)))
    root_cred = database.get_admin_info(cursor, 'person', f'email = "{credentials[0]}"')

    if root_cred == get_value(DatabaseErrors.CONNECTION_LOST):
        print(f"\nThe application lost the connection with the server :(")
        return False

    elif not check_validity(credentials, root_cred):
        print(f'\nSomething went wrong with username or password')
        return False
    else:
        print(f"\nIt's nice to see you {root_cred[0]}")
        return True


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


def handle_product_errors(error, prod_info):
    if error == get_value(DatabaseErrors.CONNECTION_LOST):
        print(f"\nCan't add the product: {prod_info} the application lost the connection with the server :(")

        input("\nPress any key to continue...")
        return

    elif error == get_value(DatabaseErrors.NAME_ALREADY_EXIST):
        print(f'\nThere is already a product named: {prod_info[0]}')

        input("\nPress any key to continue...")
        return

    else:
        print(f'\nSuccessfully added the product: {prod_info[0]}')

        input("\nPress any key to continue...")
        return


def handle_db_conn_errors(error, database):
    if error == get_value(DatabaseErrors.ACCESS_DENIED):
        print("\nSomething went wrong with username and password")

        input("\nPress any key to continue...")
        exit(-1)

    elif error == get_value(DatabaseErrors.DB_ERROR):
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
    ADD_ADMIN = 4
    SEARCH_PRODUCT = 5
    DELETE_PRODUCT = 6
    DELETE_CUSTOMER = 7
    SEARCH_CUSTOMER = 8
    EXIT = 9
    EXIT_LOG = 2


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
    DB_ERROR = -3


class GeneralOptions(enum.Enum):
    SIGN_IN = 1
    SIGN_UP = 2
    EXIT = 3


class GeneralMenuOptions(enum.Enum):
    LOG_AS_ADMIN = 1
    LOG_AS_CUSTOMER = 2
    EXIT = 3
