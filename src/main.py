from Database import database as db
from utilities.menu import *
from utilities.utils import handle_db_conn_errors


if __name__ == '__main__':
    database = db.Database(info[0], info[1], info[2], info[3])
    connection = handle_db_conn_errors(database.connect(), database)

    # create the cursor (an object that communicate with the mysql server to execute actions)
    cursor = connection.cursor()

    if not general_menu(database, cursor, connection):
        print("\nBye")

    cursor.close()
    connection.close()
