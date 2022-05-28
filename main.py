from database import database as db
from menu.general_menu import general_menu
from utilities.utils import handle_db_conn_errors

info = ['localhost', 'root', 'mySQLroot45.&ciao#.', 'ecommerce']


if __name__ == '__main__':
    database = db.Database(info[0], info[1], info[2], info[3])
    connection = handle_db_conn_errors(database.connect(), database)

    # create the cursor (an object that communicate with the mysql server to execute actions)
    cursor = connection.cursor()

    # start the menu function
    if not general_menu(database, cursor, connection):
        print("\nBye")

    # close the connections
    cursor.close()
    connection.close()