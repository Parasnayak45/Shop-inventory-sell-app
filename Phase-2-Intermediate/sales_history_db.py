import sqlite3


def sales_history():

    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM sales")

    sales = cursor.fetchall()

    connection.close()

    print("\n================================")
    print("          SALES HISTORY")
    print("================================")

    if sales:

        for sale in sales:
            print("Sale ID:", sale[0])
            print("Product:", sale[1])
            print("Quantity:", sale[2])
            print("Total: ₹", sale[3])
            print("----------------------------")

    else:
        print("No sales found!")


# TEST
#sales_history()