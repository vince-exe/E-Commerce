import enum


def get_value(enum_value):
    return enum_value.value


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
