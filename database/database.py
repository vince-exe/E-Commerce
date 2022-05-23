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
    def get_admin_info(cursor, email):
        try:
            cursor.execute(f"""SELECT first_name, email, psw 
                               FROM person JOIN administrator ON person.id = administrator.person_id
                               WHERE person.email = '{email}'
                           """)
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

        except mysql.connector.errors.DataError:
            return get_value(DatabaseErrors.DATA_ERROR)

        connection.commit()

    @staticmethod
    def get_customers(cursor, limit):
        try:
            cursor.execute(f'''SELECT customer.id, first_name, last_name, email, psw
                               FROM customer JOIN person
                               ON customer.person_id = person.id LIMIT {limit}
                          ''')
            return cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def get_products(cursor, limit):
        try:
            cursor.execute(f"SELECT * FROM product LIMIT {limit}")
            return cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def get_super_root(cursor):
        try:
            cursor.execute("""SELECT email, psw FROM person
                              JOIN administrator ON administrator.person_id = person.id
                              WHERE administrator.id = 1"""
                           )
            return cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def get_product_searched(cursor, prod_name, limit):
        try:
            cursor.execute(f"SELECT * FROM product WHERE product.product_name LIKE '%{prod_name}%' LIMIT {limit}")
            return cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)
