"""Read, filter and join tables; compare missing-value counts and means."""

import sqlite3

import pandas as pd

from data_io import DATABASE_PATH


def show_query(connection, title, sql, parameters=()):
    print(f"\n{title}")

    # Run the query with its values supplied separately from the SQL text.
    cursor = connection.execute(sql, parameters)

    # Display the column names, then each returned row.
    print(" | ".join(column[0] for column in cursor.description))

    for row in cursor.fetchall():
        print(row)


def main():
    # Check the file first: connect() would otherwise create an empty database.
    if not DATABASE_PATH.is_file():
        raise SystemExit("Base absente. Exécutez 03_create_database.py.")

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        # Select three columns and display customers in identifier order.
        show_query(
            connection,
            "CHOISIR DES COLONNES",
            """
            SELECT
                id,
                name,
                city
            FROM customers
            ORDER BY id
            """,
        )

        # Keep customers from Lyon aged 35 or older; show the oldest first.
        show_query(
            connection,
            "FILTRER PUIS TRIER",
            """
            SELECT
                id,
                name,
                age
            FROM customers
            WHERE city = ? AND age >= ?
            ORDER BY age DESC, id
            """,
            ("Lyon", 35),
        )

        # Join orders.customer_id to customers.id.
        show_query(
            connection,
            "RELIER CHAQUE COMMANDE À SON CLIENT",
            """
            SELECT
                o.id,
                c.name,
                o.product,
                o.quantity,
                o.discount_pct
            FROM orders AS o
            #
            #
            """,
        )

        # IS NULL finds missing discounts; zero remains a known value.
        show_query(
            connection,
            "COMMANDES DONT LA REMISE EST INCONNUE",
            """
            SELECT
                id,
                customer_id,
                discount_pct
            FROM orders
            #
            #
            """,
        )

        # JOIN that keeps customers even when no order matches.
        show_query(
            connection,
            "CONSERVER AUSSI LES CLIENTS SANS COMMANDE",
            """
            SELECT
                c.id,
                c.name,
                o.id AS order_id,
                o.discount_pct
            FROM customers AS c
            #
            #
            """,
        )

        print("order_id vaut None : aucune commande ; sinon la commande existe.")
        print("None est ici l'affichage Python du NULL SQL.")

        # Group by customer; COUNT(o.id) ignores the NULL for an absent order.
        # COUNT(o.discount_pct) counts only orders with a known discount.
        show_query(
            connection,
            "ALLER PLUS LOIN : COMPTER LES COMMANDES PAR CLIENT",
            """
            xxx
            """,
        )

        # COUNT(*) counts rows; COUNT(column) and AVG(column) ignore NULL.
        show_query(
            connection,
            "COMPTER ET CALCULER UNE MOYENNE EN SQL",
            """
            SELECT
                xxx
            FROM orders
            """,
        )

        # Read the same database values to make a fair comparison with pandas.
        rows = connection.execute(
            """
            SELECT discount_pct
            FROM orders
            ORDER BY id
            """
        ).fetchall()

        # Extract one value per row; Float64 accepts numbers and missing values.
        discounts = pd.Series([row[0] for row in rows], dtype="Float64")

        print("\nLES MÊMES VALEURS DE LA BASE DANS PANDAS")
        print(
            "Lignes :", len(discounts),
            "| Connues :", discounts.count(),
            "| Manquantes :", discounts.isna().sum(),
            "| Moyenne (%) :", discounts.mean(),
        )

    finally:
        # Close the connection even if a query fails.
        connection.close()


if __name__ == "__main__":
    main()
