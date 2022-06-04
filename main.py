from database import database as db

from menu.general_menu import general_menu

from errors.handle_errors import db_conn_errors, read_settings_errors

from utilities.utils import print_logo, Colors


if __name__ == '__main__':
    print_logo()

    settings = read_settings_errors('config.json')
    database = None

    try:
        database = db.Database(settings['Host'], settings['Username'], settings['Password'], settings['DbName'])

    except KeyError:
        print(f"\n\t\t\t\t\t    {Colors.RED}{Colors.BOLD}ERROR: {Colors.RESET}Check the json file!!")
        exit(-1)

    try:
        # connect to the database and check if the connection went fine.
        db_conn_errors(database.connect(), database)

    except KeyboardInterrupt:
        print(f"\n\n{Colors.RESET}")
        exit(-1)

    # initialize the cursor property of the database class, with it we can perform actions to the database
    database.get_cursor()

    # start the menu function
    general_menu(database)

    # close the connections with the database
    database.shut_down()
