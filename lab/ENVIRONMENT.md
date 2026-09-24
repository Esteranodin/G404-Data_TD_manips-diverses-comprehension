# Environnement Python et configuration

Toutes les commandes de ce guide sont exécutées depuis le dossier `lab`,
contenant ce fichier. Ouvrez ce dossier avec **Fichier → Ouvrir le dossier** dans
VS Code. Conservez un environnement déjà préparé s'il convient au projet ; ne
recréez pas sa `.venv` et n'installez pas les packages dans le Python système.

## Quatre éléments à distinguer

| Élément | Rôle | Vérification |
| --- | --- | --- |
| Python | Exécuter le code | `sys.version`, `sys.executable` |
| `.venv/` | Réunir un interpréteur et les packages du projet | `sys.prefix != sys.base_prefix` |
| `.env` | Fichier texte de paramètres `clé=valeur` | Lecture explicite par le programme |
| VS Code / kernel | Choisir quel Python lancer | Interpréteur du script et kernel du notebook |

Le nom `.venv` est une convention de dossier ; `.env` est ici un fichier. Une
extension VS Code n'est ni l'interpréteur Python, ni un package installé par pip.

## Réutiliser un environnement existant

Dans VS Code, lancez **Python: Select Interpreter** et choisissez le Python
préparé. Ouvrez un nouveau terminal. Lancez :

```text
python 01_environment_check.py
python -m pip --version
```

Vérifiez le chemin affiché, la version, le dossier courant et les packages
disponibles. Un package installé avec un autre Python ne sera pas forcément
accessible ici. Si `python` ne désigne pas l'interpréteur choisi, utilisez son
chemin complet comme dans les exemples suivants. Le script de diagnostic ne
modifie rien et peut terminer normalement avec des packages optionnels absents.

## Préparer un environnement si aucun n'existe

Utilisez un Python récent compatible avec les packages du projet. La
vérification locale utilise Python 3.13.5 sur Linux. Python 3.11 et 3.12 sont
des versions attendues compatibles, mais n'ont pas été testées ici ; exécutez
les mêmes contrôles si vous les utilisez. Les intervalles de versions de
`requirements.txt` ne constituent pas un verrouillage complet des dépendances.

### Windows — PowerShell

```powershell
py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\python.exe 01_environment_check.py
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
```

Si le lanceur `py` est absent, utilisez le chemin du Python installé. Si la
machine n'a pas Python, faites préparer son installation avant de continuer.

### Linux — Bash

```bash
python3 --version
python3 -m venv .venv
./.venv/bin/python 01_environment_check.py
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -m pip check
```

Si le module `venv` manque, sa préparation dépend de la distribution Linux.
Faites corriger cette dépendance système avant de relancer la création.

### Activation facultative

L'activation rend le nom `python` pratique dans **ce terminal**. Elle n'est pas
nécessaire avec un chemin explicite.

```powershell
.\.venv\Scripts\Activate.ps1
python 01_environment_check.py
```

```bash
source .venv/bin/activate
python 01_environment_check.py
```

Si PowerShell bloque le script d'activation, continuez avec
`.\.venv\Scripts\python.exe`. Il n'est pas nécessaire de changer la politique
d'exécution de la machine. Pour un environnement placé ailleurs, remplacez le
chemin ; en PowerShell, un chemin entre guillemets se lance avec
`& "C:\chemin\vers\python.exe" 01_environment_check.py`.

Dans les autres fiches, remplacez `python` par cet interpréteur si nécessaire :

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s guided/tests -v
```

```bash
./.venv/bin/python -m unittest discover -s guided/tests -v
```

## Choisir aussi le kernel du notebook

Ouvrez `notebooks/01_Environment_and_contracts_FR.ipynb`, puis **Select Kernel**
en haut du notebook et choisissez l'environnement du projet. Vérifiez
`sys.executable` dans une cellule : le choix de l'interpréteur des scripts ne
suffit pas à prouver celui du kernel. Après une modification des modules,
redémarrez le kernel et exécutez les cellules dans l'ordre. Cela évite de
confondre un état gardé en mémoire avec le code enregistré sur disque.

## Lire `.env` explicitement

Copiez le modèle s'il n'existe pas encore de `.env` :

```powershell
Copy-Item .env.example .env
```

```bash
cp .env.example .env
```

Puis lancez `python 02_config_demo.py`. Le programme lit exactement le fichier
`.env` situé à côté du script, avec `dotenv_values(..., interpolate=False)`.
Il obtient un dictionnaire sans modifier `os.environ`. Il ne charge pas
automatiquement des fichiers situés dans d'autres dossiers.

| Paramètre | Type lu | Contrat après conversion |
| --- | --- | --- |
| `COURSE_LABEL` | `str` | Texte non vide, une ligne, 60 caractères maximum |
| `N_VALUES` | `str` | Entier de 1 à 1 000 000 |
| `N_WORKERS` | `str` | Entier de 1 à 4 |

Essayez `N_VALUES=abc`, puis `N_WORKERS=0` ; lisez chaque erreur et rétablissez
une valeur valide. Une valeur textuelle comme `"2"` doit être convertie avant
d'être utilisée comme entier. Ce fichier ne règle que la démonstration de
configuration ; les scripts de performance utilisent leurs options de ligne
de commande.

Créer `.env` ne suffit pas à le charger. Le chargement dépend du programme ou
de l'outil de lancement ; la configuration VS Code de ce kit désactive son
injection automatique dans les terminaux. `.env.example` contient seulement
des paramètres de démonstration. Ne placez aucune clé de service ni aucun mot
de passe dans le travail à remettre.

## Vérifier dans un nouveau processus

Enregistrez les fichiers, puis relancez les scripts depuis le terminal.
Chaque commande `python ...` démarre un nouveau processus. Le rectangle et
les exercices à compléter doivent échouer au départ pour les raisons indiquées
dans [README.md](README.md), et non à cause d'un mauvais chemin ou d'un import
introuvable.

Sources : [environnements VS Code](https://code.visualstudio.com/docs/python/environments),
[paramètres Python VS Code](https://code.visualstudio.com/docs/python/settings-reference),
[python-dotenv](https://bbc2.github.io/python-dotenv/).
