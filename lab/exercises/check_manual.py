"""Inspect every case; exit unsuccessfully until the visible contract holds."""

from math import isclose

from duration_tools import minutes_to_hours


def main() -> None:
    failed = 0
    for minutes, expected in ((0, 0.0), (60, 1.0), (90, 1.5), (-60, -1.0)):
        result = minutes_to_hours(minutes)
        valid = isinstance(result, float) and isclose(result, expected)
        print(
            f"minutes={minutes}, attendu={expected!r}, obtenu={result!r}, "
            f"type={type(result).__name__} : {'OK' if valid else 'À CORRIGER'}"
        )
        failed += not valid
    if failed:
        raise SystemExit(f"{failed} cas non conforme(s). Lire valeur ET type.")
    print("Contrôles réussis. Ajouter les limites avant de conclure.")


if __name__ == "__main__":
    main()
