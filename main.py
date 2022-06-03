from database import database as db

from menu.general_menu import general_menu

from errors.handle_errors import db_conn_errors, shut_down


info = ['localhost', 'root', 'mySQLroot45.&ciao#.', 'ecommerce']


if __name__ == '__main__':
    database = db.Database(info[0], info[1], info[2], info[3])
    connection = db_conn_errors(database.connect(), database)

    # create the cursor (an object that communicate with the mysql server to execute actions)
    cursor = connection.cursor()

    # start the menu function
    try:
        input("\nPress any key to continue...")
        if not general_menu(database, cursor, connection):
            print("\nBye")

    except KeyboardInterrupt:
        shut_down(cursor, connection)

    # close the connections
    cursor.close()
    connection.close()
