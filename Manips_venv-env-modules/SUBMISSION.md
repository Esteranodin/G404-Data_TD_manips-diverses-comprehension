# Retour de travail

Préparez un fichier `RETURN.md` avec les points ci-dessous et les fichiers de code que vous avez modifiés.

Le choix du canal de remise sera indiqué séparément ; aucun compte de service n'est nécessaire pour préparer ce retour.

1. **Socle commun, puis piste choisie.** Décrivez le contrat de conversion et l'approfondissement A, B ou C que vous avez réalisé. Quel comportement vouliez-vous vérifier ? Avec quelles entrées et quelles contraintes ?
2. **Observation.** Quel défaut, désaccord ou résultat avez-vous constaté ? Indiquez une valeur et son type, une erreur ou une mesure pertinente.
3. **Diagnostic.** Quelle était votre hypothèse ? Qu'avez-vous inspecté pour la confirmer ou l'abandonner ?
4. **Modification.** Quel changement précis avez-vous effectué et pourquoi ?
5. **Preuve.** Copiez les commandes lancées depuis `lab`, la version de Python, les résultats utiles des tests ou des mesures et leur interprétation. Distinguez les tests réellement exécutés des tests seulement proposés.
6. **Point ouvert.** Quelle question reste à résoudre ? Si vous avez utilisé une IA, quelle suggestion avez-vous acceptée, corrigée ou refusée, et sur quelle preuve ?

Pour le socle commun, conservez les trois contrôles numériques de `exercises/check_manual.py` et leur type de résultat. Ajoutez un quatrième cas valide et justifiez son choix.

Indiquez les limites de l'ensemble de ces contrôles : les entrées invalides restent notamment hors de cette preuve limitée.

Pour la piste A, joignez la validation du contrat complet et les tests correspondants.

Pour une comparaison de performances, indiquez la taille du travail, le nombre de workers et de répétitions, la seed, l'accord des résultats et les coûts inclus dans la mesure.

Une conclusion « plus rapide » sans ces conditions ne permet pas de reproduire la comparaison.

Enregistrez les fichiers, fermez les anciens processus et relancez les commandes utiles avant de remettre le travail.

Pour un notebook, redémarrez le kernel puis exécutez les cellules dans l'ordre.

Ne joignez pas `.venv/`, `.env`, les caches, des clés de service ou des données personnelles.

Un court extrait de sortie pertinent vaut mieux qu'une capture complète du terminal contenant des chemins ou informations inutiles.

### Numpy plus rapide
```bash
(.venv) PS J:\DEV\G404-DATA_TD\G404-Data_TD_manips-diverses-comprehension\Manips_venv-env-modules\lab> python performance/compare_execution.py --size 100000 --workers 2 --repeats 3 --seed 404
Résultats vérifiés avant et après chaque mesure.
Temps : calcul + allocation ; threads : création/fermeture du pool incluses.
Génération des données et comparaison des résultats exclues des temps.

Boucle Python           médiane=   20.289 ms ; mesures=[20.289, 21.060, 19.389]
NumPy                   médiane=    0.300 ms ; mesures=[0.280, 0.316, 0.300]
NumPy + 2 thread(s)     médiane=    0.876 ms ; mesures=[0.876, 0.858, 1.079]

Aucun gain n'est garanti : taille, mémoire, calcul et démarrage comptent.
(.venv) PS J:\DEV\G404-DATA_TD\G404-Data_TD_manips-diverses-comprehension\Manips_venv-env-modules\lab> python performance/compare_execution.py --size 10000 --workers 2 --repeats 3 --seed 404 
10,000 valeurs ; seed=404 ; 3 mesures.
Résultats vérifiés avant et après chaque mesure.
Temps : calcul + allocation ; threads : création/fermeture du pool incluses.
Génération des données et comparaison des résultats exclues des temps.

Boucle Python           médiane=    2.050 ms ; mesures=[1.800, 2.062, 2.050]
NumPy                   médiane=    0.007 ms ; mesures=[0.008, 0.007, 0.007]
NumPy + 2 thread(s)     médiane=    0.483 ms ; mesures=[0.520, 0.483, 0.477]

Aucun gain n'est garanti : taille, mémoire, calcul et démarrage comptent.
(.venv) PS J:\DEV\G404-DATA_TD\G404-Data_TD_manips-diverses-comprehension\Manips_venv-env-modules\lab> python performance/compare_execution.py --size 1000000 --workers 2 --repeats 3 --seed 404
1,000,000 valeurs ; seed=404 ; 3 mesures.
Résultats vérifiés avant et après chaque mesure.
Temps : calcul + allocation ; threads : création/fermeture du pool incluses.
Génération des données et comparaison des résultats exclues des temps.

Boucle Python           médiane=  183.593 ms ; mesures=[202.207, 183.593, 171.965]
NumPy                   médiane=    2.357 ms ; mesures=[2.357, 2.324, 2.559]
NumPy + 2 thread(s)     médiane=    6.164 ms ; mesures=[3.495, 28.046, 6.164]

Aucun gain n'est garanti : taille, mémoire, calcul et démarrage comptent.
```

### En changeant le nombre de Threads
> 2 plus rapide que 1, mais 4 plus ments que 2...

```bash
(.venv) PS J:\DEV\G404-DATA_TD\G404-Data_TD_manips-diverses-comprehension\Manips_venv-env-modules\lab> python performance/compare_execution.py --size 100000 --workers 1 --repeats 3 --seed 404 
Résultats vérifiés avant et après chaque mesure.
Temps : calcul + allocation ; threads : création/fermeture du pool incluses.
Génération des données et comparaison des résultats exclues des temps.

Boucle Python           médiane=   26.239 ms ; mesures=[23.493, 26.239, 59.182]
NumPy                   médiane=    0.400 ms ; mesures=[0.400, 0.413, 0.350]
NumPy + 1 thread(s)     médiane=    1.339 ms ; mesures=[7.573, 1.339, 0.806]

Aucun gain n'est garanti : taille, mémoire, calcul et démarrage comptent.
(.venv) PS J:\DEV\G404-DATA_TD\G404-Data_TD_manips-diverses-comprehension\Manips_venv-env-modules\lab> python performance/compare_execution.py --size 100000 --workers 2 --repeats 3 --seed 404 
100,000 valeurs ; seed=404 ; 3 mesures.
Résultats vérifiés avant et après chaque mesure.
Temps : calcul + allocation ; threads : création/fermeture du pool incluses.
Génération des données et comparaison des résultats exclues des temps.

Boucle Python           médiane=   16.697 ms ; mesures=[16.661, 20.826, 16.697]
NumPy                   médiane=    0.263 ms ; mesures=[0.263, 0.248, 0.307]
NumPy + 2 thread(s)     médiane=    0.899 ms ; mesures=[0.899, 0.790, 1.149]

Aucun gain n'est garanti : taille, mémoire, calcul et démarrage comptent.
(.venv) PS J:\DEV\G404-DATA_TD\G404-Data_TD_manips-diverses-comprehension\Manips_venv-env-modules\lab> python performance/compare_execution.py --size 100000 --workers 4 --repeats 3 --seed 404 
100,000 valeurs ; seed=404 ; 3 mesures.
Résultats vérifiés avant et après chaque mesure.
Temps : calcul + allocation ; threads : création/fermeture du pool incluses.
Génération des données et comparaison des résultats exclues des temps.

Boucle Python           médiane=   16.084 ms ; mesures=[16.084, 15.579, 16.472]
NumPy                   médiane=    0.279 ms ; mesures=[0.275, 0.279, 0.327]
NumPy + 4 thread(s)     médiane=    1.061 ms ; mesures=[1.074, 1.061, 1.038]

Aucun gain n'est garanti : taille, mémoire, calcul et démarrage comptent.
```