import sqlite3


def inventory_value():

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute("SELECT price, quantity FROM products")

    products = cursor.fetchall()

    connection.close()

    total_value = 0

    for product in products:

        price = product[0]
        quantity = product[1]

        total_value += price * quantity

    print("\n================================")
    print("       INVENTORY VALUE")
    print("================================")
    print("Total Inventory Value: ₹", total_value)


# TEST
inventory_value()