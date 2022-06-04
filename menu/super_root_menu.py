from errors.handle_errors import *

from utilities.enums import *
from utilities.utils import get_info_person, print_admins, get_id_root, get_email, get_psw, get_money

import os


def print_admin_menu(database):
    limit = 5
    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}View Admins (5 at time)"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 / 2): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                check = database.get_admins(limit)

                if print_admin_errors(check):
                    print_admins(check)
                    input("\n\nPress any key to continue...")
                    limit += 5

            elif option == 2:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)


def search_admin_menu(database, admin_name):
    limit = 5
    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}View Admin"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 / 2): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                check = database.get_admin_searched(admin_name, limit)

                if search_admin_errors(check, admin_name):
                    print_admins(check)
                    input("\n\nPress any key to continue...")
                    limit += 5

                else:
                    return

            elif option == 2:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)


def modify_admin_menu(database, id_):
    admin_id = database.get_person_id_super_root(id_)

    if admin_id is None:
        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}No admin found with the id: [{id_}]"
              f"\n\nPress any key to continue...")
        return

    elif admin_id == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}Modify First Name"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Modify Last Name"
                               f"{Colors.BLU}{Colors.BOLD}\n3) {Colors.RESET}Modify Email"
                               f"{Colors.BLU}{Colors.BOLD}\n4) {Colors.RESET}Modify Password"
                               f"{Colors.BLU}{Colors.BOLD}\n5) {Colors.RESET}Modify Money"
                               f"{Colors.BLU}{Colors.BOLD}\n6) {Colors.RESET}Exit"
                               f"{Colors.BLU}{Colors.BOLD}\n\nInsert option (1 / 6): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == ModifyAdminOptions.MODIFY_FIRST_NAME:  # Modify First Name
                first_name = input(f"{Colors.BLU}{Colors.BOLD}\nFirst Name: {Colors.RESET}")
                update_firstname_person(database.update_person_first_name(first_name, admin_id), first_name)

            elif option == ModifyAdminOptions.MODIFY_LAST_NAME:  # Modify Last Name
                last_name = input(f"{Colors.BLU}{Colors.BOLD}\nLast Name: {Colors.RESET}")
                update_lastname_person(database.update_person_last_name(last_name, admin_id), last_name)

            elif option == ModifyAdminOptions.MODIFY_EMAIL:  # Modify Email
                email = get_email(CredentialsOptions.EMAIL_MAX_LEN)
                update_email_person(database.update_person_email(email, admin_id), email)

            elif option == ModifyAdminOptions.MODIFY_PASSWORD:  # Modify Password
                psw = get_psw(CredentialsOptions.PSW_MAX_LEN)
                update_password_person(database.update_person_password(psw, admin_id))

            elif option == ModifyAdminOptions.MODIFY_MONEY:  # Modify Money
                money = get_money(MoneyOptions.MIN, MoneyOptions.MAX)
                update_money_person(database.update_person_money(money, admin_id))

            elif option == ModifyAdminOptions.EXIT:  # Exit
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)


def super_root_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}Add Admin"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Delete Admin"
                               f"{Colors.BLU}{Colors.BOLD}\n3) {Colors.RESET}Search Admin"
                               f"{Colors.BLU}{Colors.BOLD}\n4) {Colors.RESET}Modify Admin"
                               f"{Colors.BLU}{Colors.BOLD}\n5) {Colors.RESET}View Admins"
                               f"{Colors.BLU}{Colors.BOLD}\n6) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 / 6): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == SuperRootOptions.ADD_ADMIN:  # Add Admin
                info = get_info_person()
                if add_admin_errors(database.add_person(info), info):
                    database.add_root()

            elif option == SuperRootOptions.DELETE_ADMIN:  # Delete Admin
                id_ = get_id_root()
                delete_admin_errors(database.delete_admin(id_), id_)

            elif option == SuperRootOptions.SEARCH_ADMIN:  # Search Admin
                admin_name = input(f"{Colors.BLU}{Colors.BOLD}\nFirst Name: {Colors.RESET}")
                search_admin_menu(database, admin_name)

            elif option == SuperRootOptions.MODIFY_ADMIN:  # Modify Admin
                id_ = get_id_root()
                modify_admin_menu(database, id_)
                pass

            elif option == SuperRootOptions.VIEW_ADMINS:  # View Admins
                print_admin_menu(database)

            elif option == SuperRootOptions.EXIT:  # Exit
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)
