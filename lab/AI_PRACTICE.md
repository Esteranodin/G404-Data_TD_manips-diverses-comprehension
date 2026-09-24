# Utiliser une aide IA et garder une trace fiable du travail

Ces activités accompagnent le cours : formuler une demande précise, séparer
les préférences générales du besoin actuel, puis transmettre ce qui permet
de reprendre le travail. Conservez vos réponses dans `AI_NOTES.md`, dans le
dossier `lab`.

Vous pouvez utiliser un assistant disponible ou travailler avec les réponses
fictives fournies ici. Aucun compte ni abonnement n'est nécessaire. Les
exemples contiennent uniquement du code et des données créés pour le cours.

Pour les exercices de l'après-midi, le [livret DOCX](../documents/2026-09-24_python_exercices.docx)
reste la référence : exercice commun, puis choix A, B ou C.

## 1. Passer d'une demande vague à une question vérifiable

### Un petit programme complet

Le rectangle du cours est ici présenté sous la forme d'une fonction autonome.
Enregistrez ce programme dans `ai_rectangle_v1.py`, dans `lab`, puis lancez
`python ai_rectangle_v1.py` depuis ce dossier. Utilisez le Python préparé pour
le cours, comme expliqué dans [ENVIRONMENT.md](ENVIRONMENT.md).

```python
def area(width: float, height: float) -> float:
    return f"Area: {width * height}"

result = area(4, 3)
print(repr(result))
print(type(result).__name__)
assert result == 12
```

La fonction doit renvoyer **le nombre 12**, que l'on pourra réutiliser dans
un calcul. Dans cette version, le programme affiche d'abord `'Area: 12'`, puis `str` ;
la dernière ligne déclenche `AssertionError`. C'est l'erreur volontaire à
examiner. L'indication `-> float` ne transforme pas le résultat en nombre.

### Exemple d'une demande précise

Le symbole ✨ signale un texte préparé avec une IA, à relire et adapter.
Le texte ci-dessous accompagne **le code complet ci-dessus** et les résultats
de votre exécution :

> ✨ Je travaille sur `ai_rectangle_v1.py`. Avec `area(4, 3)`, j'attends le
> nombre 12, réutilisable dans un calcul. Le programme affiche `'Area: 12'`
> et le type `str`, puis `assert result == 12` déclenche `AssertionError`.
> Voici le code et la sortie de mon exécution. Explique la cause avant de
> proposer une correction de la fonction. Conserve le résultat numérique
> attendu. Propose un autre cas à vérifier et indique ce que tu n'as pas
> exécuté. Explique en français courant ; garde le code en anglais.

### À vous de travailler

1. Partez de cette demande insuffisante : « ✨ Mon calcul est faux. Corrige-le. »
   Écrivez votre propre demande avec l'entrée, le résultat attendu, la valeur
   observée, son type et l'aide souhaitée. Joignez le code utile et la sortie
   obtenue, sans ajouter de fichiers sans rapport avec le problème.
2. Examinez les deux réponses fictives ci-dessous. Pour chacune, indiquez
   ce qu'elle propose de changer et comment vérifier si cela répond au besoin.
3. Copiez votre fichier sous le nom `ai_rectangle_v2.py`, puis corrigez cette
   copie. Gardez le résultat numérique attendu dans le test. Vérifiez aussi
   que le résultat peut servir dans une addition et choisissez une autre paire
   de dimensions dont vous connaissez l'aire.
4. Dans `AI_NOTES.md`, conservez votre demande, votre décision sur chaque
   réponse, les commandes exécutées et les résultats observés pour la version 2.
   Séparez une vérification proposée d'une vérification réellement effectuée.

**Réponse fictive A**

> ✨ Le texte contient bien 12. Remplacez le résultat attendu du test par
> `"Area: 12"` ; le test passera.

**Réponse fictive B**

> ✨ Le résultat est du texte alors qu'un nombre est attendu. Séparez le
> calcul du message affiché. Conservez le test numérique et vérifiez un
> deuxième rectangle. Je n'ai pas exécuté votre programme.

**Pour juger votre travail.** Une autre personne peut-elle reproduire l'erreur
avec les informations fournies ? La correction conserve-t-elle le résultat
attendu ? Vos traces montrent-elles quels fichiers et quels cas ont été exécutés ?
La réussite de quelques exemples ne vérifie pas toutes les valeurs possibles.

## 2. Séparer les préférences générales de la demande du jour

Une préférence générale décrit une façon de travailler que vous souhaitez
retrouver dans plusieurs tâches. La demande du jour précise le problème à
résoudre et les fichiers concernés.

| Préférences générales possibles | Informations propres au rectangle |
| --- | --- |
| Expliquer en français courant. | Examiner `ai_rectangle_v1.py`. |
| Garder les noms et commentaires du code en anglais. | Avec 4 et 3, renvoyer le nombre 12. |
| Dire si une vérification a été exécutée ou seulement proposée. | Corriger uniquement le résultat renvoyé par `area`. |

Selon l'outil, ces informations peuvent être placées dans des réglages, un
fichier d'instructions ou directement dans la demande. Pour cette activité,
écrivez-les dans deux blocs de `AI_NOTES.md` : **Mes préférences** et
**Ma demande actuelle**. Vous pouvez vérifier leur contenu sans modifier
aucun réglage d'un service.

### À vous de travailler

1. Écrivez deux ou trois préférences utiles pour vos prochains travaux.
   Vérifiez qu'elles restent compréhensibles sans connaître le rectangle.
2. Écrivez les informations propres à votre version actuelle du programme.
   N'y recopiez pas une ancienne erreur si vous l'avez déjà corrigée : indiquez
   le résultat le plus récent et ce qui reste à vérifier.
3. Passez au problème suivant : une fonction `double(value)` reçoit `7`,
   doit renvoyer le nombre `14`, mais renvoie le texte `"14"`. Expliquez
   quelles préférences vous gardez et quelles informations vous remplacez.
   Il n'est pas demandé d'écrire cette nouvelle fonction.

**Question à discuter.** « N'utilise jamais de classe » est-il une préférence
qui vous servira dans tous vos projets, ou une limite adaptée à un exercice
particulier ? Justifiez votre choix.

**À conserver.** Vos deux blocs et un exemple de phrase devenue inadaptée
quand vous avez changé de problème. Une consigne écrite ne prouve pas qu'elle
a été suivie : relevez dans la réponse un passage qui permet de le vérifier.

## 3. Transmettre assez de contexte pour reprendre le travail

Dans cette activité, le **contexte** est l'ensemble des informations utiles
pour traiter la demande : objectif, code concerné, décisions prises, résultats
observés et prochaine vérification. Une personne qui reprend le dossier en
a besoin, tout comme l'assistant auquel vous adressez une nouvelle demande.

Les fonctions appelées « mémoire » diffèrent selon les outils. Ne supposez
pas qu'une préférence enregistrée, une autre conversation et la dernière
version d'un fichier seront toutes disponibles pour la prochaine réponse.
Précisez les informations à reprendre et fournissez les fichiers utiles.

### Pourquoi le contexte se perd ou devient trompeur

| Situation | Ce qu'il faut vérifier |
| --- | --- |
| La nouvelle demande dit « corrige comme avant ». | Le besoin et les décisions précédentes sont-ils explicités ? |
| Une note dit « tout fonctionne ». | Sur quel fichier, avec quelle commande et quels cas ? |
| Un fichier a changé depuis le dernier test. | Le résultat annoncé correspond-il encore à son contenu ? |
| Un résumé a raccourci la conversation. | A-t-il conservé les exceptions, les essais non faits et les questions ouvertes ? |

### Préparer une fiche de reprise

Dans `AI_NOTES.md`, ajoutez une section **Reprendre le rectangle** en suivant
ce modèle. Remplacez chaque indication par ce que vous avez réellement fait.

```text
Objectif :
Fichier actuel joint : ai_rectangle_v2.py
Version précédente conservée : ai_rectangle_v1.py
Comportement à conserver :
Modification effectuée :
Dernière vérification exécutée : commande et fichier concernés
Résultat observé : valeurs, types et cas vérifiés
Vérifications seulement proposées ou encore absentes :
Prochaine action demandée :
```

Les deux noms distinguent les étapes de cet exercice. Joignez le contenu
actuel du fichier : son nom seul ne décrit pas le code qu'il contient.
Si vous modifiez encore la version 2, mettez la fiche à jour et relancez
les vérifications utiles avant de réutiliser leur résultat.

### À vous de travailler

1. Donnez à un collègue uniquement votre fiche et `ai_rectangle_v2.py`, sans
   les messages précédents. Vous pouvez aussi faire cette relecture seul en
   masquant les échanges précédents.
2. À partir de ces seuls éléments, la personne doit pouvoir dire ce que le
   programme doit faire, quel fichier utiliser, ce qui a été vérifié et quelle
   action reste à réaliser. Notez les informations qui lui manquent.
3. Examinez ce cas fictif : une note annonce « version 2 vérifiée », mais la
   seule commande conservée est `python ai_rectangle_v1.py`. Cette trace
   permet-elle de conclure sur la version 2 ? Corrigez l'affirmation et
   indiquez la prochaine vérification nécessaire.
4. Améliorez votre fiche. Si vous utilisez un assistant, accompagnez votre
   nouvelle demande de la fiche et du fichier actuel ; comparez sa réponse
   à ces éléments. Dire que le code fonctionne ne remplace pas son exécution.

**À conserver.** La fiche améliorée, les informations manquantes repérées et
la commande qui vérifierait le fichier actuel. Indiquez si cette commande
a ensuite été exécutée et avec quel résultat.

Utilisez les exemples du cours pour ces échanges. Les mots de passe, fichiers
`.env`, coordonnées et autres données personnelles n'aident pas à expliquer
le défaut de ce rectangle.
