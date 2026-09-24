# Python : comprendre, vérifier, comparer

Ce dossier accompagne la séance du 24 septembre 2026. Le travail consiste à
expliquer un résultat, diagnostiquer un défaut et apporter une preuve de
correction avant de comparer les performances.

**Point de départ : ouvrez le dossier `lab` dans VS Code.** Toutes les commandes
ci-dessous partent de ce dossier. Dans les exemples, `python` désigne
l'interpréteur de votre environnement choisi : vérifiez-le avec
`01_environment_check.py`. Les commandes avec un chemin explicite pour Windows
et Linux figurent dans [ENVIRONMENT.md](ENVIRONMENT.md).

Le [livret d'exercices DOCX](../2026-09-24_python_exercices.docx)
réunit les consignes détaillées, les valeurs acceptées et les résultats
attendus, les exemples de code et le texte à compléter pour rendre votre
travail. Gardez-le ouvert à côté de VS Code.

## Prendre en main le projet

1. [Vérifier l'environnement](ENVIRONMENT.md), puis lancer
   `python 01_environment_check.py`.
2. [Configurer les outils de VS Code](VSCODE.md).
3. Examiner le résultat attendu du rectangle, lancer le script et ses tests, puis
   diagnostiquer le défaut avec le débogueur.
4. Lire la configuration avec `python 02_config_demo.py` après avoir préparé
   `.env` selon le guide d'environnement.
5. Ouvrir [le notebook d'exploration](notebooks/01_Environment_and_contracts_FR.ipynb)
   si vous souhaitez inspecter les mêmes notions dans des cellules.

```text
python guided/run_rectangle.py
python -m unittest discover -s guided/tests -v
```

Le rectangle contient **un défaut volontaire** : son résultat ne respecte pas
le nombre attendu. Les tests initiaux doivent signaler ce défaut. Un échec
d'import ou un interpréteur introuvable constitue un autre problème : revenez
alors au guide d'environnement. Ne modifiez pas le résultat attendu d'un test
pour faire disparaître un désaccord avec le résultat attendu.

La fiche [PYTHONPATH dans .env](PYTHONPATH.md) montre pourquoi un lancement
direct et une découverte de tests peuvent trouver des modules différents.
Elle explique les réglages à essayer, puis leur vérification dans un nouveau
terminal. Le kit conserve son réglage initial ; suivez la fiche pour le modifier.

## Activités du cours

La fiche [Demandes, préférences et contexte de l’IA](AI_PRACTICE.md) propose
trois activités avec des exemples et des réponses fictives. Conservez votre
travail dans `AI_NOTES.md`. Aucun compte IA n’est nécessaire.

Avant les mesures de performance, les [exemples progressifs](performance/README.md)
montrent quatre durées dans un tableau NumPy, leur traitement par deux lots,
puis deux tâches exécutées en séquentiel et avec des processus. Les fonctions
sont définies avant leur appel. Ces exemples expliquent le mécanisme sans
chronométrer le calcul.

## Travail autonome

Commencez par le socle commun, puis choisissez un approfondissement adapté à
ce que vous souhaitez consolider. Rendez les preuves décrites dans
[SUBMISSION.md](SUBMISSION.md).

### Socle commun — Fonction, résultat et contrôle

Dans `exercises/duration_tools.py`, inspectez `minutes_to_hours`, puis corrigez
le défaut de retour observé. La fonction doit renvoyer une valeur de type `float`
pour une durée réelle, finie et positive ou nulle. Conservez les trois cas du
contrôle manuel : 0, 60 et 90 minutes doivent produire respectivement 0.0,
1.0 et 1.5 heure. Expliquez la différence entre le calcul renvoyé par la
fonction et son affichage par l'appelant. Ajoutez un quatrième cas valide,
choisi et justifié, sans retirer les trois contrôles fournis.

```text
python exercises/check_manual.py
```

Ce premier jalon vérifie seulement ces trois valeurs numériques et leur type
de sortie. Il ne prouve pas que toutes les entrées sont traitées correctement. Les règles
du module restent les suivantes : booléens et autres types non numériques
doivent être refusés par `TypeError` ; valeurs négatives ou non finies par
`ValueError`. Leur traitement et leurs tests sont approfondis dans la piste A.
Vous pouvez passer à la piste choisie après les trois contrôles et l'explication
du correctif, en indiquant cette limite de la preuve.

### A — Valeurs acceptées, erreurs prévues et tests

Complétez la validation des entrées de `minutes_to_hours`, puis les tests de
`exercises/tests/test_duration.py`. Conservez la fonction dans son module ;
les tests l'importent. Vérifiez les valeurs usuelles, zéro, une durée
fractionnaire et les entrées invalides selon les règles ci-dessus.

```text
python -m unittest discover -s exercises/tests -v
```

Complétez les tests à écrire. Les marqueurs `TODO` dans les tests provoquent
volontairement un échec tant que le travail n'est pas réalisé. Expliquez ce
qu'apporte chaque cas, puis relancez la commande dans un nouveau processus.

### B — Même calcul, plusieurs exécutions

Lisez `performance/compare_execution.py`, prévoyez les résultats, puis comparez
la boucle Python, NumPy et les threads. NumPy est nécessaire pour cette piste.

```text
python performance/compare_execution.py --size 100000 --workers 2 --repeats 3 --seed 404
```

Vérifiez d'abord l'accord numérique. Faites varier une seule option à la fois,
conservez les mesures et expliquez les coûts inclus dans la mesure. Un gain
observé sur votre machine n'est pas une promesse pour toute taille ou tout
matériel.

### C — Tâches indépendantes et processus

Examinez le partage des rôles entre `process_tasks.py` et `run_processes.py`.
Cette piste utilise la bibliothèque standard et se lance comme un script.

```text
python performance/run_processes.py --tasks 4 --samples 20000 --workers 2 --repeats 3 --seed 404
```

Repérez le point d'entrée protégé, les arguments transmis au worker et la
répartition des seeds. Comparez les résultats séquentiels et parallèles avant
les durées. Essayez une autre taille de tâche et expliquez si le coût de
démarrage des processus est amorti. N'exécutez pas ce script en le copiant dans
une cellule de notebook.

### Référence facultative — Fonctions et gaussiennes

Après le socle et l'approfondissement choisi,
[le notebook de continuité](notebooks/02_Gaussian_functions_FR.ipynb) reprend
les premières étapes du travail sur les fonctions et les gaussiennes du
22 septembre. Il ne constitue pas une quatrième piste obligatoire. Ses
dépendances supplémentaires sont réunies dans `requirements-gaussian.txt` :
installez-les avec le Python du projet, puis sélectionnez ce même noyau Python.

```text
python -m pip install -r requirements-gaussian.txt
```

## Exemples repris du 22 septembre

Le [dossier continuation_22](continuation_22/README.md) fournit les cinq notebooks
cités dans le cours unifié : comparaison C++/Python, CPU/GPU, atelier gaussien
complet, CSV/types/valeurs manquantes et anciennes pistes d’exercices.
Le notebook gaussien complet poursuit jusqu’à la classe, aux graphiques et à
votre module personnel ; il est distinct du petit notebook de fonctions ci-dessus.

Pour ces cinq notebooks, préparer aussi leurs dépendances, dont Plotly et
Matplotlib, avec le Python du projet :

```text
python -m pip install -r continuation_22/requirements.txt
```

Le notebook `05` contient les anciens choix du 22. Pour le travail du 24,
le livret DOCX reste la référence : exercice commun, puis A, B ou C.

## Ressources

- [Utiliser et évaluer une aide IA](AI_HELP.md) : l'activité reste réalisable
  sans compte IA, avec les réponses fictives fournies.
- [Découvrir R ultérieurement](R_NEXT.md) : installation séparée, hors du
  parcours de cette séance.
- [Préparer le retour de travail](SUBMISSION.md).

Les exercices de fonctions, de tests et de processus utilisent seulement Python.
La lecture de `.env` requiert `python-dotenv`, la comparaison NumPy requiert
`numpy`, et le notebook requiert un kernel Python avec `ipykernel`.
Après préparation des outils et des packages, ces activités s'exécutent
localement sans connexion à un service cloud. Aucun compte Google, GitHub ou IA
n'est requis pour effectuer les exercices.
