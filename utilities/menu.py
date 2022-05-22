from utilities.utils import *

info = ['localhost', 'root', 'mySQLroot45.&ciao#.', 'ecommerce']


def initial_customer_menu():
    while True:
        try:
            option = int(input("\n1)Sign In\n2)Sign Up\n3)exit\n\nInsert option (1 / 3): "))

            if option == get_value(GeneralOptions.SIGN_IN):
                pass

            elif option == get_value(GeneralOptions.SIGN_UP):
                pass

            elif option == get_value(GeneralOptions.EXIT):
                return

            else:
                print(f"\n{option} is not a valid option!!")

        except ValueError:
            print("\nOption must be a number!!")


def print_customers(customer_list):
    for customer in customer_list:
        print(f'''
* - - - - - - - - - - - - - *
Id: {customer[0]}\n
First Name: {customer[1]}\n
Last Name: {customer[2]}\n
Email: {customer[3]}\n
Password: {customer[4]}
* - - - - - - - - - - - - - *
            ''')


def view_customers_menu(cursor, database):
    limit = 5

    while True:
        try:
            option = int(input("\n1)Show Customers (5 at time)\n2)Exit\n\nInsert option (1 / 2): "))

            if option == 1:
                customers = database.get_customers(cursor, limit)

                if customers == get_value(DatabaseErrors.CONNECTION_LOST):
                    print("\nThe application has lost the connection with the database")
                else:
                    print_customers(customers)
                    limit += 5

            elif option == 2:
                return

            else:
                print(f'{option} is not a valid option')

        except ValueError:
            print("\nOption must be a number!!")


def print_products(products_list):
    for product in products_list:
        print(f'''
* - - - - - - - - - - - - - *
Id: {product[0]}\n
Name: {product[1]}\n
Price: {product[2]}\n
Quantity: {product[3]}
* - - - - - - - - - - - - - *
            ''')


def view_products_menu(cursor, database):
    limit = 5
    while True:
        try:
            option = int(input("\n1)View Products (5 at time)\n2)Exit\n\nInsert option (1 / 2): "))

            if option == 1:
                products = database.get_products(cursor, limit)
                if products == get_value(DatabaseErrors.CONNECTION_LOST):
                    print("\nThe application has lost the connection with the server")

                else:
                    print_products(products)
                    limit += 5

            elif option == 2:
                return

            else:
                print(f'\n{option} is not a valid option')

        except ValueError:
            print("\nOption must be a number!!")


def admin_menu(database, cursor, connection):
    while True:
        try:
            option = int(input(("\n1)View All Customers"
                                "\n2)View All Products"
                                "\n3)Add Product"
                                "\n4)Add Admin (Super Root)"
                                "\n5)Search Product (info)"
                                "\n6)Delete Product"
                                "\n7)Delete Customer"
                                "\n8)Search Customer"
                                "\n9)Delete Admin (Super Root)"
                                "\n10)Exit"
                                "\n\nInsert option (1 / 10): "
                                )))

            if option == get_value(AdminOptions.VIEW_CUSTOMERS):  # view all the customers
                view_customers_menu(cursor, database)

            elif option == get_value(AdminOptions.VIEW_PRODUCTS):  # view all the products
                view_products_menu(cursor, database)

            elif option == get_value(AdminOptions.ADD_PRODUCT):  # add a product
                prod_info = get_product_info()
                handle_product_errors(database.add_product(cursor, prod_info, connection), prod_info)

            elif option == get_value(AdminOptions.ADD_ADMIN):  # add an admin
                pass

            elif option == get_value(AdminOptions.SEARCH_PRODUCT):  # search a product
                pass

            elif option == get_value(AdminOptions.DELETE_PRODUCT):  # delete a product
                pass

            elif option == get_value(AdminOptions.DELETE_CUSTOMER):  # delete a customer
                pass

            elif option == get_value(AdminOptions.SEARCH_CUSTOMER):  # search a customer
                pass

            elif option == get_value(AdminOptions.DELETE_ADMIN):
                pass

            elif option == get_value(AdminOptions.EXIT):  # exit
                return

            else:
                print(f"{option} must be a number!!")

        except ValueError:
            print("\nOption can't be a string!!")


def initial_admin_menu(database, cursor, connection):
    while True:
        try:
            option = int(input("\n1)Sign In\n2)Exit\n\nInsert option (1 / 2): "))

            if option == get_value(GeneralOptions.SIGN_IN):
                if get_info_admin(database, cursor):
                    admin_menu(database, cursor, connection)

            elif option == get_value(AdminOptions.EXIT_LOG):
                return

            else:
                print(f"\n{option} is not a valid option!!")

        except ValueError:
            print("\nOption must be a number")


def general_menu(database, cursor, connection):
    while True:
        try:
            option = int(input("\n1)Log as Admin\n2)Log as Customer\n3)Exit\n\nInsert option (1 / 3): "))

            if option == get_value(GeneralMenuOptions.LOG_AS_ADMIN):
                initial_admin_menu(database, cursor, connection)

            elif option == get_value(GeneralMenuOptions.LOG_AS_CUSTOMER):
                initial_customer_menu()

            elif option == get_value(GeneralMenuOptions.EXIT):
                return False

            else:
                print(f"\n{option} is not a correct option!!")

        except ValueError:
            print("\nOption must be a number")