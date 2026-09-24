from geometry import Rectangle

def main() -> None:
    rect = Rectangle(4, 3)
    print(f"Rectangle(4, 3) area = {rect.area()}")


if __name__ == "__main__":
    main()

# Cette condition vérifie comment ce fichier est utilisé.
# Si le fichier est lancé directement avec Python, __name__ vaut "__main__"
# et la fonction main() est exécutée.
# Si le fichier est importé par un autre module, la condition est fausse :
# main() n'est pas exécutée automatiquement.
# Cela permet d'utiliser les fonctions et les classes sans lancer le programme (par exemple lors d'un import, notamment lancer des tests non voulus)