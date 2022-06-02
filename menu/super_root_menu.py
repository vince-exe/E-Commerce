from errors.handle_errors import *

from utilities.enums import *
from utilities.utils import get_info_person, print_admins, get_id_root, get_email, get_psw, get_money


def print_admin_menu(database, cursor):
    limit = 5
    while True:
        try:
            option = int(input("\n1)View Admins (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                check = database.get_admins(cursor, limit)

                if print_admin_errors(check):
                    print_admins(check)
                    limit += 5

            elif option == 2:
                return

            else:
                print(f"\n{option} can not be an option")

        except ValueError:
            print("\nOption must be a number!!")


def search_admin_menu(database, cursor, admin_name):
    limit = 5
    while True:
        try:
            option = int(input("\n1)View Admin"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                check = database.get_admin_searched(cursor, admin_name, limit)

                if search_admin_errors(check, admin_name):
                    print_admins(check)
                    limit += 5

                else:
                    return

            elif option == 2:
                return

            else:
                print(f"\n{option} is not a valid option")

        except ValueError:
            print("\nOption must be a number!!")


def modify_admin_menu(database, cursor, connection, id_):
    admin_id = database.get_person_id_super_root(cursor, id_)

    if admin_id is None:
        print(f"\nNo admin found with the id: {id_}")

        input("\nPress any key to continue...")
        return

    elif admin_id == get_value(DatabaseErrors.CONNECTION_LOST):
        conn_lost_msg()
        return

    while True:
        try:
            option = int(input("\n1)Modify First Name"
                               "\n2)Modify Last Name"
                               "\n3)Modify Email"
                               "\n4)Modify Password"
                               "\n5)Modify Money"
                               "\n6)Exit"
                               "\n\nInsert option (1 / 6): "))

            if option == get_value(ModifyAdminOptions.MODIFY_FIRST_NAME):  # Modify First Name
                first_name = input("\nInsert The First Name: ")
                update_firstname_person(database.update_person_first_name(cursor, connection, first_name, admin_id),
                                        first_name)

            elif option == get_value(ModifyAdminOptions.MODIFY_LAST_NAME):  # Modify Last Name
                last_name = input("\nInsert the Last Name: ")
                update_lastname_person(database.update_person_last_name(cursor, connection, last_name, admin_id),
                                       last_name)

            elif option == get_value(ModifyAdminOptions.MODIFY_EMAIL):  # Modify Email
                email = get_email(get_value(CredentialsOptions.EMAIL_MAX_LEN))
                update_email_person(database.update_person_email(cursor, connection, email, admin_id), email)

            elif option == get_value(ModifyAdminOptions.MODIFY_PASSWORD):  # Modify Password
                psw = get_psw(get_value(CredentialsOptions.PSW_MAX_LEN))
                update_password_person(database.update_person_password(cursor, connection, psw, admin_id))

            elif option == get_value(ModifyAdminOptions.MODIFY_MONEY):  # Modify Money
                money = get_money(get_value(MoneyOptions.MIN), get_value(MoneyOptions.MAX))
                update_money_person(database.update_person_money(cursor, connection, money, admin_id))

            elif option == get_value(ModifyAdminOptions.EXIT):  # Exit
                return

            else:
                print(f"\n{option} is not a valid option")

        except ValueError:
            print("\nOption must be a number!!")


def super_root_menu(database, cursor, connection):
    while True:
        try:
            option = int(input("\n1)Add Admin"
                               "\n2)Delete Admin"
                               "\n3)Search Admin"
                               "\n4)Modify Admin"
                               "\n5)View Admins"
                               "\n6)Exit"
                               "\n\nInsert option (1 / 6): "))

            if option == get_value(SuperRootOptions.ADD_ADMIN):  # Add Admin
                info = get_info_person()
                if add_admin_errors(database.add_person(cursor, info, connection), info):
                    database.add_root(cursor, connection)

            elif option == get_value(SuperRootOptions.DELETE_ADMIN):  # Delete Admin
                id_ = get_id_root()
                delete_admin_errors(database.delete_admin(cursor, connection, id_), id_)

            elif option == get_value(SuperRootOptions.SEARCH_ADMIN):  # Search Admin
                admin_name = input("\nInsert the name: ")
                search_admin_menu(database, cursor, admin_name)

            elif option == get_value(SuperRootOptions.MODIFY_ADMIN):  # Modify Admin
                id_ = get_id_root()
                modify_admin_menu(database, cursor, connection, id_)
                pass

            elif option == get_value(SuperRootOptions.VIEW_ADMINS):  # View Admins
                print_admin_menu(database, cursor)

            elif option == get_value(SuperRootOptions.EXIT):  # Exit
                return

            else:
                print(f'\n{option} is not an option')

        except ValueError:
            print("\nOption must be a number!!")
