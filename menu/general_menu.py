from utilities.utils import *
from utilities.enums import *

from menu.admin_menu import admin_menu
from menu.super_root_menu import super_root_menu
from menu.customer_menu import customer_menu

from errors.handle_errors import signin_customer_errors, add_person_errors, add_customer_errors

import os


def initial_admin_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}Sign In (Standard Admin)"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Sign In (Super Admin)"
                               f"{Colors.BLU}{Colors.BOLD}\n3) {Colors.RESET}Exit"
                               f"\n\n{Colors.RESET}Insert option (1 / 3): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                if get_info_admin(database):
                    admin_menu(database)

            elif option == 2:
                if get_super_root_info(database):
                    super_root_menu(database)

            elif option == 3:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)


def initial_customer_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}Sign In"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Sign Up"
                               f"{Colors.BLU}{Colors.BOLD}\n3) {Colors.RESET}exit"
                               f"\n\nInsert option (1 / 3): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == GeneralOptions.SIGN_IN:
                person = signin_customer_errors(get_psw_email_customer(), database)
                if person:
                    customer_menu(database, person)

            elif option == GeneralOptions.SIGN_UP:
                info_customer = get_info_person()
                if add_person_errors(database.add_person(info_customer), info_customer):
                    add_customer_errors(database.add_customer(info_customer[2]))

            elif option == GeneralOptions.EXIT:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)


def general_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1){Colors.RESET} Log as Admin"
                               f"{Colors.BLU}{Colors.BOLD}\n2){Colors.RESET} Log as Customer"
                               f"{Colors.BLU}{Colors.BOLD}\n3){Colors.RESET} Exit"
                               f"\n\nInsert option (1 / 3): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == GeneralMenuOptions.LOG_AS_ADMIN:
                initial_admin_menu(database)

            elif option == GeneralMenuOptions.LOG_AS_CUSTOMER:
                initial_customer_menu(database)

            elif option == GeneralMenuOptions.EXIT:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)
