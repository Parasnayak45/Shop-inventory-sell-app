import sqlite3

connection = sqlite3.connect("shop.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")

connection.commit()
connection.close()

print("Database created successfully!")
print("Products table created successfully!")