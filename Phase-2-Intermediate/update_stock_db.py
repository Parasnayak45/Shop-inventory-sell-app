import sqlite3


def update_stock():

    search = input("Enter product name: ").lower()
    new_quantity = int(input("Enter new quantity: "))

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE products SET quantity = ? WHERE LOWER(name) = ?",
        (new_quantity, search)
    )

    if cursor.rowcount > 0:
        print("\nStock updated successfully!")
    else:
        print("\nProduct not found!")

    connection.commit()
    connection.close()


# TEST
update_stock()