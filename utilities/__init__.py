DEFAULT_HOST = 'localhost'

DEFAULT_SETUP = True
N0_PSW_SETUP = False

MAX_LEN_STRING = 256
MIN_LEN_STRING = 0

option_list = ['y', 'yes', 'Y', 'YES', 'YeS', 'YEs']

info = ['localhost', 'root', 'MySQL85.#(6@', 'ecommerce']

VALUE_ERROR_MSG = "Option must be a string!!"

LOG_AS_ADMIN = 1
LOG_AS_CUSTOMER = 2

EXIT = 3
EXIT_ADMIN_LOG = 2

SIGN_IN = 1
SIGN_UP = 2

EMAIL_MAX_LEN = 20
PSW_MAX_LEN = 32


def check_answer(option):
    if option in option_list:
        return True

    return False


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


def get_info_admin():
    credentials = (get_email(EMAIL_MAX_LEN), get_psw(PSW_MAX_LEN))

    return credentials


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


def initial_admin_menu():
    exit_ = False

    while not exit_:
        try:
            option = int(input("\n1)Sign In\n2)Exit\n\nInsert option (1 / 2): "))

            if option == SIGN_IN:
                get_info_admin()

            elif option == EXIT_ADMIN_LOG:
                return False
            else:
                print(f"\n{option} is not a valid option!!")

        except ValueError:
            print(f"\n{VALUE_ERROR_MSG}")


def general_menu():
    exit_ = False

    while not exit_:
        try:
            option = int(input("\n1)Log as Admin\n2)Log as Customer\n3)Exit\n\nInsert option (1 / 3): "))

            if option == LOG_AS_ADMIN:
                if not initial_admin_menu():
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
