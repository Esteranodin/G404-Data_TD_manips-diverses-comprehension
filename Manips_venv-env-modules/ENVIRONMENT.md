# Environnement Python et configuration

Toutes les commandes de ce guide s'exécutent depuis le dossier `lab`. Ouvrez ce dossier dans VS Code avec **Fichier → Ouvrir le dossier**.

Si un environnement est déjà prêt et convient au projet, gardez-le. Ne recréez pas son `.venv`. N'installez pas les packages dans le Python système.

## Quatre éléments à distinguer

Ces quatre éléments sont différents. Ne les confondez pas.

| Élément | Rôle | Vérification |
| --- | --- | --- |
| Python | Exécuter le code | `sys.version`, `sys.executable` |
| `.venv/` | Réunir un interpréteur et les packages du projet | `sys.prefix != sys.base_prefix` |
| `.env` | Fichier texte de paramètres `clé=valeur` | Lecture explicite par le programme |
| VS Code / kernel | Choisir quel Python lancer | Interpréteur du script et kernel du notebook |

`.venv` est un nom de dossier, par convention. `.env` est un fichier, ici.

Une extension VS Code n'est pas un interpréteur Python. Ce n'est pas non plus un package installé par pip.

## Réutiliser un environnement existant

Dans VS Code, lancez **Python: Select Interpreter**. Choisissez le Python déjà préparé. Ouvrez un nouveau terminal. Lancez :

```text
python 01_environment_check.py
python -m pip --version
```

Vérifiez le chemin affiché, la version, le dossier courant et les packages disponibles.

Un package installé avec un autre Python peut être invisible ici. Si `python` ne lance pas l'interpréteur choisi, utilisez son chemin complet, comme dans les exemples suivants.

Le script de diagnostic ne modifie rien. Il peut se terminer normalement même si des packages optionnels manquent.

## Préparer un environnement si aucun n'existe

Utilisez un Python récent, compatible avec les packages du projet.

La vérification locale utilise Python 3.13.5 sur Linux. Python 3.11 et 3.12 devraient aussi convenir, mais ils n'ont pas été testés ici : relancez les mêmes vérifications si vous les utilisez.

Les versions indiquées dans `requirements.txt` ne garantissent pas des dépendances identiques sur toutes les machines.

### Windows — PowerShell

```powershell
py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\python.exe 01_environment_check.py
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
```

Si `py` n'existe pas sur la machine, utilisez le chemin complet de votre Python.

Si aucun Python n'est installé, installez-le avant de continuer.

### Linux — Bash

```bash
python3 --version
python3 -m venv .venv
./.venv/bin/python 01_environment_check.py
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -m pip check
```

Si le module `venv` manque, son installation dépend de la distribution Linux. Corrigez cela avant de recréer l'environnement.

### Activation facultative

L'activation rend la commande `python` pratique dans **ce terminal**. Elle n'est pas obligatoire si vous utilisez un chemin complet.

```powershell
.\.venv\Scripts\Activate.ps1
python 01_environment_check.py
```

```bash
source .venv/bin/activate
python 01_environment_check.py
```

Si PowerShell bloque le script d'activation, utilisez `.\.venv\Scripts\python.exe` à la place. Vous n'avez pas besoin de changer la politique d'exécution de la machine.

Pour un environnement situé ailleurs, adaptez le chemin. En PowerShell, un chemin entre guillemets se lance avec `& "C:\chemin\vers\python.exe" 01_environment_check.py`.

Dans les autres fiches, remplacez `python` par cet interpréteur si besoin :

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s guided/tests -v
```

```bash
./.venv/bin/python -m unittest discover -s guided/tests -v
```

## Choisir aussi le kernel du notebook

Ouvrez `notebooks/01_Environment_and_contracts_FR.ipynb`. Cliquez sur **Select Kernel**, en haut du notebook. Choisissez l'environnement du projet.

Vérifiez ensuite `sys.executable` dans une cellule : choisir le bon interpréteur pour les scripts ne garantit pas le bon kernel pour le notebook.

Après avoir modifié un module, redémarrez le kernel et relancez les cellules dans l'ordre. Cela évite de confondre un ancien résultat, gardé en mémoire, avec le code enregistré sur le disque.

## Lire `.env` explicitement

Si `.env` n'existe pas encore, copiez le modèle :

```powershell
Copy-Item .env.example .env
```

```bash
cp .env.example .env
```

Puis lancez `python 02_config_demo.py`. Le programme lit le fichier `.env` situé à côté du script.

Il utilise `dotenv_values(..., interpolate=False)`. Il obtient un dictionnaire, sans modifier `os.environ`. Il ne charge pas automatiquement un fichier situé dans un autre dossier.

| Paramètre | Type lu | Contrat après conversion |
| --- | --- | --- |
| `COURSE_LABEL` | `str` | Texte non vide, une ligne, 60 caractères maximum |
| `N_VALUES` | `str` | Entier de 1 à 1 000 000 |
| `N_WORKERS` | `str` | Entier de 1 à 4 |

Essayez `N_VALUES=abc`, puis `N_WORKERS=0`. Lisez chaque erreur, puis remettez une valeur valide.

Une valeur textuelle comme `"2"` doit être convertie en entier avant d'être utilisée.

Ce fichier sert seulement à la démonstration de configuration. Les scripts de performance utilisent leurs propres options de ligne de commande.

Créer `.env` ne suffit pas à le charger. Le chargement dépend du programme ou de l'outil utilisé pour le lancer. Dans ce kit, la configuration VS Code désactive le chargement automatique dans les terminaux.

`.env.example` contient seulement des valeurs de démonstration. Ne mettez aucune clé de service ni aucun mot de passe dans le travail à rendre.



Sources : [environnements VS Code](https://code.visualstudio.com/docs/python/environments), [paramètres Python VS Code](https://code.visualstudio.com/docs/python/settings-reference), [python-dotenv](https://bbc2.github.io/python-dotenv/).