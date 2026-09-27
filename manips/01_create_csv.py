"""Create the two small fictional CSV files, preserving their literal text."""
import csv
from pathlib import Path

# Locate the output folder relative to this script, not the terminal folder.
DATA_DIR = Path(__file__).resolve().parent / "data"

# Keep values as text, including leading zeros and missing-value markers.
# Columns: id, name, age, city.
CUSTOMERS = [
    ("001", "Alice", "34", "Saint-Étienne"),
    ("002", "Bilal", "47", "Lyon"),
    ("003", "Chloé", "", "Saint-Étienne"),
    ("004", "David", "29", "Grenoble"),
    ("005", "Emma", "52", "Lyon"),
    ("006", "Farid", "41", "Saint-Étienne"),
    ("007", "Gaëlle", "36", "Grenoble"),
    ("008", "Hugo", "63", "Lyon"),
    ("009", "Inès", "27", "Saint-Étienne"),
    ("010", "Jules", "45", "Grenoble"),
    ("011", "Katia", "NA", "Lyon"),
    ("012", "Luc", "31", "Saint-Étienne"),
]

# Columns: id, customer_id, product, quantity, discount_pct.
ORDERS = [
    ("001", "001", "Clavier", "1", "0"),
    ("002", "002", "Souris", "2", "10"),
    ("003", "001", "Écran", "1", ""),
    ("004", "003", "Casque", "1", "NA"),
    ("005", "004", "Webcam", "1", "unknown"),
    ("006", "005", "Clavier", "2", "0"),
    ("007", "006", "Souris", "3", "10"),
    ("008", "007", "Écran", "1", "5"),
    ("009", "008", "Casque", "2", "0"),
    ("010", "009", "Webcam", "1", "15"),
    ("011", "002", "Clavier", "1", ""),
    ("012", "010", "Souris", "1", "0"),
]


def main():
    # Create the output folder if it does not exist yet.
    DATA_DIR.mkdir(exist_ok=True)

    tables = [
        (
            "customers.csv",
            ["id", "name", "age", "city"],
            CUSTOMERS,
        ),
        (
            "orders.csv",
            ["id", "customer_id", "product", "quantity", "discount_pct"],
            ORDERS,
        ),
    ]

    for filename, columns, rows in tables:
        path = DATA_DIR / filename

        # "w" replaces this CSV. Write its header once, then the data rows.
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream) #crée un objet capable d'écrire des données CSV
            writer.writerow(columns) # écrit l'en-tête
            writer.writerows(rows) # écrit les lignes

        # Display the saved text, including empty cells and NA markers.
        print(f"{path.name} : {len(rows)} lignes de données")
        print(path.read_text(encoding="utf-8"))

    print(
        "Les CSV de démonstration ont été écrits. "
        "La base existante reste indépendante."
    )


if __name__ == "__main__":
    main()
