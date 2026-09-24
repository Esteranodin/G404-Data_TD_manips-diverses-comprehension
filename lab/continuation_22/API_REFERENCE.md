# Repères Python — lire, calculer, réutiliser

Cette fiche, reprise du cours du 22 septembre, aide à retrouver les fonctions
utiles. Les notebooks indiquent ce qui est
à pratiquer et ce qui est facultatif. Code en anglais ; explications en français.

## Reconnaître ce que l'on manipule

Un `dtype` décrit le type des valeurs d'une colonne ou d'un tableau NumPy.
Une `Series` est une colonne pandas munie d'étiquettes appelées index ; une
`DataFrame` est une table composée de plusieurs colonnes.

| Expression | Ce que c'est |
|---|---|
| `pd` après `import pandas as pd` | Le module pandas, sous un alias |
| `pd.read_csv` | Une fonction ; `pd.read_csv(...)` l'appelle |
| `pd.DataFrame` | Une classe ; le tableau créé est une instance |
| `tickets` | Un nom qui référence l'objet tableau |
| `tickets.shape` | Un attribut donnant le nombre de lignes et de colonnes |
| `tickets.head()` | Un appel de méthode sur ce tableau |
| `tickets["resolution_minutes"]` | Une Series, avec son index et son dtype |
| `type(tickets)` / `tickets.dtypes` | Type de l'objet / types des colonnes |

## CSV et valeurs manquantes

`pd.read_csv` lit un chemin ou un objet fichier. `StringIO(csv_text)` fait
apparaître une chaîne comme un fichier texte en mémoire. Recréer cet objet
pour chaque lecture : sa position avance pendant la lecture.

| Paramètre | Question à se poser |
|---|---|
| `dtype={"ticket_id": "string", "resolution_minutes": "Float64"}` | Quel type impose-t-on à chaque colonne ? Les zéros initiaux d'un identifiant comptent-ils ? |
| `keep_default_na=True` | Les marqueurs manquants habituels doivent-ils être reconnus ? |
| `keep_default_na=False` | Veut-on limiter les marqueurs à ceux déclarés, ou préserver le texte ? |
| `na_values={"resolution_minutes": ["", "NA", "unknown"]}` | Quelles chaînes signifient une donnée manquante dans cette colonne ? |
| `na_filter=False` | Désactive-t-on la reconnaissance des NA ? Ce réglage ignore les deux paramètres NA précédents. |
| `sep`, `decimal`, `encoding`, `usecols` | Quel séparateur, notation décimale, encodage et sous-ensemble de colonnes ? |

`None` représente une absence en Python ; dans pandas, la représentation
dépend du dtype : `np.nan` pour `float64` et le texte `str` de pandas 3,
`pd.NA` pour les types acceptant des valeurs manquantes, nommés `Int64`, `Float64`, `boolean`, `string`,
`pd.NaT` pour les dates. Un entier NumPy `int64` ne représente pas directement
un NA ; le dtype pandas `Int64` le permet. Les majuscules ont donc un sens.

Détecter avec `pd.isna(value)`, `series.isna()` ou `.notna()`. Ne pas tester avec
`== np.nan`. Une valeur inconnue n'est pas zéro. `False` et `""` ne sont pas
intrinsèquement manquants ; la lecture du CSV peut interpréter une cellule vide comme NA.

`pd.to_numeric(values, errors="raise")` signale une conversion impossible.
Avec `errors="coerce"`, elle devient manquante : inspecter les valeurs qui ont
changé, ne pas confondre donnée absente et erreur de saisie. Même idée pour
`pd.to_datetime(..., errors="coerce")`. `.astype(...)` impose un type compatible.

Sources : [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html),
[NA](https://pandas.pydata.org/docs/user_guide/missing_data.html),
[texte pandas 3](https://pandas.pydata.org/docs/user_guide/migration-3-strings.html).

## Sélectionner, contrôler et calculer

```python
mask = tickets["channel"] == "phone"
durations = tickets.loc[mask, "resolution_minutes"]
valid_durations = durations.dropna()
```

`.loc` sélectionne par étiquettes de ligne ou de colonne, ou par conditions
booléennes ; `.iloc` sélectionne par positions.
Avec des Series booléennes, combiner des conditions parenthésées avec `&` et
`|`, inverser avec `~`. `and` et `or` ne combinent pas élément par élément.

| Opération | Sens / précaution |
|---|---|
| `len(durations)` / `durations.count()` | Toutes les lignes / valeurs non manquantes |
| `.mean()`, `.median()`, `.quantile(0.25)` | Statistiques calculées sur les valeurs disponibles par défaut |
| `.std(ddof=1)` | Convention d'écart-type d'échantillon ; la rendre explicite |
| `(valid_durations >= threshold).sum()` | Nombre de valeurs au moins égales au seuil |
| `.sum(min_count=1)` | Préserve un résultat manquant si aucune valeur n'est disponible ; `.sum()` seul peut renvoyer 0 |
| `.value_counts(dropna=False)` | Compter aussi les valeurs manquantes |
| `.str.strip().str.lower()` | Normaliser du texte si cette décision a un sens |
| `.copy()` | Créer une copie explicite avant une modification |
| `.fillna(0)` | Choix d'interprétation à justifier, jamais une correction automatique universelle |
| `.to_csv(path, index=False)` | Écrire le tableau sans ajouter son index au CSV |

## Fonction et lambda

Une fonction reçoit des arguments, effectue un traitement et renvoie un objet.
`print` affiche ; `return` transmet au code appelant ; `to_csv` écrit sur disque.
Sans retour explicite, une fonction renvoie `None`.

```python
def minutes_to_hours(minutes):
    return minutes / 60

hours = list(map(minutes_to_hours, [30, 60, 90]))
hours = list(map(lambda minutes: minutes / 60, [30, 60, 90]))
```

| Appel | Objet reçu par la fonction transmise |
|---|---|
| `map(function, values)` | Un élément ; le résultat est un itérateur |
| `series.map(function, na_action="ignore")` | Une valeur non manquante |
| `series.map(mapping_dict)` | Correspondance de valeurs ; une clé absente donne un NA |
| `sorted(records, key=function)` | Un élément dont on calcule la clé de tri |
| `grouped.agg(function)` | Une Series du groupe et de la colonne agrégée |
| `frame.apply(function, axis=1)` | Une ligne sous forme de Series (réglages par défaut) |

Une lambda contient une expression et renvoie son résultat. Elle ne remplace
pas toutes les fonctions nommées. Comparer à `durations / 60`, qui exprime déjà
la conversion élément par élément. `apply` est une extension de lecture,
pas une étape obligatoire de l'exercice.

## Simulation et graphiques : le mélange gaussien

`np.random.default_rng(seed)` crée un générateur reproductible ;
`rng.normal(loc=mean, scale=std_dev, size=n)` renvoie `n` valeurs NumPy.
`np.concatenate([a, b])` rassemble les valeurs ; une colonne `component`
indique leur origine. Un mélange réunit des observations de A **ou** de B,
pas la somme de deux tirages. La méthode `sample` garde la DataFrame dans
`self.samples` et la renvoie aussi.

| Méthode de la classe | Figure renvoyée | Question |
|---|---|---|
| `plot_components()` | `px.histogram(..., color="component", barmode="overlay", histnorm="probability density")` | Les distributions A et B se recouvrent-elles ? |
| `plot_mixture()` | `px.histogram(..., x="value")` | Que voit-on sans les étiquettes de composante ? |
| `plot_box()` | `px.box(..., x="component", y="value")` | Centres et dispersions diffèrent-ils ? |

La classe **renvoie** des objets `Figure`. Le notebook choisit quand appeler
`figure.show()`. Comparer les figures avec les effectifs et statistiques du
DataFrame ; une visualisation seule ne valide pas le code.

## Classe, instance et module

- `class`, `__init__` et `self` définissent un type et l'état de chaque
  instance. Une méthode peut appeler une fonction existante.
- `first = GaussianMixture(...)` et `second = GaussianMixture(...)` créent deux
  états indépendants. Une redéfinition de la classe dans le notebook ne
  transforme pas les instances déjà créées : recréez-les.
- `my_gaussian_mixture.py` est votre module personnel. Il contient les imports,
  `draw_component`, `combine_components` et `GaussianMixture`, sans données de
  démonstration. `import my_gaussian_mixture as gm`, puis
  `gm.GaussianMixture(...)`. Le notebook garde les paramètres, appels,
  graphiques et interprétations.
- Enregistrer le module, redémarrer le noyau, tout exécuter. Un import déjà
  exécuté peut garder la version précédente du fichier. `gm.__file__` montre
  quel fichier a été importé.
- `Path.cwd()` montre le dossier de travail du noyau. `__file__` n'est pas
  disponible dans un notebook comme dans un script Python ordinaire.

Les exemples précédents sur les tickets illustrent la lecture et les calculs
sur une table. Ils ne constituent pas un travail supplémentaire à rendre.

Sources : [fonctions Python](https://docs.python.org/3/tutorial/controlflow.html),
[modules](https://docs.python.org/3/tutorial/modules.html),
[classes](https://docs.python.org/3/tutorial/classes.html),
[NumPy Generator](https://numpy.org/doc/stable/reference/random/generator.html),
[Plotly Express](https://plotly.com/python/plotly-express/).
