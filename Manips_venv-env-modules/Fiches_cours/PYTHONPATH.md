# Aider Python à trouver les modules du projet

`PYTHONPATH` indique à Python des dossiers supplémentaires où chercher les modules importés. Il ne choisit pas l'interpréteur. Il n'installe aucun paquet. Dans cet exemple, il indique le dossier `lab`, qui contient le paquet `guided`.

Ouvrez **le dossier `lab`** dans VS Code et choisissez le Python du cours. Toutes les commandes ci-dessous partent de ce dossier. Si `python` ne lance pas cet interpréteur, utilisez son chemin complet, comme expliqué dans [ENVIRONMENT.md](ENVIRONMENT.md).

## 1. Observer un échec d'import

Lancez le fichier de test directement :

```text
python guided/tests/test_rectangle.py
```

Si rien n'a encore ajouté `lab` aux dossiers de recherche, Python signale `ModuleNotFoundError: No module named 'guided'`. Le fichier de test est dans `guided/tests/`. En le lançant ainsi, c'est ce dossier qui est ajouté au début de la liste de recherche, pas `lab`. Le code des tests n'a pas encore été exécuté.

La commande recommandée dans le kit reste :

```text
python -m unittest discover -s guided/tests -v
```

Lancée depuis `lab`, elle permet l'import sans ajouter `PYTHONPATH`. L'exécution directe du fichier sert seulement à comprendre pourquoi la façon de lancer Python change les dossiers où il cherche les modules. [Explication officielle de `sys.path`](https://docs.python.org/3/library/sys_path_init.html).

## 2. Inscrire le chemin de `lab` dans `.env`

Repérez le chemin complet du dossier actuel : `pwd` dans Bash sous Linux, ou `(Get-Location).Path` dans PowerShell sous Windows.

Dans le fichier `.env` du dossier `lab`, ajoutez **une seule ligne `PYTHONPATH`**, ou modifiez-la si elle existe déjà. Gardez les autres paramètres. Remplacez le chemin d'exemple par celui de votre propre dossier.

Exemple Linux :

```dotenv
PYTHONPATH=/home/votre_nom/cours/2026-09-24/lab
```

Exemple Windows — les barres `/` sont utilisables dans ce chemin :

```dotenv
PYTHONPATH=C:/Users/VotreNom/cours/2026-09-24/lab
```

Le chemin doit désigner **`lab`**, pas `guided`, `guided/tests` ou `.venv`. Ce sont des exemples à remplacer : ils ne correspondent pas à votre ordinateur. Cette étape utilise seulement un chemin de dossier, sans identifiant ni mot de passe.

## 3. Faire lire `.env` au nouveau terminal de VS Code

Le kit contient actuellement `"python.terminal.useEnvFile": false` dans `.vscode/settings.json`. Pour essayer ce chargement, passez cette valeur à `true` et ajoutez le réglage `python.envFile` dans le même objet JSON. Gardez les autres réglages. Ne créez pas une deuxième propriété portant le même nom.

```json
{
  "python.envFile": "${workspaceFolder}/.env",
  "python.terminal.useEnvFile": true
}
```

Ici, `${workspaceFolder}` désigne le dossier `lab` ouvert dans VS Code. Enregistrez `.env` et `settings.json`. Fermez l'ancien terminal, puis ouvrez **un nouveau terminal intégré**. VS Code transmet les variables à la création du terminal : un terminal déjà ouvert garde son ancien environnement. [Documentation VS Code](https://code.visualstudio.com/docs/python/environments#_env-file-support).

## 4. Vérifier ce que reçoit Python

Dans le nouveau terminal, affichez le Python choisi, la variable qui nous intéresse, et les dossiers de recherche :

```text
python -c "import os, sys; print(sys.executable); print(os.getenv('PYTHONPATH')); print(*sys.path, sep='\n')"
```

Le premier chemin doit être celui du Python du cours. La deuxième ligne doit contenir le chemin de `lab`. Vous devez aussi le retrouver dans `sys.path`. `None` signifie que la variable n'a pas été transmise à Python.

Vérifiez ensuite quel fichier est importé :

```text
python -c "import guided.rectangle_tools as module; print(module.__file__)"
```

Le résultat doit désigner `lab/guided/rectangle_tools.py`. Attention : avec `python -c`, le dossier courant est aussi accessible. Ce contrôle ne suffit donc pas à vérifier le lancement direct du fichier de test. **Relancez exactement la première commande :**

```text
python guided/tests/test_rectangle.py
```

Cette fois, les tests doivent démarrer. Le message final annonce encore des échecs et des erreurs : c'est attendu, car `Rectangle.area()` renvoie volontairement du texte au lieu d'un nombre. L'import fonctionne désormais ; il reste à corriger la fonction. Les messages `FAIL`, `ERROR` et le nombre de tests exécutés permettent de distinguer les deux problèmes.

## 5. Comprendre ce qui ne change pas automatiquement

Python construit `sys.path` au démarrage. La variable doit donc lui être transmise **avant** le lancement. Modifier `.env` pendant qu'un programme ou un noyau de notebook tourne ne reconstruit pas sa liste de recherche.

Le script `02_config_demo.py` utilise `dotenv_values(...)` pour obtenir un dictionnaire. Cette lecture ne modifie ni les variables de son processus (`os.environ`), ni `sys.path`. Ajouter `PYTHONPATH` au fichier qu'il lit ne suffit donc pas à changer les imports.

`python.analysis.extraPaths` aide Pylance à trouver les imports pendant l'analyse dans l'éditeur. Ce réglage ne change pas les dossiers où le Python exécuté cherche ses modules. [Paramètres Pylance](https://code.visualstudio.com/docs/python/settings-reference#_pylance-language-server).

Un notebook ou une tâche personnalisée de VS Code peut être lancé par un chemin différent de ce nouveau terminal. Vérifiez son propre `sys.executable`, sa variable `PYTHONPATH` et son `sys.path`. Pour une tâche personnalisée, la variable peut être définie dans son bloc `options.env`. Le seul réglage du terminal ne garantit pas qu'elle sera transmise à la tâche.

Gardez cet essai dans le projet. Il n'est pas nécessaire de modifier les variables globales de Windows, le profil Bash, ou le Python installé sur la machine.