## Choisir le fichier utile

| Fichier | Ce que vous allez faire |
|---|---|
| [01_Benchmark_Cpp_Python_FR.ipynb](01_Benchmark_Cpp_Python_FR.ipynb) | Convertir les mêmes minutes en heures avec C++, une boucle Python, NumPy et deux écritures pandas. Vérifier les résultats avant de comparer les durées. |
| [01_Benchmark_Cpp_Python_FR.py](01_Benchmark_Cpp_Python_FR.py) | Exécuter la même comparaison depuis un terminal. |
| [02_Parallelisme_CPU_GPU_FR.ipynb](02_Parallelisme_CPU_GPU_FR.ipynb) | Comparer un calcul NumPy et plusieurs threads CPU ; explorer le GPU seulement s'il est disponible. |
| [03_Architecture_Gaussian_mixture_FR.ipynb](03_Architecture_Gaussian_mixture_FR.ipynb) | Simuler deux groupes, écrire deux fonctions, construire la classe `GaussianMixture`, puis déplacer les définitions dans votre module. |
| [04_CSV_types_missing_values_FR.ipynb](04_CSV_types_missing_values_FR.ipynb) | Lire un petit CSV, choisir les types, repérer les valeurs manquantes et comparer plusieurs usages de `lambda`. |
| [05_Afternoon_exercises_FR.ipynb](05_Afternoon_exercises_FR.ipynb) | Reprendre, si vous le souhaitez, l'un des quatre exercices du 22 septembre. |

Les numéros `01` à `05` sont ceux des fichiers conservés. Ce ne sont pas des
numéros de diapositives dans le cours du 24 septembre.

## Préparer Python

Réutilisez l'environnement du cours s'il dispose déjà des bibliothèques
nécessaires. La [fiche d'environnement](../ENVIRONMENT.md) explique comment
choisir le bon Python dans le terminal et dans un notebook. Le fichier
[requirements.txt](requirements.txt) indique les versions utilisées pour
vérifier ces exemples, dont Plotly pour les graphiques du mélange gaussien et
Matplotlib pour les comparaisons de durées.

Depuis le dossier `lab/`, avec le Python choisi pour le cours :

```text
python -m pip install -r continuation_22/requirements.txt
```

Installer ces bibliothèques demande une connexion. Une fois l'environnement
préparé, les notebooks fonctionnent localement sur CPU, sans compte en ligne.
Ils contiennent leurs données : aucun CSV externe n'est à télécharger.

La comparaison C++ est facultative. Sans compilateur déjà disponible, le
notebook `01` poursuit avec les quatre méthodes Python. Le notebook `02`
poursuit sur CPU si PyTorch ou un GPU CUDA est absent. Le fichier de
dépendances n'installe ni compilateur C++, ni PyTorch, ni pilote GPU.

## Exécuter un notebook

Ouvrez le fichier choisi dans VS Code ou Jupyter et sélectionnez le noyau
Python du cours. Un noyau est le programme qui exécute les cellules et garde
leurs variables en mémoire. Pour vérifier votre choix, vous pouvez exécuter :

```python
import sys
from pathlib import Path

print(sys.executable)
print(Path.cwd())
```

Pour les notebooks `03` et `05`, le dossier de travail affiché doit être
`continuation_22/`, où vous placerez vos modules personnels. Si VS Code
démarre les notebooks dans un autre dossier, ouvrez directement
`continuation_22/` comme dossier de travail dans l'éditeur, puis vérifiez à
nouveau `Path.cwd()`.

Lisez la consigne avant le code. Exécutez les cellules dans l'ordre, sauf
indication précise du notebook. Après avoir modifié les paramètres d'une
comparaison, reprenez depuis la cellule des paramètres pour recréer les
données. Pour lancer la version script du benchmark depuis `lab/` :

```text
python continuation_22/01_Benchmark_Cpp_Python_FR.py
```

## Compléter le mélange gaussien

Le notebook `03` contient des lignes `TODO` : elles indiquent du code à écrire.
Un message « à compléter » est donc attendu au départ. Une exécution sans
erreur ne signifie pas que le travail est terminé.

Complétez les deux fonctions, puis la classe dans l'ordre proposé. Les
vérifications portent notamment sur les 2 000 lignes, les 1 200 étiquettes A
et les 800 étiquettes B. Les graphiques viennent après ces contrôles.

Créez vous-même `my_gaussian_mixture.py` **à côté du notebook**, dans
`continuation_22/`. Copiez-y vos imports, vos deux fonctions et votre classe,
sans les données d'essai ni les appels d'affichage. Aucun module terminé
n'est fourni. Le notebook ne crée pas ce fichier à votre place.

Enregistrez le module, redémarrez le noyau, puis suivez la vérification
d'import. Le chemin `gm.__file__` doit désigner votre fichier et
`module_build_ok` doit valoir `True`. Expliquez aussi ce que les contrôles
vérifient : leur réussite ne garantit pas tous les comportements possibles.

## Lire les mesures avec leurs limites

Les durées dépendent de votre ordinateur, des versions et des autres
programmes en cours. Les résultats historiques du cours ne sont pas des
temps à reproduire exactement.

Le notebook `02` crée son groupe de threads **avant** les mesures. Le script
du 24 septembre `../performance/compare_execution.py` inclut sa création et
sa fermeture dans la durée. Avant de rapprocher deux nombres, vérifiez que
les chronomètres couvrent le même travail. Un ralentissement reste un résultat
à expliquer.

Le notebook `04` a été vérifié avec pandas 3. Certains noms de types et
affichages de valeurs manquantes diffèrent avec pandas 2. Comparez toujours
les valeurs et leurs types ; l'affichage seul ne suffit pas.
