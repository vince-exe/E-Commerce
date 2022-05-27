import enum


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
    EMAIL_ALREADY_EXIST = -5


class GeneralOptions(enum.Enum):
    SIGN_IN = 1
    SIGN_UP = 2
    EXIT = 3


class GeneralMenuOptions(enum.Enum):
    LOG_AS_ADMIN = 1
    LOG_AS_CUSTOMER = 2
    EXIT = 3


class CustomerOptions(enum.Enum):
    VIEW_PRODUCTS = 1
    SEARCH_PRODUCT = 2
    BUY_PRODUCT = 3
    CHECK_CREDIT = 4
    ADD_CREDIT = 5
    VIEW_ORDERS = 6
    DELETE_ORDERS = 7
    SEARCH_ORDERS = 8
    EXIT = 9


class MoneyOptions(enum.Enum):
    MIN = 5
    MAX = 100000000
