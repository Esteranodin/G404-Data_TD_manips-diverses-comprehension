"""Read an explicit configuration file without changing process variables."""

import os
import sys
from pathlib import Path


def parse_integer(value: str | None, name: str, minimum: int, maximum: int) -> int:
    """Parse a bounded integer from a configuration string."""
    if value is None:
        raise ValueError(f"{name} : valeur manquante.")
    try:
        result = int(value)
    except ValueError as error:
        raise ValueError(f"{name} : entier attendu, valeur reçue : {value!r}.") from error
    if not minimum <= result <= maximum:
        raise ValueError(f"{name} : valeur attendue entre {minimum} et {maximum}.")
    return result


def read_config(config_path: Path) -> dict[str, str | int]:
    """Read only the specified file and validate the three course settings."""
    from dotenv import dotenv_values
    #  module qui permet de lire un fichier .env sans toucher aux variables globales de l’environnement

    if not config_path.is_file():
        raise FileNotFoundError(
            "Fichier .env absent : copiez .env.example vers .env dans lab."
        )
    raw = dotenv_values(config_path, encoding="utf-8", interpolate=False)
    label = raw.get("COURSE_LABEL")
    if (
        label is None
        or not label.strip()
        or len(label) > 60
        or "\n" in label
        or "\r" in label
    ):
        raise ValueError("COURSE_LABEL : texte non vide, une ligne, 60 caractères maximum.")
    return {
        "COURSE_LABEL": label.strip(),
        "N_VALUES": parse_integer(raw.get("N_VALUES"), "N_VALUES", 1, 1_000_000),
        "N_WORKERS": parse_integer(raw.get("N_WORKERS"), "N_WORKERS", 1, 4),
    }


def main() -> int:
    """Display validated values and their Python types."""
    config_path = Path(__file__).resolve().parent / ".env"
    # \ concatène sur un path
    try:
        config = read_config(config_path)
    except ModuleNotFoundError as error:
        if error.name != "dotenv":
            raise
        print("Package python-dotenv absent dans cet interpréteur.", file=sys.stderr)
        prefix = "& " if os.name == "nt" else ""
        print(
            f'Commande : {prefix}"{sys.executable}" -m pip install '
            '"python-dotenv>=1.0,<2"',
            file=sys.stderr,
        )
        print("Voir ENVIRONMENT.md pour la syntaxe PowerShell et Bash.", file=sys.stderr)
        return 1
    except (OSError, ValueError) as error:
        print(f"Configuration invalide : {error}", file=sys.stderr)
        return 1
    print("Configuration lue explicitement depuis le fichier .env du lab.")
    for name, value in config.items():
        print(f"{name} = {value!r} ; type après validation : {type(value).__name__}")
    print("Aucune variable de os.environ n'a été modifiée.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
