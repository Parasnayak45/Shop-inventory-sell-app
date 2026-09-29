import sqlite3


def add_product():

    name = input("Enter product name: ")
    price = float(input("Enter product price: ₹"))
    quantity = int(input("Enter product quantity: "))

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
    """, (name, price, quantity))

    connection.commit()
    connection.close()

    print("\nProduct added successfully!")


# TEST
add_product()