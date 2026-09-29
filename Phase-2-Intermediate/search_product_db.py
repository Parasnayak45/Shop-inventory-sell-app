import sqlite3


def search_product():

    search = input("Enter product name to search: ").lower()

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE LOWER(name) = ?",
        (search,)
    )

    product = cursor.fetchone()

    connection.close()

    if product:

        print("\n================================")
        print("        PRODUCT FOUND")
        print("================================")
        print("ID:", product[0])
        print("Product:", product[1])
        print("Price: ₹", product[2])
        print("Quantity:", product[3])

    else:
        print("\nProduct not found!")


# TEST
#search_product()