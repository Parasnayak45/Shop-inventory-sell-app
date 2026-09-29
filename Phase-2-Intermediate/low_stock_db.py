import sqlite3


def low_stock():

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name, quantity FROM products WHERE quantity <= 5"
    )

    products = cursor.fetchall()

    connection.close()

    print("\n================================")
    print("        LOW STOCK ALERT")
    print("================================")

    if products:

        for product in products:
            print("Product:", product[0])
            print("Quantity:", product[1])
            print("----------------------------")

    else:
        print("No low stock products!")


# TEST
low_stock()