# Consignes

**Le rendu de l'exo** est le dossier [gaussian-mixture-project](./gaussian-mixture-project/)

## Les six exigences

#### 1. Simuler deux groupes.
A : moyenne 100, écart-type 18, proportion 60 %.
B : moyenne 106, écart-type 24, proportion 40 %.
Produire 2 000 observations avec la graine aléatoire (`seed`) 404.

Ces paramètres sont modifiables dans le script de lancement.

#### 2. Produire un dataframe.
Une observation par ligne, une colonne numérique `value` et une colonne `component` indiquant A ou B.  
Le cas initial contient 1 200 A et 800 B.  
Chaque observation vient d'un groupe ; les tirages ne s'additionnent pas.

#### 3. Utiliser une classe.
Chaque objet garde ses paramètres et son dernier dataframe.  
Ses méthodes produisent et renvoient ce dataframe, puis préparent et renvoient les figures.  
Des fonctions séparées tirent les valeurs et les assemblent dans le dataframe ; le module de la classe les importe et ses méthodes les utilisent.

#### 4. Reprendre l'organisation de Rectangle.
Un paquet local est un dossier contenant `__init__.py`.  
Ce fichier définit une constante pour la graine par défaut, utilisée par la classe et le lanceur.  
Placez la classe et les fonctions dans deux modules distincts de ce paquet.  
À l'intérieur du paquet, utilisez des imports relatifs, qui désignent les modules du même paquet.

Un script de lancement importe la classe, choisit les paramètres, crée les objets, lance le calcul et affiche les résultats.  
Les fichiers du dossier `tests/` importent cette même classe.  
Importer le paquet et ses modules ne lance aucune simulation ni aucun affichage.  
Les noms des fichiers, fonctions et classes sont libres.

#### 5. Produire trois graphiques du premier objet depuis le même dataframe.
Deux histogrammes superposés pour comparer A et B, un histogramme du mélange sans distinguer les groupes, puis des boîtes à moustaches pour A, B et leur mélange (A∪B : toutes les observations), afin de comparer médianes et dispersion. Les histogrammes représentent des densités ; les axes et les groupes sont nommés.

#### 6. Reproduire un résultat et garder deux objets indépendants.
Les mêmes paramètres et la même graine redonnent les mêmes valeurs dans votre environnement.  
Le second objet utilise 30 % de A et un écart-type de 30 pour B, les autres paramètres restant identiques : 600 A et 1 400 B.  
Le premier objet conserve ses propres paramètres et données.  
Des tests vérifient les valeurs et effectifs, la reproductibilité, l'indépendance des objets et la réutilisation du dataframe par les figures.

---

## Exemples à copier et à adapter

Ces trois scripts fonctionnent indépendamment. Utilisez leur code pour
construire votre propre projet Python selon les consignes du diaporama.

Depuis le dossier `lab/`, avec le Python du cours :

```bash
python -m pip install -r requirements.txt
python gaussian/snippets/01_draw_values.py
python gaussian/snippets/02_build_dataframe.py
python gaussian/snippets/03_plot_distributions.py
```

L'installation n'est utile que si les bibliothèques manquent.

| Script | Données utilisées | Résultat |
| --- | --- | --- |
| `01_draw_values.py` | Moyenne 0, écart-type 1, 1 000 valeurs, `seed=404` | Un tableau NumPy, avec un seul appel à `rng.normal` |
| `02_build_dataframe.py` | Liste `[1, 2, 3]` | Un dataframe avec une colonne `value` |
| `03_plot_distributions.py` | Une distribution normale, comme dans `01` | Histogramme, boîte à moustaches et courbe cumulée |

Modifiez les paramètres et adaptez ces opérations aux exigences du projet.

Le troisième script utilise le **même échantillon** pour trois graphiques :

- **Histogramme :** forme de la distribution. L'aire totale des barres vaut 1
  car l'axe vertical représente une densité.
- **Boîte à moustaches :** médiane et dispersion ; la boîte contient les 50 %
  centraux des observations.
- **Courbe cumulée :** pour chaque valeur, proportion des observations
  inférieures ou égales à cette valeur.

La courbe cumulée est un exemple supplémentaire, pas une nouvelle exigence du projet.

exo_projet_gaussian-mixture/
├── README.md
├── gaussian-mixture-project/
│   ├── requirements.txt
│   ├── run.py
│   ├── gaussian/
│   │   ├── __init__.py
│   │   ├── sampling.py
│   │   └── mixture.py
│   └── tests/
│       ├── test_sampling.py
│       └── test_mixture.py
└── snippets/
    └── (les 3 fichiers d'exemple)