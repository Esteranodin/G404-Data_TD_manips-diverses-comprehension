"""Recreate SQLite tables and import the typed CSV values in one transaction."""

import sqlite3

import pandas as pd

from data_io import DATABASE_PATH, read_tables


def main():
    # Validate the input before opening or changing the database.
    customers, orders = read_tables()

    # Convert pandas values to Python values for SQLite.
    # None becomes SQL NULL; known numbers become int or float.
    customer_rows = [
        (
            row.id,
            row.name,
            None if pd.isna(row.age) else int(row.age),
            row.city,
        )
        for row in customers.itertuples(index=False)
    ]

    order_rows = [
        (
            row.id,
            row.customer_id,
            row.product,
            int(row.quantity),
            None if pd.isna(row.discount_pct) else float(row.discount_pct),
        )
        for row in orders.itertuples(index=False)
    ]

    # Track a new database file so a failed first import can remove it.
    database_existed = DATABASE_PATH.exists()
    import_succeeded = False

    # Open the SQLite file, creating it if it does not exist.
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        # Enforce the link: each order must refer to an existing customer.
        # Enable this SQLite setting before starting the transaction.
        connection.execute("PRAGMA foreign_keys = ON")

        # Group table recreation and imports into one transaction.
        # Save all changes with commit(), or undo them with rollback().
        connection.execute("BEGIN")

        # Reset both tables on every run.
        # Drop orders before customers because orders refers to customers.
        connection.execute("DROP TABLE IF EXISTS orders")
        connection.execute("DROP TABLE IF EXISTS customers")

        # Create customers first: orders will refer to its unique identifiers.
        connection.execute(
            """
            CREATE TABLE customers (
                id TEXT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                age INTEGER CHECK (age BETWEEN 0 AND 120),
                city TEXT NOT NULL
            )
            """
        )

        # Define the customer link, positive quantities and valid discounts.
        # A discount can be NULL; a known discount must be between 0 and 100.
        connection.execute(
            """
            CREATE TABLE orders (
                id TEXT PRIMARY KEY NOT NULL,
                customer_id TEXT NOT NULL REFERENCES customers(id),
                product TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK (quantity > 0),
                discount_pct REAL CHECK (discount_pct BETWEEN 0 AND 100)
            )
            """
        )

        # Insert customers before the orders that refer to them.
        # Each ? receives the corresponding value from a row.
        # executemany() repeats the INSERT for each row.
        connection.executemany(
            """
            INSERT INTO customers (id, name, age, city)
            VALUES (?, ?, ?, ?)
            """,
            customer_rows,
        )

        connection.executemany(
            """
            INSERT INTO orders (id, customer_id, product, quantity, discount_pct)
            VALUES (?, ?, ?, ?, ?)
            """,
            order_rows,
        )

        # Save the new tables and their rows only after every step succeeds.
        connection.commit()
        import_succeeded = True

        # Check the saved counts; fetchone()[0] extracts the returned number.
        print("Base enregistrée :", DATABASE_PATH)
        print(
            "Clients :",
            connection.execute(
                """
                SELECT COUNT(*)
                FROM customers
                """
            ).fetchone()[0],
        )
        print(
            "Commandes :",
            connection.execute(
                """
                SELECT COUNT(*)
                FROM orders
                """
            ).fetchone()[0],
        )

        print(
            "Âges manquants :",
            connection.execute(
                """
                SELECT COUNT(*)
                FROM customers
                WHERE age IS NULL
                """
            ).fetchone()[0],
        )
        print(
            "Remises manquantes :",
            connection.execute(
                """
                SELECT COUNT(*)
                FROM orders
                WHERE discount_pct IS NULL
                """
            ).fetchone()[0],
        )

    except sqlite3.Error as error:
        # Undo uncommitted changes, including table drops and creation.
        connection.rollback()
        raise SystemExit(f"Import annulé : {error}") from error

    finally:
        # Release the file even when an import fails.
        connection.close()

        # Avoid leaving an empty file after a failed first import.
        if not database_existed and not import_succeeded:
            DATABASE_PATH.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
