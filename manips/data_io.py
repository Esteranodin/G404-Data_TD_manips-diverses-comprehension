"""CSV and SQLite paths, with explicit rules for reading the CSV tables."""

from pathlib import Path

import pandas as pd


# Find the data beside this module, regardless of the terminal folder.
DATA_DIR = Path(__file__).resolve().parent / "data"

CUSTOMERS_CSV = DATA_DIR / "customers.csv"
ORDERS_CSV = DATA_DIR / "orders.csv"

DATABASE_PATH = DATA_DIR / "shop.sqlite"


def read_tables():
    """Return typed tables; reject missing files and unexpected columns."""
    # Both input files are required before either table can be returned.
    for path in (CUSTOMERS_CSV, ORDERS_CSV):
        if not path.is_file():
            raise SystemExit(f"Fichier absent : {path}\nExécutez 01_create_csv.py.")

    # Keep identifiers such as 001 as text; Int64 allows missing ages.
    # Recognize missing-value markers only in age, not in names or cities.
    customers = pd.read_csv(
        CUSTOMERS_CSV,
        dtype={
            "id": "string",
            "name": "string",
            "age": "Int64",
            "city": "string",
        },
        keep_default_na=False,
        na_values={"age": ["", "NA", "unknown"]},
    )

    # Float64 allows missing discounts. A numeric zero remains a known value.
    # keep_default_na=False uses only the missing-value rules given here.
    orders = pd.read_csv(
        ORDERS_CSV,
        dtype={
            "id": "string",
            "customer_id": "string",
            "product": "string",
            "quantity": "Int64",
            "discount_pct": "Float64",
        },
        keep_default_na=False,
        na_values={"discount_pct": ["", "NA", "unknown"]},
    )

    # Check column names and order before passing the tables to other scripts.
    expected_customers = ["id", "name", "age", "city"]
    expected_orders = ["id", "customer_id", "product", "quantity", "discount_pct"]

    if list(customers.columns) != expected_customers:
        raise ValueError(
            f"Colonnes attendues dans customers.csv : {expected_customers}"
        )

    if list(orders.columns) != expected_orders:
        raise ValueError(f"Colonnes attendues dans orders.csv : {expected_orders}")

    return customers, orders
