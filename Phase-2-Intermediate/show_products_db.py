import sqlite3


def show_products():

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    connection.close()

    print("\n================================")
    print("       PRODUCTS FROM DATABASE")
    print("================================")

    if not products:
        print("No products found!")

    else:
        for product in products:
            print("ID:", product[0])
            print("Product:", product[1])
            print("Price: ₹", product[2])
            print("Quantity:", product[3])
            print("----------------------------")


# TEST
show_products()