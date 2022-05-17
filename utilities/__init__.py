DEFAULT_HOST = 'localhost'

DEFAULT_SETUP = True
N0_PSW_SETUP = False

MAX_LEN_STRING = 256
MIN_LEN_STRING = 0

option_list = ['y', 'yes', 'Y', 'YES', 'YeS', 'YEs']


def check_answer(option):
    if option in option_list:
        return True

    return False


def get_information(word, max_, min_):
    info = ''

    while len(info) > max_ or len(info) <= min_:
        info = input(word)

    return info


def get_info():
    info = []

    # check if he wants to connect to the database with the password
    if check_answer(input("\nContinue with the default setup (password required) (y / n): ")):
        info.append(DEFAULT_SETUP)
    else:   # setup the database without the password
        print("\nOkay you will connect to the database without the password :3")
        info.append(N0_PSW_SETUP)

    # check if he wants to change the host
    if check_answer(input("\nThe default host is: localhost, do you want to change it (y / n): ")):
        info.append(input("\nInsert new host: "))
    else:
        info.append(DEFAULT_HOST)

    info.append(get_information('\nInsert the username: ', MAX_LEN_STRING, MIN_LEN_STRING))

    if info[0]:
        info.append(get_information('\nInsert the password: ', MAX_LEN_STRING, MIN_LEN_STRING))

    info.append(get_information('\nInsert the database name: ', MAX_LEN_STRING, MIN_LEN_STRING))

    return info
