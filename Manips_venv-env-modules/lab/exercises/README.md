# Exercice commun : convertir une durée

Commencez par le socle, puis choisissez un approfondissement A, B ou C.
Toutes les commandes partent du dossier `lab`, avec le Python de votre projet.

## Socle commun

`duration_tools.py` contient une fonction dont le **résultat a volontairement
le mauvais type**. Le calcul et le texte de présentation ont des responsabilités
distinctes. Observer la valeur et le type avant de modifier le code.

```text
python exercises/check_manual.py
```

Corriger `minutes_to_hours` pour que les trois contrôles réussissent :

| Entrée en minutes | Sortie en heures | Type de sortie |
| --- | --- | --- |
| `0` | `0.0` | `float` |
| `60` | `1.0` | `float` |
| `90` | `1.5` | `float` |

Conserver ces trois contrôles, ajouter un quatrième cas choisi et justifié,
puis expliquer le défaut, la correction et la possibilité de réutiliser le
résultat dans un calcul. Si vous voulez afficher « heures », construire ce
texte dans l'appelant. Les trois cas réussis valident le socle, pas encore
toutes les limites du contrat.

## Contrat complet de `minutes_to_hours(minutes: float) -> float`

- Une valeur réelle finie, positive ou nulle, donne un résultat numérique de
  type `float`. Les fractions de minute restent valides : `0.5` minute
  représente `1/120` heure.
- Refuser les booléens et les valeurs non réelles par `TypeError` : exemples
  `True`, `"90"`, `None` et `90 + 0j`. Ne pas convertir silencieusement une
  chaîne de caractères.
- Refuser les valeurs négatives, infinies et `NaN` par `ValueError`.
- Ne pas afficher depuis la fonction. Un appelant choisit sa présentation.

L'annotation décrit le contrat ; elle ne convertit ni ne vérifie les valeurs
à elle seule. Le domaine numérique utilisé dans cet exercice est celui des
valeurs représentables comme nombres flottants finis Python.

## Formaliser le module et ses tests

La fonction reste définie à un seul endroit : `duration_tools.py`. Les tests
l'importent depuis ce module. Compléter la validation des entrées et remplacer
chaque TODO dans `tests/test_duration.py` par des contrôles justifiés.

```bash
python -m unittest discover -s exercises/tests -v
# pour lancer les tests (et bien à partir de \lab !)
```

Les TODO provoquent un **échec explicite** avant leur remplacement. Utiliser
`assertAlmostEqual` pour les résultats décimaux et `assertRaises` pour les
entrées invalides. Conserver les cas usuels du socle dans les tests. Un test
doit refuser au moins une erreur plausible ; modifier le contrat pour obtenir
« OK » ne constitue pas une correction.

Preuve attendue : fichiers modifiés, noms et nombre de tests exécutés, sortie
de la commande et explication d'un cas limite. Exécuter la commande dans un
nouveau processus pour utiliser le module enregistré.