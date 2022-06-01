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

        except mysql.connector.errors.DataError:
            return get_value(DatabaseErrors.DATA_ERROR)

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

            if product[3] <= 0:  # if the quantity is equal to 0
                return get_value(DatabaseErrors.OUT_OF_STOCK)

            cursor.execute(f"UPDATE product SET qnt = {product[3] - 1} WHERE id = {product[0]};")

        except mysql.connector.errors.InterfaceError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()

    @staticmethod
    def delete_customer(cursor, connection, id_):
        try:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            connection.commit()

            cursor.execute(f"""SELECT customer.person_id FROM customer
                                       JOIN person ON person.id = customer.person_id WHERE customer.id = {id_};""")

            person_id = cursor.fetchone()

            cursor.execute(f"DELETE FROM customer WHERE customer.id = {id_};")
            cursor.execute(f"""DELETE FROM person WHERE person.id = {person_id[0]};""")
            connection.commit()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        except mysql.connector.errors.InterfaceError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

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
    def customer_change_money(cursor, connection, credit, person_id):
        try:
            cursor.execute(f"UPDATE person SET person.money = {credit} WHERE person.id = {person_id}")

        except mysql.connector.errors.OperationalError:
            return False

        connection.commit()
        return True

    @staticmethod
    def create_my_order(cursor, connection, customer_id):
        try:
            cursor.execute(f"INSERT INTO my_order (customer_id) VALUES ({customer_id});")

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()

    @staticmethod
    def create_prod_ordered(cursor, connection, prod_id, customer_id):
        try:
            order_id = Database.get_last_order(cursor, customer_id)
            sql = "INSERT INTO product_ordered(product_id, order_id, date_) VALUES (%s, %s, %s);"
            args = (f'{prod_id}', f'{order_id[0]}', get_date())

            cursor.execute(sql, args)

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()

    @staticmethod
    def get_customer_id(cursor, person_id):
        try:
            cursor.execute(f"""SELECT customer.id FROM customer
                               JOIN person ON person.id = customer.person_id
                               WHERE person.id = {person_id}
                           """)
            return cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def get_last_order(cursor, customer_id):
        try:
            cursor.execute(
                f"SELECT id FROM my_order WHERE my_order.customer_id = {customer_id} ORDER BY id DESC LIMIT 1")
            return cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def get_orders(cursor, customer_id, limit):
        try:
            cursor.execute(f'''SELECT person.first_name,
	                                  person.last_name,
	                                  product.product_name,
                                      product_ordered.date_,
	                                  my_order.id, product.id
                                      
                               FROM my_order
	                                JOIN customer ON my_order.customer_id = customer.id
                                    JOIN person ON person.id = customer.person_id
	                                JOIN product_ordered ON product_ordered.order_id = my_order.id
                                    JOIN product ON product.id = product_ordered.product_id
                                    
                                WHERE customer_id = {customer_id}
                                LIMIT {limit}
                           ''')
            return cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        except TypeError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def get_orders_searched(cursor, customer_id, prod_name, limit):
        try:
            cursor.execute(f'''SELECT person.first_name,
	                                  person.last_name,
	                                  product.product_name,
                                      product_ordered.date_,
	                                  my_order.id,
	                                  product.id
                                      
                               FROM my_order
	                               JOIN customer ON my_order.customer_id = customer.id
                                   JOIN person ON person.id = customer.person_id
	                               JOIN product_ordered ON product_ordered.order_id = my_order.id
                                   JOIN product ON product.id = product_ordered.product_id
                                   
                               WHERE customer_id = {customer_id} AND product.product_name LIKE "%{prod_name}%"
                               LIMIT {limit};''')

            return cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def delete_order(cursor, connection, order_id):
        try:
            cursor.execute('''SET FOREIGN_KEY_CHECKS = 0;''')
            connection.commit()

            cursor.execute(f'''DELETE FROM my_order WHERE my_order.id = {order_id};''')
            connection.commit()

            cursor.execute(f'''DELETE FROM product_ordered WHERE product_ordered.order_id = {order_id};''')
            connection.commit()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def update_qnt_product(cursor, connection, prod_id, new_qnt):
        try:
            cursor.execute(f'''UPDATE product SET product.qnt = "{new_qnt}" WHERE product.id = {prod_id}''')

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        except mysql.connector.errors.DataError:
            return get_value(DatabaseErrors.DATA_ERROR)

        connection.commit()

    @staticmethod
    def update_name_product(cursor, connection, prod_id, new_name):
        try:
            cursor.execute(f'''UPDATE product SET product.product_name = "{new_name}" WHERE product.id = {prod_id}''')

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        except mysql.connector.errors.DataError:
            return get_value(DatabaseErrors.DATA_ERROR)

        except mysql.connector.errors.IntegrityError:
            return get_value(DatabaseErrors.NAME_ALREADY_EXIST)

        connection.commit()

    @staticmethod
    def update_price_product(cursor, connection, prod_id, new_price):
        try:
            cursor.execute(f'''UPDATE product SET product.price = "{new_price}" WHERE product.id = {prod_id}''')

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        connection.commit()

    @staticmethod
    def get_last_person(cursor):
        try:
            cursor.execute("SELECT person.id FROM person ORDER BY person.id DESC LIMIT 1")
            return cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def add_root(cursor, connection):
        try:
            last_person_id = Database.get_last_person(cursor)

            cursor.execute(f"""INSERT INTO administrator(person_id) VALUES ('{last_person_id[0]}');""")

        except mysql.connector.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

        except mysql.connector.IntegrityError:
            return get_value(DatabaseErrors.EMAIL_ALREADY_EXIST)

        connection.commit()

    @staticmethod
    def get_admins(cursor, limit):
        try:
            cursor.execute(f"""SELECT administrator.id,
                                      person.first_name,
                                      person.last_name,
                                      person.email,
                                      person.psw,
                                      person.money
                                FROM ecommerce.administrator JOIN person ON person.id = administrator.person_id
                                LIMIT {limit}
                           """)
            return cursor.fetchall()

        except mysql.connector.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def get_person_id_super_root(cursor, id_):
        try:
            cursor.execute(f"""SELECT administrator.person_id

                               FROM ecommerce.administrator JOIN person ON person.id = administrator.person_id
                               WHERE administrator.id = {id_}
                           """)

            return cursor.fetchone()

        except mysql.connector.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def delete_admin(cursor, connection, admin_id):
        try:
            id_ = Database.get_person_id_super_root(cursor, admin_id)

            if id_ is None:
                return get_value(DatabaseErrors.NO_ADMIN_FOUND)

            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            connection.commit()

            cursor.execute(f"DELETE FROM person WHERE person.id = {id_[0]};")
            connection.commit()

            cursor.execute(f"DELETE FROM administrator WHERE administrator.person_id = {id_[0]};")
            connection.commit()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)

    @staticmethod
    def get_admin_searched(cursor, admin_name, limit):
        try:
            cursor.execute(f"""SELECT administrator.id,
                                      person.first_name,
                                      person.last_name,
                                      person.email,
                                      person.psw,
                                      person.money
                                      
                               FROM administrator
                               
                               JOIN person ON person.id = administrator.person_id
                               
                               WHERE person.first_name LIKE '%{admin_name}%' LIMIT {limit}
                           """)

            return cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return get_value(DatabaseErrors.CONNECTION_LOST)
