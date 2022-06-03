class StringOptions:
    MAX_LEN_STRING = 256
    MIN_LEN_STRING = 0


class CredentialsOptions:
    EMAIL_MAX_LEN = 20
    PSW_MAX_LEN = 32


class AdminOptions:
    VIEW_CUSTOMERS = 1
    VIEW_PRODUCTS = 2
    ADD_PRODUCT = 3
    MODIFY_PRODUCT = 4
    SEARCH_PRODUCT = 5
    DELETE_PRODUCT = 6
    DELETE_CUSTOMER = 7
    SEARCH_CUSTOMER = 8
    EXIT = 9
    EXIT_LOG = 2


class CustomerOptions:
    VIEW_PRODUCTS = 1
    SEARCH_PRODUCT = 2
    BUY_PRODUCT = 3
    CHECK_CREDIT = 4
    ADD_CREDIT = 5
    VIEW_ORDERS = 6
    DELETE_ORDERS = 7
    SEARCH_ORDERS = 8
    EXIT = 9


class SuperRootOptions:
    ADD_ADMIN = 1
    DELETE_ADMIN = 2
    SEARCH_ADMIN = 3
    MODIFY_ADMIN = 4
    VIEW_ADMINS = 5
    EXIT = 6


class PriceOptions:
    MIN = 0.99
    MAX = 9999.00


class QntOptions:
    MIN = 1
    MAX = 9999


class DatabaseErrors:
    NAME_ALREADY_EXIST = 0
    CONNECTION_LOST = -1
    ACCESS_DENIED = -2
    DB_EXCEPTION = -3
    DATA_ERROR = -4
    EMAIL_ALREADY_EXIST = -5
    OUT_OF_STOCK = -6
    NO_ADMIN_FOUND = -7


class ModifyAdminOptions:
    MODIFY_FIRST_NAME = 1
    MODIFY_LAST_NAME = 2
    MODIFY_EMAIL = 3
    MODIFY_PASSWORD = 4
    MODIFY_MONEY = 5
    EXIT = 6


class GeneralOptions:
    SIGN_IN = 1
    SIGN_UP = 2
    EXIT = 3


class GeneralMenuOptions:
    LOG_AS_ADMIN = 1
    LOG_AS_CUSTOMER = 2
    EXIT = 3


class MoneyOptions:
    MIN = 5
    MAX = 100000000


class Colors:
    GREEN = "\u001b[32m"
    RESET = "\u001b[0m"
    MAGENTA = "\u001b[35m"
    RED = "\u001b[31m"
    YELLOW = "\u001b[33m"
    BLU = "\033[94m"
    BOLD = "\033[1m"
