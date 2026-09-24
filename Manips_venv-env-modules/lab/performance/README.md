# Comprendre l’exécution, puis comparer les durées

## Exemples progressifs du cours

Les commandes partent du dossier `lab`, avec le Python du projet.
Commencez par ces deux petits programmes pour retrouver le code du diaporama.
Ils vérifient les résultats sans mesurer de durée.

```text
python performance/vectorization_steps.py
python performance/parallel_steps.py
```

Dans `vectorization_steps.py`, `values` est le tableau NumPy
`[0.0, 60.0, 90.0, 120.0]`, en minutes. Le programme construit le résultat par
une boucle, par une division du tableau, puis en confiant deux lots à un groupe
de deux threads au maximum. Il rassemble les sorties dans l’ordre initial.
Les trois méthodes donnent `[0.0, 1.0, 1.5, 2.0]`, en heures. NumPy est requis.
Les tâches lisent le tableau sans le modifier. Deux lots ne garantissent pas
l’emploi de deux threads différents, ni un calcul plus rapide.

Pour les processus, lisez les fichiers dans cet ordre :

1. `mean_task.py` définit `sample_mean`. Elle reçoit un couple `(seed, size)`
   et renvoie la moyenne d’un échantillon simulé. Chaque appel crée son propre
   générateur. Les tâches fournies ont un effectif entier strictement positif.
2. `parallel_steps.py` importe cette fonction et définit `run_sequential` :
   appeler chaque tâche à son tour et conserver les résultats dans une liste.
3. Le même script définit `run_parallel` : transmettre les mêmes tâches à des
   processus séparés, puis récupérer les résultats dans le même ordre.
4. `main` appelle les deux fonctions et vérifie leur accord. Le bloc
   `if __name__ == "__main__":` lance `main` lorsque le fichier est exécuté
   directement ; il évite de relancer ce travail lors d’un import.

Exécutez le fichier dans le terminal : le mode `spawn` démarre des Python
neufs qui doivent pouvoir importer la fonction. Ne recopiez pas ce programme
dans une cellule de notebook. Cet exemple utilise seulement la bibliothèque
standard ; il ne promet aucun gain de vitesse.

## Travail autonome B ou C

Terminer d'abord le [socle de conversion](../exercises/README.md), puis
choisir une piste. Ces scripts sont des démonstrations complètes ; le travail
consiste à formuler une prédiction, changer un paramètre, conserver la preuve
d'accord des résultats et interpréter les mesures. Les commandes partent de
`lab`, avec le Python du projet.

## Trois mécanismes distincts

| Mécanisme | Travail effectué | Point à examiner |
| --- | --- | --- |
| Vectorisation NumPy | Une opération sur un tableau est exécutée par une routine compilée | Évite la boucle explicite en Python ; ne signifie pas automatiquement plusieurs cœurs |
| Threads | Des lots NumPy partagent le même processus et travaillent sur des tranches disjointes | Pour ce calcul numérique, NumPy peut libérer le GIL ; aucune garantie de gain |
| Processus | Des tâches vivent dans des interpréteurs séparés | Démarrage, transmission des arguments et retour des résultats ont un coût |

Ces démonstrations utilisent le CPU. Elles ne demandent ni GPU ni service
cloud. Accélérer le même calcul ne remplace pas la validation de son résultat.

## B — Même conversion, boucle ou tableaux

`compare_execution.py` convertit les mêmes valeurs de minutes en heures par
une boucle Python, NumPy, puis NumPy réparti entre threads. NumPy est requis.

```text
python performance/compare_execution.py --size 100000 --workers 2 --repeats 3 --seed 404
```

| Option | Défaut | Domaine |
| --- | --- | --- |
| `--size` | `200000` | 1 à 5 000 000 valeurs |
| `--workers` | `2` | 1 à 4 threads |
| `--repeats` | `3` | 2 à 20 mesures |
| `--seed` | `404` | Entier positif ou nul |

Avant de mesurer, le script vérifie les cas connus `0`, `60`, `90`, puis
compare chaque méthode au résultat de référence. Une exécution de préparation
précède les répétitions chronométrées. Chaque résultat chronométré est aussi
contrôlé après la mesure ; la médiane et toutes les durées sont affichées.

Le temps comprend **le calcul et l'allocation de la sortie**. Pour les threads,
il comprend aussi la création et la fermeture du pool. La génération des
données et les comparaisons ne sont pas chronométrées. Les méthodes sont
mesurées successivement : l'activité de la machine peut influencer les durées.

Comparer d'abord deux tailles, par exemple `10000` et `1000000`, à workers
constants. Revenir ensuite à une taille fixe et comparer 1, 2 et 4 workers.
Un ralentissement peut révéler le coût d'organisation ou une limite de bande
passante mémoire ; il ne signifie pas à lui seul que le programme est faux.

## C — Des tâches indépendantes dans des processus

`process_tasks.py` contient le worker importable :

```text
SimulationTask(seed: int, samples: int)
simulate_sample(task: SimulationTask) -> SimulationSummary
```

Chaque tâche génère un échantillon synthétique gaussien de moyenne théorique
100 et d'écart-type 18. Elle renvoie seulement sa seed, son effectif, sa moyenne
observée et la proportion de valeurs supérieures à 130. Il ne s'agit pas de
données observées ni d'un test statistique.

`run_processes.py` construit la liste des tâches, l'exécute séquentiellement,
puis avec `ProcessPoolExecutor`. La seed d'une tâche reste la même dans les
deux exécutions ; les seeds diffèrent entre tâches.

Ce programme reprend l’organisation de `parallel_steps.py`, mais sa fonction
`simulate_sample` renvoie davantage d’informations que `sample_mean`. Les
paramètres de chaque tâche sont nommés dans `SimulationTask`, et les calculs
sont répétés pour mesurer des durées. Il s’agit du programme complet de la
piste C, déjà décrit dans le livret DOCX.

```text
python performance/run_processes.py --tasks 4 --samples 20000 --workers 2 --repeats 3 --seed 404
```

| Option | Défaut | Domaine |
| --- | --- | --- |
| `--tasks` | `8` | 1 à 32 tâches |
| `--samples` | `50000` | 1 à 1 000 000 observations par tâche |
| `--workers` | `2` | 1 à 4 processus |
| `--repeats` | `3` | 2 à 10 mesures |
| `--seed` | `404` | Entier positif ou nul ; les tâches utilisent `seed + index` |

Le script contrôle l'égalité exacte des résumés avant les mesures et après
chaque répétition. Le temps est mesuré **de bout en bout**, y compris le
démarrage, les transferts et la fermeture du pool à chaque appel. Les
comparaisons des résultats sont exclues. La première comparaison sert aussi
de préparation ; elle ne conserve pas de pool pour les mesures suivantes.

Comparer 1 puis 2 workers à tâches constantes. Augmenter ensuite la taille
des échantillons sans modifier le reste. Prévoir quelle partie du coût peut
être amortie. Davantage de processus ne modifie ni le nombre d'observations
ni la précision statistique du travail fixé.

Garder le worker dans son module, le mode explicite `spawn` et le garde
`if __name__ == "__main__":`. Exécuter le script dans le terminal ; recopier
le worker dans une cellule de notebook ne reproduit pas cette architecture.
Le mode `spawn` a été testé sur Linux ; le kit n'a pas été exécuté sur Windows.

## Preuve à conserver

Noter la version de Python, les commandes, les paramètres, l'accord des
résultats, les mesures répétées et leur médiane. Formuler une conclusion
limitée au calcul, au protocole et à la machine utilisés. Compléter
[SUBMISSION.md](../SUBMISSION.md), avec une explication du résultat du socle.
