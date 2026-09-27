"""Apply four explicit changes and check that they persist after reopening."""

import sqlite3

from data_io import DATABASE_PATH


def show_target_rows(connection):
    # Show the same records before editing, after editing and after reopening.
    print(
        "Client 003 :",
        connection.execute(
            """
            SELECT
                id,
                name,
                city
            FROM customers
            WHERE id = ?
            """,
            ("003",),
        ).fetchall(),
    )

    print(
        "Commandes 002, 004 et 012 :",
        connection.execute(
            """
            SELECT
                id,
                quantity,
                discount_pct
            FROM orders
            WHERE id IN (?, ?, ?)
            ORDER BY id
            """,
            ("002", "004", "012"),
        ).fetchall(),
    )


def main():
    # Require the database created by 03 before opening a connection.
    if not DATABASE_PATH.is_file():
        raise SystemExit("Base absente. Exécutez 03_create_database.py.")

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        # Enforce the declared links between orders and customers.
        connection.execute("PRAGMA foreign_keys = ON")

        print("AVANT")
        show_target_rows(connection)

        # Check that all records needed by this example still exist.
        # A previous run deletes order 012, so restart with 03 before repeating.
        required_customer = connection.execute(
            """
            SELECT COUNT(*)
            FROM customers
            WHERE id = ?
            """,
            ("003",),
        ).fetchone()[0]

        required_orders = connection.execute(
            """
            SELECT COUNT(*)
            FROM orders
            WHERE id IN (?, ?, ?)
            """,
            ("002", "004", "012"),
        ).fetchone()[0]

        if required_customer != 1 or required_orders != 3:
            raise SystemExit(
                "Les lignes de l'exemple ne sont plus toutes présentes.\n"
                "Pour recommencer : python 03_create_database.py"
            )

        # Fictional corrections supplied by a verified source for this exercise.
        # Each ? receives its value from the tuple after the SQL text.
        # With this connection, the first UPDATE starts a transaction automatically.
        connection.execute(
            "UPDATE customers SET city = ? WHERE id = ?",
            ("Lyon", "003"),
        )

        connection.execute(
            "UPDATE orders SET quantity = ? WHERE id = ?",
            (3, "002"),
        )

        # Here, 5 replaces an unknown discount with a confirmed value.
        connection.execute(
            "UPDATE orders SET discount_pct = ? WHERE id = ?",
            (5.0, "004"),
        )

        connection.execute(
            "DELETE FROM orders WHERE id = ?",
            ("012",),
        )

        # This connection can see its changes before they are saved.
        print("\nAPRÈS MODIFICATION, AVANT ENREGISTREMENT")
        show_target_rows(connection)

        # Save all four changes together.
        connection.commit()

    except sqlite3.Error as error:
        # Cancel the uncommitted changes if a SQL operation fails.
        connection.rollback()
        raise SystemExit(f"Modifications annulées : {error}") from error

    finally:
        connection.close()

    # A new connection verifies that commit() saved the changes to the file.
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        print("\nAPRÈS FERMETURE ET RÉOUVERTURE")
        show_target_rows(connection)

        print(
            "Commandes enregistrées :",
            connection.execute(
                """
                SELECT COUNT(*)
                FROM orders
                """
            ).fetchone()[0],
        )

    finally:
        connection.close()


if __name__ == "__main__":
    main()
