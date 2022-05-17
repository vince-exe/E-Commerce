import mysql.connector


class Database:
    def __init__(self, host, username, password, database):
        mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            databse=database
        )
