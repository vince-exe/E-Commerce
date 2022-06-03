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
        self.cursor = None
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(user=self.username,
                                                      password=self.password,
                                                      host=self.host,
                                                      database=self.db_name
                                                      )

            return self.connection

        except mysql.connector.Error as err:

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return DatabaseErrors.ACCESS_DENIED

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return DatabaseErrors.DB_EXCEPTION

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_cursor(self):
        self.cursor = self.connection.cursor()

    def shut_down(self):
        self.cursor.close()
        self.connection.close()

    def get_admin_info(self, email):
        try:
            self.cursor.execute(f"""
                                    SELECT first_name, email, psw 
                                    FROM person JOIN administrator ON person.id = administrator.person_id
                                    WHERE person.email = '{email}'
                                """)
            return self.cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def add_product(self, values):
        query = "INSERT INTO product (product_name, price, qnt) VALUES (%s, %s, %s);"
        args = (values[0], f'{values[1]}', values[2])

        # try to execute the query
        try:
            self.cursor.execute(query, args)

        except mysql.connector.errors.IntegrityError:
            return DatabaseErrors.NAME_ALREADY_EXIST

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.errors.DataError:
            return DatabaseErrors.DATA_ERROR

        self.connection.commit()

    def add_person(self, values):
        query = "INSERT INTO person (first_name, last_name, email, psw, money) VALUES (%s, %s, %s, %s, %s);"
        args = (values[0], values[1], values[2], values[3], f'{values[4]}')

        try:
            self.cursor.execute(query, args)

        except mysql.connector.errors.IntegrityError:
            return DatabaseErrors.EMAIL_ALREADY_EXIST

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.errors.DataError:
            return DatabaseErrors.DATA_ERROR

        self.connection.commit()

    def add_customer(self, customer_email):
        try:
            self.cursor.execute(f"SELECT id FROM person WHERE email = '{customer_email}'")
            id_ = self.cursor.fetchone()

            self.cursor.execute(f"INSERT INTO customer (person_id) VALUES ({id_[0]});")

        except mysql.connector.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        self.connection.commit()

    def get_customers(self, limit):
        try:
            self.cursor.execute(f'''SELECT customer.id, first_name, last_name, email, psw, money
                               FROM customer JOIN person
                               ON customer.person_id = person.id LIMIT {limit}
                          ''')
            return self.cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_customer_info(self, email):
        try:
            self.cursor.execute(f"""SELECT email, psw, first_name, last_name, person.id, money
                               FROM ecommerce.customer JOIN person ON customer.person_id = person.id
                               WHERE email = '{email}';
                           """)

            return self.cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_products(self, limit):
        try:
            self.cursor.execute(f"SELECT * FROM product LIMIT {limit}")
            return self.cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_super_root(self):
        try:
            self.cursor.execute("""SELECT email, psw FROM person
                              JOIN administrator ON administrator.person_id = person.id
                              WHERE administrator.id = 1"""
                                )
            return self.cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_product_bought(self, prod_name):
        try:
            self.cursor.execute(f"SELECT * FROM product WHERE product.product_name LIKE '{prod_name}';")
            return self.cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_product_searched(self, prod_name, limit):
        try:
            self.cursor.execute(f"SELECT * FROM product WHERE product.product_name LIKE '%{prod_name}%' LIMIT {limit}")
            return self.cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def delete_product(self, id_):
        try:
            self.cursor.execute(f"DELETE FROM product WHERE id = {id_}")

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.errors.InterfaceError:
            return DatabaseErrors.CONNECTION_LOST

        self.connection.commit()

    def rmv_qnt_product(self, prod_name):
        try:
            product = self.get_product_bought(prod_name)

            if product[3] <= 0:  # if the quantity is equal to 0
                return DatabaseErrors.OUT_OF_STOCK

            self.cursor.execute(f"UPDATE product SET qnt = {product[3] - 1} WHERE id = {product[0]};")

        except mysql.connector.errors.InterfaceError:
            return DatabaseErrors.CONNECTION_LOST

        self.connection.commit()

    def delete_customer(self, id_):
        try:
            self.cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            self.connection.commit()

            self.cursor.execute(f"""SELECT customer.person_id FROM customer
                                       JOIN person ON person.id = customer.person_id WHERE customer.id = {id_};""")

            person_id = self.cursor.fetchone()

            self.cursor.execute(f"DELETE FROM customer WHERE customer.id = {id_};")
            self.cursor.execute(f"""DELETE FROM person WHERE person.id = {person_id[0]};""")
            self.connection.commit()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.errors.InterfaceError:
            return DatabaseErrors.CONNECTION_LOST

        self.connection.commit()

    def get_customer_searched(self, customer_name, limit):
        try:
            self.cursor.execute(f"""SELECT person.id, first_name, last_name, email, psw, money
                               FROM person JOIN customer ON person.id = customer.person_id
                               WHERE person.first_name LIKE '%{customer_name}%' LIMIT {limit}""")
            return self.cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def customer_change_money(self, credit, person_id):
        try:
            self.cursor.execute(f"UPDATE person SET person.money = {credit} WHERE person.id = {person_id}")

        except mysql.connector.errors.OperationalError:
            return False

        self.connection.commit()
        return True

    def create_my_order(self, customer_id):
        try:
            self.cursor.execute(f"INSERT INTO my_order (customer_id) VALUES ({customer_id});")

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        self.connection.commit()

    def create_prod_ordered(self, prod_id, customer_id):
        try:
            order_id = self.get_last_order(customer_id)
            sql = "INSERT INTO product_ordered(product_id, order_id, date_) VALUES (%s, %s, %s);"
            args = (f'{prod_id}', f'{order_id[0]}', get_date())

            self.cursor.execute(sql, args)

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        self.connection.commit()

    def get_customer_id(self, person_id):
        try:
            self.cursor.execute(f"""SELECT customer.id FROM customer
                               JOIN person ON person.id = customer.person_id
                               WHERE person.id = {person_id}
                           """)
            return self.cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_last_order(self, customer_id):
        try:
            self.cursor.execute(
                f"SELECT id FROM my_order WHERE my_order.customer_id = {customer_id} ORDER BY id DESC LIMIT 1")
            return self.cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_orders(self, customer_id, limit):
        try:
            self.cursor.execute(f"""SELECT person.first_name,
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
                               """)

            return self.cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except TypeError:
            return DatabaseErrors.CONNECTION_LOST

    def get_orders_searched(self, customer_id, prod_name, limit):
        try:
            self.cursor.execute(f'''SELECT person.first_name,
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

            return self.cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def delete_order(self, order_id):
        try:
            self.cursor.execute('''SET FOREIGN_KEY_CHECKS = 0;''')
            self.connection.commit()

            self.cursor.execute(f'''DELETE FROM my_order WHERE my_order.id = {order_id};''')
            self.connection.commit()

            self.cursor.execute(f'''DELETE FROM product_ordered WHERE product_ordered.order_id = {order_id};''')
            self.connection.commit()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def update_qnt_product(self, prod_id, new_qnt):
        try:
            self.cursor.execute(f'''UPDATE product SET product.qnt = "{new_qnt}" WHERE product.id = {prod_id}''')

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.errors.DataError:
            return DatabaseErrors.DATA_ERROR

        self.connection.commit()

    def update_name_product(self, prod_id, new_name):
        try:
            self.cursor.execute(f'''
                                    UPDATE product SET product.product_name = "{new_name}"
                                    WHERE product.id = {prod_id}
                                ''')

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.errors.DataError:
            return DatabaseErrors.DATA_ERROR

        except mysql.connector.errors.IntegrityError:
            return DatabaseErrors.NAME_ALREADY_EXIST

        self.connection.commit()

    def update_price_product(self, prod_id, new_price):
        try:
            self.cursor.execute(f'''UPDATE product SET product.price = "{new_price}" WHERE product.id = {prod_id}''')

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        self.connection.commit()

    def get_last_person(self):
        try:
            self.cursor.execute("SELECT person.id FROM person ORDER BY person.id DESC LIMIT 1")
            return self.cursor.fetchone()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def add_root(self):
        try:
            last_person_id = self.get_last_person()

            self.cursor.execute(f"""INSERT INTO administrator(person_id) VALUES ('{last_person_id[0]}');""")

        except mysql.connector.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.IntegrityError:
            return DatabaseErrors.EMAIL_ALREADY_EXIST

        self.connection.commit()

    def get_admins(self, limit):
        try:
            self.cursor.execute(f"""SELECT administrator.id,
                                      person.first_name,
                                      person.last_name,
                                      person.email,
                                      person.psw,
                                      person.money
                                FROM ecommerce.administrator JOIN person ON person.id = administrator.person_id
                                LIMIT {limit}
                           """)
            return self.cursor.fetchall()

        except mysql.connector.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_person_id_super_root(self, id_):
        try:
            self.cursor.execute(f"""SELECT administrator.person_id

                               FROM ecommerce.administrator JOIN person ON person.id = administrator.person_id
                               WHERE administrator.id = {id_}
                           """)

            return self.cursor.fetchone()

        except mysql.connector.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def delete_admin(self, admin_id):
        try:
            id_ = self.get_person_id_super_root(admin_id)

            if id_ is None:
                return DatabaseErrors.NO_ADMIN_FOUND

            self.cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            self.connection.commit()

            self.cursor.execute(f"DELETE FROM person WHERE person.id = {id_[0]};")
            self.connection.commit()

            self.cursor.execute(f"DELETE FROM administrator WHERE administrator.person_id = {id_[0]};")
            self.connection.commit()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def get_admin_searched(self, admin_name, limit):
        try:
            self.cursor.execute(f"""SELECT administrator.id,
                                      person.first_name,
                                      person.last_name,
                                      person.email,
                                      person.psw,
                                      person.money
                                      
                               FROM administrator
                               
                               JOIN person ON person.id = administrator.person_id
                               
                               WHERE person.first_name LIKE '%{admin_name}%' LIMIT {limit}
                           """)

            return self.cursor.fetchall()

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

    def update_person_first_name(self, new_name, person_id):
        try:
            self.cursor.execute(f"UPDATE person SET person.first_name = '{new_name}' WHERE person.id = {person_id[0]};")

        except mysql.connector.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.errors.DataError:
            return DatabaseErrors.DATA_ERROR

        self.connection.commit()

    def update_person_last_name(self, new_name, person_id):
        try:
            self.cursor.execute(f"UPDATE person SET person.last_name = '{new_name}' WHERE person.id = {person_id[0]};")

        except mysql.connector.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.errors.DataError:
            return DatabaseErrors.DATA_ERROR

        self.connection.commit()

    def update_person_email(self, new_email, person_id):
        try:
            self.cursor.execute(f"UPDATE person SET person.email = '{new_email}' WHERE person.id = {person_id[0]};")

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST

        except mysql.connector.errors.IntegrityError:
            return DatabaseErrors.EMAIL_ALREADY_EXIST

        self.connection.commit()

    def update_person_password(self, new_psw, person_id):
        try:
            self.cursor.execute(f"UPDATE person SET person.psw = '{new_psw}' WHERE person.id = {person_id[0]};")

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors.CONNECTION_LOST
        self.connection.commit()

    def update_person_money(self, new_money, person_id):
        try:
            self.cursor.execute(f"UPDATE person SET person.money = '{new_money}' WHERE person.id = {person_id[0]}")

        except mysql.connector.errors.OperationalError:
            return DatabaseErrors

        self.connection.commit()
