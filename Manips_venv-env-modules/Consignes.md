# Python : comprendre, vérifier, comparer

Commencez par corriger une fonction qui convertit des minutes en heures. Choisissez ensuite un exercice A, B ou C pour approfondir les tests ou comparer des façons d'exécuter un calcul. Ce livret accompagne les fichiers du dossier `lab`.

Le code de la fonction contient volontairement une erreur. Votre travail consiste à observer le résultat, expliquer l'erreur, la corriger et vérifier votre correction. Les extraits de code du livret peuvent être sélectionnés et copiés ; les indications autour de chaque extrait précisent comment l'utiliser.

## Ce que vous allez faire

1. Ouvrir le dossier de travail et vérifier le Python utilisé — page 2.
2. Réaliser l'exercice commun : convertir des minutes en heures — page 3.
3. Choisir un exercice A, B ou C — pages 4 à 8.
4. Préparer vos fichiers et expliquer vos résultats — page 10.

| Exercice au choix | Question à examiner | Travail à rendre |
|---|---|---|
| **A · Tester la fonction** | La fonction accepte-t-elle les bonnes valeurs et signale-t-elle les erreurs prévues ? | Fonction corrigée, tests exécutés et explication des cas choisis. |
| **B · Comparer les temps de calcul** | Quelle méthode est la plus rapide pour le calcul et le nombre de valeurs choisis ? | Commandes, temps mesurés et explication des résultats. |
| **C · Répartir les calculs** | Faire plusieurs calculs en parallèle permet-il de gagner du temps ? | Comparaison des résultats et des temps, avec une explication. |

Vous n'avez pas à terminer les trois exercices. A prolonge la correction de votre fonction. Pour B et C, les programmes sont déjà fournis : vous prévoyez un résultat, faites varier un paramètre, puis expliquez ce que vous observez.

### Où trouver les fichiers utiles

| Document ou dossier | Utilité |
|---|---|
| `README.md` | Présentation des fichiers et liens vers les guides. |
| `ENVIRONMENT.md` | Préparation de Python et des bibliothèques nécessaires. |
| `lab/exercises/` | Fonction de conversion et tests à compléter. |
| `lab/performance/` | Programmes des exercices B et C. |
| `SUBMISSION.md` | Liste des éléments à rendre. |

> **Pour suivre les exemples.** Toutes les commandes des pages suivantes se lancent depuis le dossier `lab`. Les chemins de fichiers sont indiqués à partir de ce dossier. Le mot `python` désigne le Python choisi pour ce travail. Les explications sont en français ; les noms de fonctions, de variables et les commentaires de votre code restent en anglais.

---

## 1 · Préparer le dossier de travail

Extrayez les fichiers de l'archive ZIP. Dans VS Code, ouvrez le dossier `lab` lui-même : vous devez y voir `exercises`, `guided` et `performance`. Ouvrez ensuite **Terminal → Nouveau terminal**. Saisissez les commandes dans ce terminal, pas dans un fichier Python ni dans une cellule de notebook.

### Vérifier quel Python exécute votre code

L'interpréteur est le programme qui exécute votre code Python. Réutilisez celui qui a été préparé pour ce travail : ouvrez la palette de commandes de VS Code avec `Ctrl + Maj + P`, puis choisissez **Python: Select Interpreter**. Ouvrez un nouveau terminal et lancez :

```bash
python 01_environment_check.py
python -m pip --version
```

Vérifiez le chemin de Python, sa version et le dossier courant : ce dernier doit être `lab`. Le diagnostic indique aussi les bibliothèques disponibles. Python seul suffit pour l'exercice commun, A et C ; B demande en plus NumPy, une bibliothèque de calcul sur des tableaux de nombres.

### Utiliser directement le bon Python

Le dossier `.venv` réunit le Python du projet et ses bibliothèques. S'il se trouve dans `lab`, les commandes suivantes permettent de l'utiliser directement, sans activer l'environnement dans le terminal.

**Windows · PowerShell**
```powershell
.\.venv\Scripts\python.exe 01_environment_check.py
.\.venv\Scripts\python.exe exercises/check_manual.py
```

**Linux · Bash**
```bash
./.venv/bin/python 01_environment_check.py
./.venv/bin/python exercises/check_manual.py
```

Dans la suite, remplacez au besoin `python` par ce chemin. Si votre environnement se trouve ailleurs, adaptez-le. Si aucun environnement n'est prêt, suivez `ENVIRONMENT.md` pour le créer et installer les bibliothèques nécessaires.

### Distinguer une erreur de l'exercice d'un problème d'installation

```bash
python exercises/check_manual.py
```

Au départ, cette commande doit afficher **À CORRIGER** pour les trois cas, puis signaler un échec : la fonction s'est exécutée, mais elle n'a pas renvoyé le type de résultat attendu. En revanche, une commande introuvable, un fichier absent ou `ModuleNotFoundError` demande de vérifier l'installation ou le chemin utilisé.

> **À ne pas confondre.** `.venv/` est un dossier ; `.env` est un fichier de paramètres. Vous n'avez pas besoin de créer `.env` pour ces exercices. Les programmes B et C utilisent les options écrites dans leurs commandes.

---

## 2 · Convertir des minutes en heures

**Exercice commun.** Ouvrez `exercises/duration_tools.py` et `exercises/check_manual.py`.

Une fonction de calcul doit renvoyer un nombre réutilisable dans un autre calcul. Le programme qui l'appelle peut ensuite ajouter l'unité pour l'afficher. Par exemple, `1.5` est un nombre ; `"1.5 hours"` est du texte, même s'il contient des chiffres.

### Lire le résultat avant de modifier le code

Voici l'extrait à examiner dans `duration_tools.py`. Il contient l'erreur à corriger :

```python
def minutes_to_hours(minutes: float) -> float:
    return f"{minutes / 60:g} hours"
```

`float` est le type Python utilisé ici pour les nombres à virgule ; `str` désigne du texte. Dans le code, écrivez les décimales avec un point : `1.5`. L'indication `-> float` annonce le type attendu sans transformer le résultat. Lancez `python exercises/check_manual.py` et lisez la valeur et le type de chaque résultat.

| Minutes données à la fonction | Heures attendues | Type attendu |
|---|---|---|
| 0 | 0.0 | float |
| 60 | 1.0 | float |
| 90 | 1.5 | float |

### Corriger, puis vérifier le résultat

1. Expliquez le problème avant de modifier le fichier : la fonction renvoie-t-elle le nombre attendu ou un texte qui contient ce nombre ?
2. Corrigez le résultat renvoyé par `minutes_to_hours`. L'affichage avec l'unité reste dans le programme qui l'appelle. Il n'est pas demandé de créer une classe.
3. Enregistrez, puis relancez `python exercises/check_manual.py`. Conservez les trois cas du tableau et leurs résultats attendus.
4. Dans `check_manual.py`, ajoutez un quatrième couple de valeurs à ceux déjà parcourus par la boucle : une durée et son résultat attendu. Choisissez un autre nombre fini, positif ou nul, puis expliquez votre choix. Adaptez le message final au nombre de cas vérifiés.
5. Créez `exercises/check_reuse.py`. Importez la fonction avec `from duration_tools import minutes_to_hours`, appelez-la avec `90`, puis utilisez son résultat dans une addition. Lancez `python exercises/check_reuse.py` et expliquez pourquoi l'addition demande un nombre.

> **À conserver.** Vos fichiers modifiés, les résultats affichés et l'explication du quatrième cas. Montrez la différence entre le nombre renvoyé par la fonction et le texte qui sert à le présenter.

> **Ce qui reste à vérifier.** Ces exemples ne disent pas ce qui arrive avec une valeur interdite. La page 4 précise quelles valeurs accepter ou refuser. Après l'exercice commun, vous pouvez choisir A, B ou C en indiquant les cas que vous n'avez pas encore vérifiés.

---

## 3 · A : quelles valeurs accepter ou refuser ?

**Objectif :** compléter la fonction pour qu'elle accepte les durées prévues et signale clairement les autres valeurs. Modifiez `exercises/duration_tools.py`. Les tests de la page 5 utiliseront cette même fonction.

### Ce que la fonction doit recevoir et renvoyer

Acceptez zéro et les durées positives, entières ou avec une partie décimale. Le résultat doit toujours être de type `float`. Ici, on reste dans les limites des nombres que Python peut représenter par un `float` fini, c'est-à-dire sans infini ni NaN.

NaN désigne une valeur numérique indéfinie. `None` indique une absence de valeur. Les booléens `True` et `False` représentent vrai et faux. Aucune de ces valeurs ne doit être traitée comme une durée dans cet exercice.

| Valeur reçue | Exemples | Résultat ou erreur attendus |
|---|---|---|
| Durée habituelle | `60`, `90` | `1.0`, `1.5`, de type `float`. |
| Zéro | `0` | `0.0`, de type `float`. |
| Fraction de minute | `0.5` | `1/120` heure, de type `float`. |
| Booléen | `True`, `False` | Signaler `TypeError`. |
| Texte, absence de valeur, nombre complexe | `"90"`, `None`, `90 + 0j` | Signaler `TypeError`. |
| Nombre négatif | `-1` | Signaler `ValueError`. |
| Infini ou valeur indéfinie | `float("inf")`, `float("-inf")`, `float("nan")` | Signaler `ValueError`. |

### Signaler la bonne erreur

En Python, on peut signaler une erreur en déclenchant une exception. Ici, `TypeError` indique que le type de la valeur est refusé. `ValueError` indique qu'un nombre a été fourni, mais qu'il n'est pas autorisé. Ces erreurs doivent pouvoir être détectées par les tests ; afficher simplement un message ne suffit pas.

Ne transformez pas `"90"` en nombre : le texte doit être refusé. Ne remplacez pas non plus une valeur interdite par zéro, car zéro est une durée autorisée. La fonction renvoie un nombre ou déclenche l'erreur prévue ; elle n'affiche rien.

### Deux difficultés à examiner

Python permet d'utiliser les booléens dans certains calculs comme des entiers. Une vérification trop large risque donc d'accepter `True`. Vérifiez que votre fonction le refuse. Pour NaN, une comparaison à zéro ne suffit pas : recherchez dans la bibliothèque standard comment vérifier qu'un nombre est fini.

> **Travail demandé.** Complétez la fonction et écrivez les tests correspondant au tableau. Expliquez quelle erreur chaque test permettrait de repérer. Gardez les cas de l'exercice commun ; la page 5 montre comment organiser les tests.

---

## 4 · A : écrire et exécuter les tests

**Fichier :** `exercises/tests/test_duration.py`. L'outil `unittest` est fourni avec Python ; aucune bibliothèque supplémentaire n'est nécessaire pour cet exercice.

Le fichier contient déjà le test ci-dessous. La ligne `from ... import ...` charge la fonction depuis son fichier. Le test vérifie ensuite le type et la valeur qu'elle renvoie.

```python
import unittest
from exercises.duration_tools import minutes_to_hours

class DurationTests(unittest.TestCase):
    def test_ninety_minutes(self):
        result = minutes_to_hours(90)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 1.5)
```

Ne recopiez pas la fonction dans le fichier de tests : les tests doivent utiliser celle que vous avez corrigée. Dans la classe `DurationTests`, les fonctions dont le nom commence par `test_` sont exécutées comme des tests.

### Choisir ce que le test vérifie

| Instruction de vérification | Ce qu'elle vérifie ici |
|---|---|
| `self.assertIsInstance(result, float)` | Le résultat est de type `float`. |
| `self.assertAlmostEqual(result, expected)` | La valeur est assez proche de celle attendue pour accepter un petit écart d'arrondi. |
| `with self.assertRaises(ValueError):` | L'appel qui suit, dans le bloc indenté, déclenche bien `ValueError`. |

L'exemple suivant porte sur un autre calcul : la racine carrée réelle d'un nombre négatif, qui doit être refusée. Enregistrez-le dans `check_square_root.py`, directement dans le dossier `lab`, puis lancez `python check_square_root.py` : un test doit réussir.

```python
import math
import unittest

class SquareRootTests(unittest.TestCase):
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            math.sqrt(-1)

if __name__ == "__main__":
    unittest.main()
```

Dans les tests de conversion, remplacez chaque `self.fail("TODO: ...")` par vos vérifications. Ces lignes signalent un travail à compléter ; les supprimer sans ajouter de test ne vérifie rien. Couvrez les cas de la page 4, puis lancez depuis `lab` :

```bash
python -m unittest discover -s exercises/tests -v
```

> **À conserver.** Les fichiers, la commande, les noms et le nombre de tests exécutés, puis leur résultat. `Ran 0 tests` signifie qu'aucun test n'a été exécuté. `OK` concerne seulement les cas vérifiés : ne changez pas un résultat attendu pour faire accepter une erreur du programme.

---

## 5 · B : comparer les temps de calcul

**Fichier :** `performance/compare_execution.py`. NumPy doit être installé dans le Python choisi, comme indiqué page 2. Le programme convertit en heures un tableau de durées créées pour l'exercice. Il utilise ses propres fonctions : son succès ne vérifie pas votre correction de `minutes_to_hours`.

### Comprendre les trois façons de calculer

La boucle Python traite les valeurs une à une.  
NumPy applique l'opération au tableau avec du code compilé, c'est-à-dire déjà traduit pour être exécuté par la machine.  
Dans la troisième version, plusieurs threads se répartissent le tableau : ce sont des fils d'exécution d'un même programme. Chaque thread écrit dans une partie distincte du tableau de résultats.

Les lignes suivantes sont des extraits à lire dans les fonctions du fichier, pas un programme à exécuter seul :

```python
# Excerpts from compare_execution.py
output[index] = value / 60.0

return values / 60.0

np.divide(values[start:stop], 60.0, out=output[start:stop])
```

Appliquer une opération à tout un tableau s'appelle la **vectorisation**. Cela ne signifie pas que plusieurs cœurs du processeur travaillent. Avec des threads, la répartition du travail prend aussi du temps : ils ne rendent donc pas forcément le calcul plus rapide.

### Faire varier un seul paramètre à la fois

Depuis `lab`, entrez cette commande sur une seule ligne :

```bash
python performance/compare_execution.py --size 100000 --workers 2 --repeats 3 --seed 404
```

Elle traite 100 000 valeurs (`size`), avec 2 threads pour la troisième méthode (`workers`) et 3 mesures par méthode (`repeats`). `seed` règle le générateur aléatoire : garder `404` permet de refaire les mêmes tirages avec les mêmes paramètres et le même environnement.

1. Prévoyez la méthode la plus rapide et expliquez votre choix. Lancez la commande ; vérifiez qu'elle se termine sans erreur de comparaison des résultats.
2. Comparez `--size 10000` et `--size 1000000`, sans changer les autres options. Conservez toutes les durées affichées.
3. À nombre de valeurs fixé, comparez `--workers 1, 2 et 4`. Le nombre de threads est le seul paramètre qui change.

### Comprendre les temps affichés

Les durées sont en millisecondes. Avec trois mesures, la médiane est la valeur du milieu une fois les durées classées. Un premier calcul non chronométré précède les mesures. Le temps comprend le calcul et la création du tableau de résultats ; pour les threads, il comprend aussi leur démarrage et leur arrêt. La création des données et les comparaisons sont hors chronométrage. Les résultats sont vérifiés avant les mesures puis après chaque répétition.

> **À rendre.** Les commandes, les versions de Python et NumPy (`python -m pip show numpy`), les résultats des vérifications, les durées et votre explication. Comparez à votre prévision. Les autres activités de l'ordinateur peuvent influer sur les temps ; votre conclusion vaut pour les conditions testées. Un ralentissement est aussi un résultat à expliquer.

---

## 6 · C : répartir les calculs entre processus

**Fichiers :** `performance/process_tasks.py` et `performance/run_processes.py`.  
Un processus est ici une exécution séparée de Python, avec ses propres variables.  
Le programme principal peut envoyer du travail à plusieurs processus et récupérer leurs résultats.

### Lire ce que reçoit une tâche et ce qu'elle renvoie

Une tâche crée un ensemble de valeurs selon une loi normale, avec une moyenne théorique de 100 et un écart-type de 18. Ce sont des données simulées. Voici les structures qui regroupent les informations dans `process_tasks.py` ; `NamedTuple` permet de nommer chaque information :

```python
from typing import NamedTuple

class SimulationTask(NamedTuple):
    seed: int
    samples: int

class SimulationSummary(NamedTuple):
    seed: int
    samples: int
    sample_mean: float
    fraction_above_130: float
```

`seed` est la valeur de départ du générateur aléatoire ; la conserver permet de refaire les mêmes tirages avec les mêmes paramètres et le même environnement. `samples` est le nombre de valeurs à créer. `simulate_sample(task)` renvoie la moyenne obtenue et la proportion de valeurs supérieures à 130, avec les paramètres utilisés. La moyenne obtenue peut différer de 100. La fonction ne renvoie pas toutes les valeurs créées.

### Lire comment le travail est réparti

Dans `run_processes.py`, `run_parallel` répartit les tâches entre un groupe de processus, appelé *pool* dans le code. Chaque processus appelle `simulate_sample` pour les tâches qu'il reçoit. Cet extrait est à lire dans le fichier fourni, où figurent aussi les imports nécessaires :

```python
def run_parallel(tasks, workers):
    with ProcessPoolExecutor(
        max_workers=workers,
        mp_context=get_context("spawn"),
    ) as pool:
        return list(pool.map(simulate_sample, tasks))
```

`workers` fixe le nombre maximal de processus du groupe. Avec le mode `spawn`, chaque nouveau processus charge les fonctions dont il a besoin depuis leurs fichiers. Gardez donc `simulate_sample` dans `process_tasks.py`.

La condition suivante lance le programme quand ce fichier est exécuté directement. Elle évite de le relancer lorsqu'un autre processus importe le fichier. Conservez ces lignes dans le script fourni :

```python
if __name__ == "__main__":
    freeze_support()
    main()
```

> **À expliquer.** Quelle fonction réalise une tâche ? Quel code répartit les tâches ? Quelles informations sont envoyées, puis renvoyées ? Pour faire les essais de la page suivante, lancez le fichier `.py` depuis le terminal ; ne recopiez pas le programme dans une cellule de notebook.

---

## 7 · C : comparer les résultats et les temps

Quatre tâches restent quatre tâches, qu'on utilise un ou deux processus. On compare d'abord les mêmes calculs faits l'un après l'autre, puis répartis entre plusieurs processus. Vérifiez que les résultats sont identiques avant de comparer les temps.

Depuis `lab`, entrez cette commande sur une seule ligne :

```bash
python performance/run_processes.py --tasks 4 --samples 20000 --workers 2
```

Les options non écrites gardent leurs valeurs par défaut : trois répétitions et une valeur initiale `seed` de 404.

| Paramètre | Ce qu'il règle |
|---|---|
| `--tasks 4` | Quatre simulations, qui peuvent être exécutées séparément. |
| `--samples 20000` | 20 000 valeurs par tâche : 80 000 par exécution des quatre tâches. |
| `--workers 2` | Au plus deux processus dans le groupe de calcul. |
| `--repeats 3` | Trois mesures pour chaque façon d'exécuter les calculs. |
| `--seed 404` | Les quatre tâches partent des valeurs 404, 405, 406 et 407. |

### Faire les comparaisons

1. Prévoyez si répartir les calculs fera gagner assez de temps pour compenser le démarrage des processus. Lancez le script et lisez les résultats avant les durées.
2. Comparez `--workers 1` puis `--workers 2`, sans changer les autres options. Même avec un seul processus dans le groupe, son démarrage prend du temps. Le script mesure aussi le calcul direct dans le programme principal, sans ce groupe.
3. Gardez deux processus et comparez `--samples 20000` puis `--samples 200000`. Ne changez pas le nombre de tâches, les répétitions ni `seed`. Expliquez si des tâches plus longues rendent le démarrage moins important dans le temps total.

### Comprendre ce qui change, et ce qui reste identique

Pour chaque essai, les tâches gardent les mêmes valeurs de départ et le même nombre d'observations dans les deux façons de calculer. Le script compare exactement leurs résumés avant les mesures et après chaque répétition. Des valeurs `seed` différentes distinguent les tirages des tâches ; elles ne suffisent pas à prouver leur indépendance statistique.

Un premier passage non chronométré précède les mesures. Le temps mesuré comprend la création des données simulées et les calculs. Pour les processus, il comprend aussi le démarrage, l'envoi des paramètres, le retour des résumés et l'arrêt. Les valeurs simulées restent dans les processus qui les créent. Un nouveau groupe est créé à chaque répétition. Les comparaisons des résultats sont hors chronométrage.

> **À rendre.** Commandes, version de Python, paramètres, résultats des comparaisons et durées en millisecondes. Conservez aussi la médiane : pour trois mesures classées, c'est celle du milieu. Expliquez un éventuel ralentissement. Changer seulement le nombre de processus ne change ni le nombre de valeurs créées ni la précision statistique des résultats.

---

## 8 · Trouver la cause d'un problème

Avant de modifier plusieurs fichiers, isolez un appel ou une commande qui pose problème. Notez ce que vous attendiez et ce que vous avez obtenu. Cette comparaison permet de chercher une cause précise.

| Ce que vous observez | Ce que vous pouvez vérifier |
|---|---|
| `python` est introuvable ou lance le mauvais Python | Utilisez le chemin du Python choisi et relisez les vérifications de la page 2. |
| Le fichier demandé est introuvable | Vérifiez que les fichiers du ZIP ont été extraits et que le terminal est dans `lab`. |
| `No module named numpy` | Installez NumPy avec le Python utilisé pour l'exercice, selon `ENVIRONMENT.md`. |
| Le résultat est du texte ou « À CORRIGER » apparaît | Comparez le type et la valeur obtenus au tableau de la page 3. |
| Un test affiche `TODO` | Remplacez la partie à compléter par de vraies vérifications. |
| Les tests affichent `Ran 0 tests` | Reprenez la commande de la page 5 ; vérifiez le dossier et les noms commençant par `test_`. |
| Une modification semble sans effet | Enregistrez le fichier, puis relancez la commande depuis le terminal. |
| Les processus échouent dans un notebook | Lancez le script `.py` depuis le terminal et conservez son organisation décrite page 7. |

### Demander une aide qui répond au problème

Préparez cinq éléments : le résultat attendu, le code concerné, la valeur donnée à la fonction, le résultat ou l'erreur obtenus, et ce que vous avez déjà essayé. Demandez une explication et un moyen de la vérifier. Les exemples locaux suffisent ; aucun compte IA n'est obligatoire.

Si vous utilisez une IA, examinez chaque changement proposé. Par exemple, un test qui attend le texte `"1.5 hours"` peut réussir alors que la fonction devrait renvoyer le nombre `1.5`. Le test ne vérifie alors plus la bonne chose. Vérifiez aussi si l'outil a réellement exécuté le code ou s'il propose seulement un test.

Vous pouvez faire cette réflexion sans assistant avec les deux réponses fictives de `AI_HELP.md`, qui portent sur le rectangle. Pour chaque réponse, demandez-vous : la modification répond-elle au besoin ? Quelle exécution permet de le vérifier ?

### Si vous restez bloqué

Conservez la commande qui reproduit l'erreur, sa sortie utile et votre explication possible. Précisez s'il s'agit d'un problème d'installation, de fichier introuvable, de résultat incorrect ou de temps de calcul. Vous pouvez rendre cette description même si la correction n'est pas terminée.

`ENVIRONMENT.md` aide à préparer Python. Pour les notebooks facultatifs, le noyau, ou *kernel*, est le Python qui exécute les cellules : redémarrez-le après avoir modifié un module, puis relancez les cellules dans l'ordre. Ne partagez ni `.env`, ni mots de passe, ni données personnelles pour obtenir de l'aide.

---
