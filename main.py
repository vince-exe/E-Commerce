from database import database as db

from menu.general_menu import general_menu

from errors.handle_errors import db_conn_errors

from utilities.utils import print_logo, Colors

info = ['localhost', 'root', 'mySQLroot45.&ciao#.', 'ecommerce']


if __name__ == '__main__':
    print_logo()
    database = db.Database(info[0], info[1], info[2], info[3])

    try:
        # connect to the database and check if the connection went fine.
        db_conn_errors(database.connect(), database)

    except KeyboardInterrupt:
        print(f"\n\n{Colors.RESET}")
        exit(-1)

    # initialize the cursor property of the database class, with it we can perform actions to the database
    database.get_cursor()

    # start the menu function
    try:
        if not general_menu(database):
            print("\nBye")

    except KeyboardInterrupt:
        print(f"\n\n{Colors.RESET}")
        database.shut_down()

    # close the connections with the database
    database.shut_down()
