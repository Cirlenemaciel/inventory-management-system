# Inventory Management System

A simple inventory management system built with Python and SQLite.

## Overview

This project was developed as a personal software engineering portfolio project.

The system provides basic operations for managing products in an inventory database.

## Technologies

- Python
- SQLite
- SQL
- Git
- GitHub

## Features

- Create products
- List products
- Update products
- Delete products
- SQLite database
- Basic data validation
- CRUD operations

## Project Structure

```text
inventory-management-system/
├── app.py
├── .gitignore
└── README.md
```

## Database

The project uses SQLite to store product information.

The database contains the following fields:

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Product identifier |
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

Run the application:

```bash
python app.py
```

## Example

When the application starts, it initializes the SQLite database and creates the products table if it does not already exist.

## Future Improvements

Possible improvements for future versions:

- Command-line interface
- Product search
- Stock alerts
- Input validation improvements
- REST API integration
- Web interface
- Automated tests
- PostgreSQL support

## Author

**Cirlene Maciel**

Junior Software Engineer | Python | JavaScript | Automation | AI
