from mysql.connector import errorcode

import mysql.connector

DATABASE_ERROR = -1


class Database:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.db_name = database

    def connect(self):
        try:
            return mysql.connector.connect(user=self.username,
                                           password=self.password,
                                           host=self.host,
                                           database=self.db_name
                                           )

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("\nSomething went wrong with username or password")
                return False

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print(f"\nThe database [{self.db_name}] doesn't exist")
                return False

            else:
                return False

    @staticmethod
    def show_all_(cursor, table_name):
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()
