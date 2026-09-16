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

    while True:
        print("\nInventory Management System")
        print("1. Add product")
        print("2. List products")
        print("3. Update product")
        print("4. Delete product")
        print("5. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            name = input("Product name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))

            add_product(name, quantity, price)
            print("Product added successfully.")

        elif option == "2":
            products = list_products()

            if not products:
                print("No products found.")
            else:
                print("\nProducts:")
                for product in products:
                    print(
                        f"ID: {product[0]} | "
                        f"Name: {product[1]} | "
                        f"Quantity: {product[2]} | "
                        f"Price: ${product[3]:.2f}"
                    )

        elif option == "3":
            product_id = int(input("Product ID: "))
            name = input("New product name: ")
            quantity = int(input("New quantity: "))
            price = float(input("New price: "))

            update_product(product_id, name, quantity, price)
            print("Product updated successfully.")

        elif option == "4":
            product_id = int(input("Product ID: "))
            delete_product(product_id)
            print("Product deleted successfully.")

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()