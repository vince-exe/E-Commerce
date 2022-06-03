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
            option = int(input("\n1)Sign In (Standard Admin)"
                               "\n2)Sign In (Super Admin)"
                               "\n3)Exit"
                               "\n\nInsert option (1 / 3): "))

            if option == 1:
                if get_info_admin(database):
                    admin_menu(database)

            elif option == 2:
                if get_super_root_info(database):
                    super_root_menu(database)

            elif option == 3:
                return

            else:
                input(f"\n{option} is not a valid option!!\n\nPress any key to continue...")

        except ValueError:
            input("\nOption must be a number\n\nPress any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()


def initial_customer_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input("\n1)Sign In"
                               "\n2)Sign Up"
                               "\n3)exit"
                               "\n\nInsert option (1 / 3): "))

            if option == get_value(GeneralOptions.SIGN_IN):
                person = signin_customer_errors(get_psw_email_customer(), database)
                if person:
                    customer_menu(database, person)

            elif option == get_value(GeneralOptions.SIGN_UP):
                info_customer = get_info_person()
                if add_person_errors(database.add_person(info_customer), info_customer):
                    add_customer_errors(database.add_customer(info_customer[2]))

            elif option == get_value(GeneralOptions.EXIT):
                return

            else:
                input(f"\n{option} is not a valid option!!\n\nPress any key to continue...")

        except ValueError:
            input("\nOption must be a number!!\n\nPress any key to continue...")


def general_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input("\n1)Log as Admin"
                               "\n2)Log as Customer"
                               "\n3)Exit"
                               "\n\nInsert option (1 / 3): "))

            if option == get_value(GeneralMenuOptions.LOG_AS_ADMIN):
                initial_admin_menu(database)

            elif option == get_value(GeneralMenuOptions.LOG_AS_CUSTOMER):
                initial_customer_menu(database)

            elif option == get_value(GeneralMenuOptions.EXIT):
                return False

            else:
                input(f"\n{option} is not a correct option!!\n\nPress any key to continue...")

        except ValueError:
            input("\nOption must be a number\n\nPress any key to continue...")
