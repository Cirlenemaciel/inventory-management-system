import os
import tempfile

import app


def setup_function():
    temp_db = tempfile.NamedTemporaryFile(delete=False)
    temp_db.close()

    app.DATABASE = temp_db.name
    app.create_table()


def teardown_function():
    if os.path.exists(app.DATABASE):
        os.remove(app.DATABASE)


def test_add_product():
    app.add_product("Notebook", 10, 2500.00)

    products = app.list_products()

    assert len(products) == 1
    assert products[0][1] == "Notebook"
    assert products[0][2] == 10
    assert products[0][3] == 2500.00


def test_update_product():
    app.add_product("Mouse", 5, 100.00)
    product = app.list_products()[0]

    app.update_product(product[0], "Mouse Gamer", 8, 150.00)

    updated_product = app.list_products()[0]

    assert updated_product[1] == "Mouse Gamer"
    assert updated_product[2] == 8
    assert updated_product[3] == 150.00


def test_delete_product():
    app.add_product("Keyboard", 3, 200.00)
    product = app.list_products()[0]

    app.delete_product(product[0])

    assert app.list_products() == []