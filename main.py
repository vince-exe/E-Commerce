from database import database as db

from menu.general_menu import general_menu

from errors.handle_errors import db_conn_errors


info = ['localhost', 'root', 'MySQL85.#(6@', 'ecommerce']


if __name__ == '__main__':
    database = db.Database(info[0], info[1], info[2], info[3])
    # connect to the database and check if the connection went fine.
    db_conn_errors(database.connect(), database)

    # initialize the cursor property of the database class, with it we can perform actions to the database
    database.get_cursor()

    # start the menu function
    try:
        input("\nPress any key to continue...")
        if not general_menu(database):
            print("\nBye")

    except KeyboardInterrupt:
        database.shut_down()

    # close the connections with the database
    database.shut_down()
