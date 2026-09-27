"""Read, display and describe the two CSV tables."""

from data_io import read_tables


def main():
    # data_io defines the column types and the missing-value rules.
    customers, orders = read_tables()

    # Show all rows, column types and numeric summaries for customers.
    print("CUSTOMERS")
    print(customers.to_string(index=False))

    customers.info()

    # Numeric summaries use known values; missing values are excluded.
    print(customers.describe())

    # Apply the same inspection to orders.
    print("\nORDERS")
    print(orders.to_string(index=False))

    orders.info()

    print(orders.describe())


if __name__ == "__main__":
    main()
