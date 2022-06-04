from utilities.utils import *

from errors.handle_errors import *

import os


def view_customers_menu(database):
    limit = 5

    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}Show Customers (5 at time)"
                               f"{Colors.BLU}{Colors.BOLD}\n2){Colors.RESET} Exit"
                               f"\n\nInsert option (1 / 2): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                customers = database.get_customers(limit)

                if customers == DatabaseErrors.CONNECTION_LOST:
                    conn_lost_msg()

                elif not len(customers):
                    input(f"{Colors.YELLOW}{Colors.BOLD}\nThere are no customers registered\n\n"
                          f"{Colors.RESET}Press any key to continue...")

                else:
                    print_customers(customers)
                    input("\nPress any key to continue...")
                    limit += 5

            elif option == 2:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)


def view_products_menu(database):
    limit = 5
    while True:
        try:
            os.system('cls||clear')

            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}View Products (5 at time)"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 / 2): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                products = database.get_products(limit)
                if products == DatabaseErrors.CONNECTION_LOST:
                    conn_lost_msg()

                else:
                    print_products(products)
                    input("\nPress any key to continue...")
                    limit += 5

            elif option == 2:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)


def view_product_searched(database, prod_name):
    limit = 5

    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}View Products (5 at time)"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 / 2): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                if not prod_searched_errors(database.get_product_searched(prod_name, limit), prod_name):
                    return

                else:
                    print_products(database.get_product_searched(prod_name, limit))
                    input("\n\nPress any key to continue...")
                    limit += 5

            elif option == 2:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)


def delete_product_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}Delete Product"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 /2): {Colors.BLU}{Colors.BOLD}"
                               )
                         )

            print(f"{Colors.RESET}")

            if option == 1:
                while True:
                    try:
                        os.system('cls||clear')
                        id_ = int(input(f"{Colors.BLU}{Colors.BOLD}\nProduct Id: {Colors.RESET}"))
                        break
                    except ValueError:
                        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Id must be a number!!"
                              f"\n\nPress any key to continue...")

                del_prod = database.delete_product(id_)
                if rmv_errors(del_prod):
                    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully removed the product with id: {Colors.RESET}"
                          f"[{id_}]\n\nPress any key to continue...")

            elif option == 2:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shutdown()
            exit(0)


def delete_customer_menu(database):
    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}Delete Customer"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 / 2): {Colors.BLU}{Colors.BOLD}"
                               )
                         )

            if option == 1:
                while True:
                    try:
                        id_ = int(input(f"{Colors.BLU}{Colors.BOLD}\nCustomer Id: {Colors.RESET}"))
                        break

                    except ValueError:
                        input(f"{Colors.RED}{Colors.BOLD}\nERROR: {Colors.RESET}Id must be a number!!"
                              f"\n\nPress any key to continue...")

                if rmv_errors(database.delete_customer(id_)):
                    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully removed the customer with id: {Colors.RESET}"
                          f"[{id_}]"
                          f"\n\nPress any key to continue...")

            elif option == 2:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)


def search_customer_menu(database, customer_name):
    limit = 5

    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}View Customer"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 / 2): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                if customer_searched_errors(database.get_customer_searched(customer_name, limit),
                                            customer_name):

                    print_customers(database.get_customer_searched(customer_name, limit))
                    input("\n\nPress any key to continue...")
                    limit += 5

                else:
                    return

            elif option == 2:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shutdown()
            exit(0)


def modify_product(database):
    prod_id = get_id_product()

    while True:
        try:
            os.system('cls||clear')
            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}Change Name"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Change Quantity"
                               f"{Colors.BLU}{Colors.BOLD}\n3) {Colors.RESET}Change Price"
                               f"{Colors.BLU}{Colors.BOLD}\n4) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 / 4): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                os.system('cls||clear')
                prod_name = input(f"{Colors.BLU}{Colors.BOLD}\nNew Name: {Colors.RESET}")
                update_name_product_errors(database.update_name_product(prod_id, prod_name), prod_name)

            elif option == 2:
                update_qnt_errors(database.update_qnt_product(prod_id, get_prod_qnt()))

            elif option == 3:
                update_price_errors(database.update_price_product(prod_id, get_prod_price(PriceOptions.MAX)))

            elif option == 4:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shutdown()
            exit(0)


def admin_menu(database):
    while True:
        os.system('cls||clear')
        try:
            option = int(input((f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}View All Customers"
                                f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}View All Products"
                                f"{Colors.BLU}{Colors.BOLD}\n3) {Colors.RESET}Add Product"
                                f"{Colors.BLU}{Colors.BOLD}\n4) {Colors.RESET}Modify Product"
                                f"{Colors.BLU}{Colors.BOLD}\n5) {Colors.RESET}Search Product (info)"
                                f"{Colors.BLU}{Colors.BOLD}\n6) {Colors.RESET}Delete Product"
                                f"{Colors.BLU}{Colors.BOLD}\n7) {Colors.RESET}Delete Customer"
                                f"{Colors.BLU}{Colors.BOLD}\n8) {Colors.RESET}Search Customer"
                                f"{Colors.BLU}{Colors.BOLD}\n9) {Colors.RESET}Exit"
                                f"\n\n{Colors.RESET}Insert option (1 / 9): {Colors.BLU}{Colors.BOLD}"
                                )))

            print(f"{Colors.RESET}")

            if option == AdminOptions.VIEW_CUSTOMERS:  # View Customers
                view_customers_menu(database)

            elif option == AdminOptions.VIEW_PRODUCTS:  # View Products
                view_products_menu(database)

            elif option == AdminOptions.ADD_PRODUCT:  # Add Product
                prod_info = get_product_info()
                add_prod_errors(database.add_product(prod_info), prod_info)

            elif option == AdminOptions.MODIFY_PRODUCT:  # Modify Product
                input(f"{Colors.GREEN}{Colors.BOLD}\n\nNote: {Colors.RESET}"
                      f"The application doesn't check if you are using the correct id..")
                modify_product(database)

            elif option == AdminOptions.SEARCH_PRODUCT:  # Search Product
                prod_name = input(f"{Colors.BLU}{Colors.BOLD}\nProduct Name: {Colors.RESET}")
                view_product_searched(database, prod_name)

            elif option == AdminOptions.DELETE_PRODUCT:  # Delete Product
                input(f"{Colors.GREEN}{Colors.BOLD}\n\nNote: {Colors.RESET}"
                      f"The application doesn't check if you are using the correct id..")
                delete_product_menu(database)

            elif option == AdminOptions.DELETE_CUSTOMER:  # Delete Customer
                input(f"{Colors.GREEN}{Colors.BOLD}\n\nNote: {Colors.RESET}"
                      f"The application doesn't check if you are using the correct id..")
                delete_customer_menu(database)

            elif option == AdminOptions.SEARCH_CUSTOMER:  # Search Customer
                customer_name = input(f"{Colors.BLU}{Colors.BOLD}\nCustomer Name: {Colors.RESET}")
                search_customer_menu(database, customer_name)

            elif option == AdminOptions.EXIT:  # Exit
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)
