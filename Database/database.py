from mysql.connector import errorcode
from utilities.utils import *

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
                return get_value(DatabaseErrors.ACCESS_DENIED)

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return get_value(DatabaseErrors.DB_ERROR)

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def show_all_(cursor, table_name):
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()

    @staticmethod
    def get_admin_info(cursor, table_name, condition):
        try:
            cursor.execute(f"SELECT first_name, last_name, email, psw FROM {table_name} WHERE {condition}")
            return cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def add_product(cursor, values, connection):
        query = "INSERT INTO product (product_name, price, qnt) VALUES (%s, %s, %s);"
        args = (values[0], f'{values[1]}', values[2])

        # try to execute the query
        try:
            cursor.execute(query, args)

        except mysql.connector.errors.IntegrityError:
            return get_value(DatabaseErrors.NAME_ALREADY_EXIST)

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()
