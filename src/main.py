from Database import database as db
from utilities import *


if __name__ == '__main__':
    database = db.Database(info[0], info[1], info[2], info[3])
    connection = database.connect()

    # check if the connection went fine
    if connection:
        print(f"\nSuccessfully connected to the database: [{database.db_name}]")
    else:
        print(f"\nCan't connect to the database: [{database.db_name}]")
        exit(db.DATABASE_ERROR)

    # create the cursor (an object that communicate with the mysql server to execute actions)
    cursor = connection.cursor()

    if not general_menu(database, cursor):
        print("\nBye")

    cursor.close()
    connection.close()
