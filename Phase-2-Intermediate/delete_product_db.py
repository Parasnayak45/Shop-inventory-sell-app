import sqlite3


def delete_product():

    search = input("Enter product name to delete: ").lower()

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM products WHERE LOWER(name) = ?",
        (search,)
    )

    if cursor.rowcount > 0:
        print("\nProduct deleted successfully!")
    else:
        print("\nProduct not found!")

    connection.commit()
    connection.close()


# TEST
#delete_product()