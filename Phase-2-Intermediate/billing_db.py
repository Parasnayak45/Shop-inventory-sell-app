import sqlite3


def generate_bill():

    search = input("Enter product name: ").lower()
    quantity = int(input("Enter quantity: "))

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE LOWER(name) = ?",
        (search,)
    )

    product = cursor.fetchone()

    if product is None:
        print("\nProduct not found!")
        connection.close()
        return

    product_id = product[0]
    name = product[1]
    price = product[2]
    stock = product[3]

    if quantity > stock:
        print("\nNot enough stock!")
        print("Available stock:", stock)
        connection.close()
        return

    total = price * quantity
    new_stock = stock - quantity

    cursor.execute(
        "UPDATE products SET quantity = ? WHERE id = ?",
        (new_stock, product_id)
    )

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        total REAL NOT NULL
    )
    """)

    cursor.execute("""
    INSERT INTO sales (product, quantity, total)
    VALUES (?, ?, ?)
    """, (name, quantity, total))

    connection.commit()
    connection.close()

    print("\n================================")
    print("           SHOP BILL")
    print("================================")
    print("Product:", name)
    print("Price: ₹", price)
    print("Quantity:", quantity)
    print("Total: ₹", total)
    print("================================")
    print("Sale saved successfully!")
    print("Remaining stock:", new_stock)


# TEST
generate_bill()