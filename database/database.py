from mysql.connector import errorcode
from utilities.utils import *
from utilities.enums import *

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
                return get_value(DatabaseErrors.DB_EXCEPTION)

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
    def add_person(cursor, values, connection):
        query = "INSERT INTO person (first_name, last_name, email, psw, money) VALUES (%s, %s, %s, %s, %s);"
        args = (values[0], values[1], values[2], values[3], f'{values[4]}')

        try:
            cursor.execute(query, args)

        except mysql.connector.errors.IntegrityError:
            return get_value(DatabaseErrors.EMAIL_ALREADY_EXIST)

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()

    @staticmethod
    def add_customer(cursor, connection, customer_email):
        try:
            cursor.execute(f"SELECT id FROM person WHERE email = '{customer_email}'")
            id_ = cursor.fetchone()

            cursor.execute(f"INSERT INTO customer (person_id) VALUES ({id_[0]});")

        except mysql.connector.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()

    @staticmethod
    def get_customers(cursor, limit):
        try:
            cursor.execute(f'''SELECT customer.id, first_name, last_name, email, psw, money
                               FROM customer JOIN person
                               ON customer.person_id = person.id LIMIT {limit}
                          ''')
            return cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def get_customer_info(cursor, email):
        try:
            cursor.execute(f"""SELECT email, psw, first_name, last_name, person.id, money
                               FROM ecommerce.customer JOIN person ON customer.person_id = person.id
                               WHERE email = '{email}';
                           """)

            return cursor.fetchone()

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
    def get_product_bought(cursor, prod_name):
        try:
            cursor.execute(f"SELECT * FROM product WHERE product.product_name LIKE '{prod_name}';")
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

    @staticmethod
    def delete_product(cursor, connection, id_):
        try:
            cursor.execute(f"DELETE FROM product WHERE id = {id_}")

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        except mysql.connector.errors.InterfaceError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()

    @staticmethod
    def rmv_qnt_product(cursor, connection, prod_name):
        try:
            product = Database.get_product_bought(cursor, prod_name)

            cursor.execute(f"UPDATE product SET qnt = {product[3]} WHERE id = {product[0]};")

        except mysql.connector.errors.InterfaceError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()

    @staticmethod
    def delete_customer(cursor, connection, id_):
        try:
            cursor.execute(f"DELETE FROM customer WHERE person_id = {id_}")

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        except mysql.connector.errors.InterfaceError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()

    @staticmethod
    def delete_person(cursor, connection, id_):
        cursor.execute(f"DELETE FROM person WHERE id = {id_}")
        connection.commit()

    @staticmethod
    def get_customer_searched(cursor, customer_name, limit):
        try:
            cursor.execute(f"""SELECT person.id, first_name, last_name, email, psw, money
                               FROM person JOIN customer ON person.id = customer.person_id
                               WHERE person.first_name LIKE '%{customer_name}%' LIMIT {limit}""")
            return cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def customer_add_money(cursor, connection, credit, person_id):
        try:
            cursor.execute(f"UPDATE person SET person.money = {credit} WHERE person.id = {person_id}")

        except mysql.connector.errors.OperationalError:
            return False

        connection.commit()
        return True
