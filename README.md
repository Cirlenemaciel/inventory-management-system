# Inventory Management System

A simple inventory management system built with Python and SQLite, featuring persistent data storage and automated tests.

## Overview

This project was developed as a personal software engineering portfolio project.

The application provides CRUD operations for managing products in an inventory database, including creating, listing, updating, and deleting products.

## Technologies

- Python
- SQLite
- SQL
- Pytest
- Git
- GitHub

## Features

- Add products to inventory
- List stored products
- Update product information
- Delete products
- Persistent SQLite database
- CRUD operations
- Automated testing with Pytest
- Temporary test database isolation

## Project Structure

```text
inventory-management-system/
├── tests/
│   └── test_inventory.py
├── app.py
├── .gitignore
└── README.md
```

## Database

The application uses SQLite for persistent product storage.

The `products` table contains:

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique product identifier |
| name | TEXT | Product name |
| quantity | INTEGER | Available quantity |
| price | REAL | Product price |

## Installation

Clone the repository:

```bash
git clone https://github.com/Cirlenemaciel/inventory-management-system.git
```

Navigate to the project directory:

```bash
cd inventory-management-system
```

## Running the Application

Run:

```bash
python app.py
```

The application provides an interactive command-line interface for inventory management.

## Running the Tests

Install Pytest:

```bash
pip install pytest
```

Run the automated test suite:

```bash
python -m pytest tests -v
```

The test suite currently covers:

- Adding products
- Updating products
- Deleting products

Current test result:

```text
3 passed
```

## Future Improvements

- Product search and filtering
- Stock alerts
- Improved input validation
- REST API integration
- Web interface
- Additional automated tests
- PostgreSQL support
- Continuous integration with GitHub Actions

## Author

**Cirlene Maciel**

Junior Software Engineer | Python | JavaScript | Automation | AI
