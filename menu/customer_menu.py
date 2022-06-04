from utilities.utils import *

from errors.handle_errors import *

from menu.admin_menu import view_products_menu
from menu.admin_menu import view_product_searched


def buy_product(database, prod_name, person):
    product = database.get_product_bought(prod_name)

    if not prod_bought_errors(product, person.get_money()):
        return

    check = database.rmv_qnt_product(prod_name)

    if check == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    elif check == DatabaseErrors.OUT_OF_STOCK:
        input(f"{Colors.YELLOW}{Colors.BOLD}\nWARNING: {Colors.RESET}the product is out of stock"
              f"\n\nPress any key to continue...")
        return

    person.remove_money(product[2])
    database.customer_change_money(person.get_money(), person.get_id())

    customer_id = database.get_customer_id(person.get_id())
    database.create_my_order(customer_id[0])
    database.create_prod_ordered(product[0], customer_id[0])

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully ordered the product: {Colors.RESET}[{product[1]}]{Colors.RESET}"
          f"\n\nPress any key to continue...")


def add_money(database, person, credit):
    person.add_money(credit)

    if database.customer_change_money(person.get_money(), person.get_id()):
        input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully added {Colors.RESET}[{credit}] {Colors.GREEN}{Colors.BOLD}"
              f"to the account{Colors.RESET}\n\nPress any key to continue...")
        return

    person.remove_money(credit)
    conn_lost_msg()
    return


def view_orders(database, person):
    limit = 5

    customer_id = database.get_customer_id(person.get_id())
    if customer_id == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    while True:
        try:
            os.system('cls||clear')

            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}View Orders (5 at time)"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Exit"
                               f"\n\nInsert option (1 / 2): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                try:
                    order = database.get_orders(customer_id[0], limit)

                    if view_orders_errors(order):
                        print_orders(order)
                        input("\n\nPress any key to continue...")
                        limit += 5
                    else:
                        return

                except TypeError:
                    conn_lost_msg()
                    return

            elif option == 2:
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")


def search_order_menu(database, prod_name, person):
    customer_id = database.get_customer_id(person.get_id())

    if customer_id == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    limit = 5
    while True:
        try:
            os.system('cls||clear')

            option = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}View Orders"
                               f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Exit"
                               f"\n\nInsert an option (1 / 2): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option == 1:
                orders = database.get_orders_searched(customer_id[0], prod_name, limit)

                if search_orders_errors(orders, prod_name):
                    print_orders(orders)
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


def delete_customer_order(database):
    id_ = get_order_id()

    if database.delete_order(id_) == DatabaseErrors.CONNECTION_LOST:
        conn_lost_msg()
        return

    input(f"{Colors.GREEN}{Colors.BOLD}\nSuccessfully removed the order with id: {Colors.RESET}[{id_}]"
          f"\n\nPress any key to continue...")


def customer_menu(database, person):
    while True:
        try:
            os.system('cls||clear')
            option_ = int(input(f"{Colors.BLU}{Colors.BOLD}\n1) {Colors.RESET}View All Products"
                                f"{Colors.BLU}{Colors.BOLD}\n2) {Colors.RESET}Search Product"
                                f"{Colors.BLU}{Colors.BOLD}\n3) {Colors.RESET}Buy Product"
                                f"{Colors.BLU}{Colors.BOLD}\n4) {Colors.RESET}Check Credit"
                                f"{Colors.BLU}{Colors.BOLD}\n5) {Colors.RESET}Add Credit"
                                f"{Colors.BLU}{Colors.BOLD}\n6) {Colors.RESET}View Orders"
                                f"{Colors.BLU}{Colors.BOLD}\n7) {Colors.RESET}Delete Orders"
                                f"{Colors.BLU}{Colors.BOLD}\n8) {Colors.RESET}Search Order"
                                f"{Colors.BLU}{Colors.BOLD}\n9) {Colors.RESET}Exit"
                                f"\n\nInsert option (1 / 9): {Colors.BLU}{Colors.BOLD}"))

            print(f"{Colors.RESET}")

            if option_ == CustomerOptions.VIEW_PRODUCTS:  # View Orders
                view_products_menu(database)

            elif option_ == CustomerOptions.SEARCH_PRODUCT:  # Search Product
                prod_name = input(f"{Colors.BLU}{Colors.BOLD}\nProduct Name: {Colors.RESET}")
                view_product_searched(database, prod_name)

            elif option_ == CustomerOptions.BUY_PRODUCT:  # Buy Product
                prod_name = input(f"{Colors.BLU}{Colors.BOLD}\nProduct Name: {Colors.RESET}")
                buy_product(database, prod_name, person)

            elif option_ == CustomerOptions.CHECK_CREDIT:  # Check Credit
                input(f"{Colors.GREEN}{Colors.BOLD}\nYour credit: {Colors.RESET}[{round(person.get_money(), 2)}]"
                      f"\n\nPress any key to continue...")

            elif option_ == CustomerOptions.ADD_CREDIT:  # Add Credit
                credit = get_money(MoneyOptions.MIN, MoneyOptions.MAX)
                add_money(database, person, credit)

            elif option_ == CustomerOptions.VIEW_ORDERS:  # View Orders
                view_orders(database, person)

            elif option_ == CustomerOptions.DELETE_ORDERS:  # Delete Orders
                input(f"{Colors.GREEN}{Colors.BOLD}\nNote: the application doesn't check if you are using a correct id..")
                delete_customer_order(database)

            elif option_ == CustomerOptions.SEARCH_ORDERS:  # Search Orders
                product_name = input(f"{Colors.BLU}{Colors.BOLD}\nProduct Name: {Colors.RESET}")
                search_order_menu(database, product_name, person)

            elif option_ == CustomerOptions.EXIT:  # Exit
                return

            else:
                input(f"\n{Colors.BLU}{Colors.BOLD}{option_} {Colors.RED}{Colors.BOLD}is not a correct option!!"
                      f"\n\n{Colors.RESET}Press any key to continue...")

        except ValueError:
            input(f"\n{Colors.RED}{Colors.BOLD}Option must be a number\n\n{Colors.RESET}Press any key to continue...")

        except KeyboardInterrupt:
            database.shut_down()
            exit(0)
