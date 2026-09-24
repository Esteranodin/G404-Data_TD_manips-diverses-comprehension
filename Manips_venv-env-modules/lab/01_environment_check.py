"""Inspect the current interpreter without installing or changing anything."""

import importlib.metadata
import importlib.util
import sys
from pathlib import Path


def main() -> None:
    print(f"Python exécuté : {sys.executable}")
    print(f"Version : {sys.version.split()[0]}")
    print(f"Dossier courant : {Path.cwd()}")
    print(f"Environnement virtuel actif : {sys.prefix != sys.base_prefix}")
    print(f"Préfixe Python : {sys.prefix}")
    print("\nPaquets visibles depuis CET interpréteur :")
    for module_name, distribution_name in (
        ("numpy", "numpy"),
        ("ipykernel", "ipykernel"),
        ("dotenv", "python-dotenv"),
    ):
        available = importlib.util.find_spec(module_name) is not None
        if available:
            try:
                version = importlib.metadata.version(distribution_name)
            except importlib.metadata.PackageNotFoundError:
                version = "version non disponible"
            print(f"  {distribution_name} : présent ({version})")
        else:
            print(f"  {distribution_name} : absent")
    print("\nComparer ce chemin Python à sys.executable dans le notebook.")
    print("Un paquet absent n'empêche pas les exercices Python standard.")


if __name__ == "__main__":
    main()
