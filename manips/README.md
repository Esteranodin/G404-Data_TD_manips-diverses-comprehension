# Du CSV à une base SQLite

Suivez les mêmes données à chaque étape : lire du texte, choisir les types,
repérer ce qui manque, puis sélectionner et modifier des lignes en SQL.
Les scripts `01`, `02`, `03` et `05` sont des exemples complets.
**`04_select_data.py` est l'exercice : les requêtes SQL sont à compléter.**

## Exécuter les exemples

Dans le terminal, utilisez l'environnement Python du cours :

```bash
python -m pip install pandas
python -c "import sqlite3; print(sqlite3.sqlite_version)"
```

La seconde commande affiche la version de SQLite disponible. `sqlite3` est
normalement fourni avec Python ; aucun serveur n'est à installer. Si le module
manque, utilisez une installation de Python qui l'inclut. `csv` est également
fourni avec Python. Si votre commande est `python3`, remplacez `python` par
`python3` dans toutes les commandes.

Depuis le dossier `lab/sql` :

```bash
python 01_create_csv.py
python 02_read_csv.py
python 03_create_database.py
```

Complétez ensuite les requêtes de `04_select_data.py` selon la section 4,
puis exécutez :

```bash
python 04_select_data.py
python 05_modify_data.py
```

Terminez et vérifiez `04` avant de lancer `05`, qui modifie les données.

Une fois les requêtes complétées, `python 00_do_all.py` enchaîne les cinq
scripts avec le même Python. Il recrée les CSV et la base, puis applique `05`.
Il s'arrête à la première erreur, notamment si `04` est encore incomplet.

Depuis un autre dossier, donnez le chemin du script. Les fichiers créés
restent dans `lab/sql/data/`, à côté du code. Lisez le résultat d'une étape
avant de passer à la suivante.

`01` écrit ou réécrit les deux CSV de démonstration. À chaque exécution,
`03` recrée les deux tables à partir des CSV actuels : les modifications
précédentes de ces tables sont remplacées. Aucun argument n'est nécessaire.

Pour retrouver le début de l'exemple, relancez `01`, puis `03`.
Relancer seulement `03` conserve les changements éventuels dans les CSV.
Relancer `05` sans recréer la base est refusé, car la commande `012` a déjà
été supprimée. Les étapes `03` à `05` ne modifient pas les CSV.

## Les données et le sens des valeurs

Les personnes et commandes sont fictives. Chaque CSV contient **12 lignes
de données et une ligne d'en-tête**.

| Fichier | Une ligne représente | Colonnes |
| --- | --- | --- |
| `customers.csv` | Un client | `id`, `name`, `age`, `city` |
| `orders.csv` | Une commande d'un seul produit | `id`, `customer_id`, `product`, `quantity`, `discount_pct` |

`id` est un identifiant, pas une quantité : les zéros de `"001"` restent
utiles. `customer_id` relie une commande au client de même `id`.
`quantity` est le nombre d'unités commandées ; `discount_pct` est la remise
en pourcentage, de 0 à 100.
Une remise `0` signifie « aucune remise ». **Dans les colonnes `age` et
`discount_pct` de cet exemple**, une cellule vide, `NA` ou `unknown`
signifie « valeur non renseignée ». Cette règle ne s'applique pas aux noms,
villes ou identifiants. Une erreur de saisie inconnue demande une vérification.

## 1. Créer puis regarder le texte

Ouvrez les CSV créés par `01`. Retrouvez les identifiants et les cinq
premières remises : `0`, `10`, cellule vide, `NA`, `unknown`.

**Avant `02` :** quelles colonnes doivent rester du texte ? Où attendez-vous
les valeurs manquantes ?

## 2. Lire, afficher et décrire les tables

`customers, orders = read_tables()` charge les deux tables avec les règles
de **`data_io.py`**, qui regroupe les chemins des CSV et de la base SQLite,
ainsi que les règles de lecture des CSV. Le script affiche ensuite
chaque table complète, ses colonnes et ses statistiques numériques.

Le [notebook CSV](../csv_examples/04_CSV_types_missing_values_FR.ipynb)
illustre ces règles sur cinq tickets fictifs, comme les slides 16–21.

| Instruction | Résultat |
| --- | --- |
| `print(table.to_string(index=False))` | Toutes les lignes, sans numéro d'index ajouté |
| `table.info()` | Colonnes, types et nombre de valeurs non manquantes |
| `print(table.describe())` | Statistiques des colonnes numériques : count, moyenne, dispersion et quartiles |

Dans `describe()`, `count` compte les valeurs connues et la moyenne exclut les
valeurs manquantes. Les statistiques portent sur chaque table complète.
Les identifiants restent du texte ; `Int64` et `Float64` acceptent des valeurs
numériques et des manques. Les colonnes `age` et `discount_pct` ont respectivement
2 et 4 valeurs manquantes. Le zéro reste une valeur connue.

Les règles de `read_csv`, dont `dtype` et `na_values`, restent visibles dans
`data_io.py`. `02` utilise une seule lecture et n'applique aucun remplacement
aux valeurs manquantes.

## Python et les autres bases SQL

Python utilise un **connecteur** : un module qui ouvre la connexion, transmet
les requêtes SQL et récupère les résultats. Un `SELECT` renvoie des lignes ;
une modification peut seulement confirmer son exécution. L'accès dépend de
la base :

| Base | Paquet à installer avec pip | Module à importer | Informations de connexion |
| --- | --- | --- | --- |
| SQLite | Normalement fourni avec Python | `sqlite3` | Chemin du fichier, ici `data/shop.sqlite` |
| MySQL | `mysql-connector-python` | `mysql.connector` | Adresse du serveur, port, nom de la base et identifiants de connexion |
| PostgreSQL | `psycopg[binary]` | `psycopg` | Adresse du serveur, port, nom de la base et identifiants de connexion |

Un serveur MySQL ou PostgreSQL peut fonctionner sur le même ordinateur que
Python ou sur une autre machine. Installer le connecteur Python n'installe pas
le serveur et ne crée pas de compte. Le serveur doit être disponible et le
compte doit avoir les droits nécessaires. Les connecteurs et certaines formes
de SQL diffèrent : changer le nom importé ne suffit pas à adapter un programme.

L'atelier utilise **SQLite**. Pour un autre projet avec MySQL ou PostgreSQL,
les commandes d'installation des connecteurs sont respectivement :

```bash
python -m pip install mysql-connector-python
python -m pip install "psycopg[binary]"
```

Le complément `[binary]` fournit les bibliothèques clientes de PostgreSQL ;
le module à importer reste `psycopg`. Repères officiels :
[SQLite dans Python](https://docs.python.org/3/library/sqlite3.html),
[installation MySQL](https://dev.mysql.com/doc/connector-python/en/ch04s04s01.html),
[connexion MySQL](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html),
[installation Psycopg](https://www.psycopg.org/psycopg3/docs/basic/install.html) et
[connexion PostgreSQL](https://www.psycopg.org/psycopg3/docs/basic/usage.html).

## 3. Importer en SQLite

Lisez `03` avant de l'exécuter. `CREATE TABLE` fixe les colonnes.
Une clé primaire identifie chaque ligne ; une clé étrangère relie les
commandes aux clients. `PRAGMA foreign_keys = ON` active ce contrôle.

`executemany()` insère plusieurs lignes. Les `?` reçoivent séparément les
valeurs : on ne fabrique pas la requête en collant du texte.
Les valeurs manquantes pandas deviennent `None` en Python, puis `NULL` en
SQLite. `int()` et `float()` fournissent les nombres attendus par SQLite.
`itertuples()` parcourt les lignes du tableau ; `row.discount_pct` lit la
remise de la ligne courante.

`commit()` enregistre les changements ; `rollback()` les annule si
l'import échoue. `close()` ferme la connexion. Le fichier `shop.sqlite`
conserve les données après la fermeture du programme.

## 4. Compléter les requêtes SQL

Dans `04_select_data.py`, les deux premières requêtes sont des exemples
complets. Les cinq suivantes sont à compléter : remplacez les lignes `#`
et les marqueurs `xxx` dans les chaînes SQL. Ce sont des emplacements à
remplir, pas du SQL exécutable. Le script s'arrête au premier emplacement
non complété. Gardez le code Python fourni.
Relancez le script après chaque requête complétée pour vérifier votre résultat.

Les titres indiquent les résultats attendus : relier commandes et clients,
trouver les remises inconnues, conserver les clients sans commande, compter
les commandes par client, puis compter les remises et calculer leur moyenne.
Une jointure relie ici `customers.id` à `orders.customer_id`.

Pour les deux blocs `xxx`, produire les identifiants et noms des clients,
leurs nombres de commandes et de remises connues, clients sans commande
inclus ; puis les nombres total, connu et manquant des remises et leur moyenne
sur les valeurs connues.

**Avant chaque requête :** annoncez les colonnes attendues et les lignes
qui devraient être présentes. Après avoir complété le script, changez le
filtre de ville et d'âge pour vérifier votre compréhension.

Avec `LEFT JOIN`, un client sans commande reste visible. Si `order_id`
est manquant, aucune commande ne correspond. Si `order_id` est présent
et la remise manque, la commande existe mais sa remise est inconnue.
Python affiche les `NULL` renvoyés par SQLite sous la forme `None`.

| Besoin | pandas | SQL |
| --- | --- | --- |
| Compter les lignes | `len(values)` | `COUNT(*)` |
| Compter les valeurs connues | `values.count()` | `COUNT(discount_pct)` |
| Trouver les valeurs manquantes | `values.isna()` | `discount_pct IS NULL` |
| Moyenne des valeurs connues | `values.mean()` | `AVG(discount_pct)` |

La requête « aller plus loin » compte les commandes par client avec
`COUNT(o.id)`. Pour un client sans commande, `COUNT(*)` compterait quand
même sa ligne produite par `LEFT JOIN`.

## 5. Modifier puis vérifier l'enregistrement

Dans ce scénario, une vérification des fiches fournit quatre corrections :
le client `003` habite Lyon ; la quantité de la commande `002` est 3 ;
la remise de la commande `004` est 5 % ; la commande `012` doit être supprimée.
La remise renseignée est une information vérifiée du scénario, pas une
valeur inventée pour combler le manque.

**Avant `05` :** prédisez les lignes concernées. Repérez chaque `WHERE`.
Que ferait la même instruction sans ce filtre ? Le script montre les
valeurs avant et après, enregistre, ferme puis rouvre la base.
Relancez `04` pour observer les nouvelles données.

## Repères pour vérifier vos résultats

Consultez ces repères après vos prédictions, sur les données initiales.

- Deux CSV de 12 lignes ; 12 clients et 12 commandes importés.
- `info()` : 10 âges et 8 remises connus ; respectivement 2 et 4 manques.
- `describe()` : `count` vaut 10 pour les âges, 12 pour les quantités et 8 pour
  les remises. La moyenne des remises connues vaut 5 %.
- Cinq premières remises : 2 connues, 3 manquantes, moyenne 5 %.
- Filtre Lyon et âge ≥ 35 : Hugo (63), Emma (52), Bilal (47).
- `JOIN` : 12 lignes. `LEFT JOIN` : 14 lignes, dont les clients `011` et
  `012` sans commande. Plusieurs lignes pour un client peuvent être normales.
- Après `05` : 11 commandes, 8 remises connues, 3 manquantes,
  moyenne 5,625 %. Les corrections restent présentes après réouverture.

**À modifier puis expliquer :** dans `orders.csv`, remplacez le
`unknown` de la commande `005` par `0`. Relancez `02`, puis `03`
et `04`. Le nombre de remises connues augmente-t-il ? Le nombre de
commandes change-t-il ? Rétablissez les CSV avec `01`, puis la base avec
`03`.

Repères officiels : [lecture CSV avec pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html),
[Python et SQLite](https://docs.python.org/3/library/sqlite3.html),
[comptages et moyennes SQLite](https://www.sqlite.org/lang_aggfunc.html).
