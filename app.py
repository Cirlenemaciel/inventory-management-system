import sqlite3


DATABASE = "inventory.db"


def connect_database():
    return sqlite3.connect(DATABASE)


def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_product(name, quantity, price):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
        (name, quantity, price)
    )

    connection.commit()
    connection.close()


def list_products():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    connection.close()

    return products


def update_product(product_id, name, quantity, price):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE products
        SET name = ?, quantity = ?, price = ?
        WHERE id = ?
    """, (name, quantity, price, product_id))

    connection.commit()
    connection.close()


def delete_product(product_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    connection.commit()
    connection.close()


def main():
    create_table()

    print("Inventory Management System")
    print("Database initialized successfully.")


if __name__ == "__main__":
    main()
