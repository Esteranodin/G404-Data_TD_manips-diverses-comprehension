# Demander une aide, puis vérifier

Une aide IA peut proposer une explication, un test ou une modification. La
preuve de correction repose sur le contrat, l'exécution et l'interprétation
des résultats. Cette activité peut être réalisée avec un assistant disponible,
ou uniquement avec les deux réponses fictives ci-dessous. Aucun abonnement
ni création de compte n'est nécessaire.

## Préparer une demande utile

Avant de demander de l'aide, écrivez le résultat attendu, le résultat observé
et ce que vous avez déjà vérifié. Fournissez seulement le code pertinent,
les valeurs d'entrée, l'erreur exacte et la version de Python. Distinguez une
question sur le raisonnement d'une demande de modification du programme.

Un canevas à adapter :

> ✨ Je travaille sur une fonction Python dont le contrat est [contrat]. Avec
> [entrée], j'attends [valeur et type] et j'observe [valeur et type]. Voici le
> code et le test. Explique le désaccord, propose une modification limitée et
> un moyen de vérifier le résultat. Conserve le contrat ; précise ce que tu
> n'as pas exécuté. Utilise des identifiants et commentaires en anglais et
> explique en français.

Le symbole ✨ signale ici un texte préparé avec une IA, à relire et adapter.
N'envoyez ni `.env`, ni mot de passe, ni données personnelles pour résoudre
cet exercice. Les exemples du kit sont suffisants.

Après la réponse, vérifiez les changements un par un. Demandez-vous ce que
la proposition explique réellement, exécutez les tests et ajoutez un cas qui
pourrait réfuter l'explication. Conservez dans votre retour un exemple de
suggestion acceptée, corrigée ou refusée, avec sa justification.

## Personnaliser au bon endroit

| Réglage ou information | Portée |
| --- | --- |
| Pylance / réglages VS Code | Complétion classique, analyse et affichage de l'éditeur |
| Instructions personnalisées de ChatGPT | Préférences répétées entre conversations, lorsque disponibles |
| Prompt de la conversation | Contrat, code, erreur et objectif de la tâche actuelle |
| Instructions de projet d'un agent IA | Conventions pour les fonctions de chat ou d'agent compatibles |
| Suggestions IA pendant la frappe | Réglages propres à l'extension ; contexte du code et fichiers ouverts |

Pour ChatGPT, placez les préférences stables dans **Paramètres →
Personnalisation**, si ce contrôle existe dans votre interface. Le contrat
spécifique à un exercice appartient au prompt. Les fonctions et libellés
peuvent varier selon l'interface et le compte.

Dans VS Code, les instructions personnalisées de Copilot ne s'appliquent pas
aux suggestions automatiques pendant la frappe. Les commentaires et fichiers
ouverts peuvent leur donner du contexte. Apprendre à activer ou désactiver
ces suggestions permet de distinguer sa propre prédiction de celle de l'outil.

## Deux réponses fictives à examiner

Ces réponses ont été rédigées pour l'exercice. Elles ne sont pas la trace d'une
conversation réelle. Elles concernent seulement le rectangle étudié ensemble,
pas la solution de la piste autonome.

Contrat examiné : `Rectangle(4, 3).area()` doit fournir la valeur numérique `12`
réutilisable dans un calcul. L'implémentation actuelle renvoie `"Area: 12"`.

**Réponse fictive A**

> ✨ Le programme produit bien 12 dans son message. Remplacez le résultat attendu
> du test par `"Area: 12"`. Le test passera et le problème sera résolu.

**Réponse fictive B**

> ✨ Le calcul et sa présentation ont été mélangés. Le contrat demande une
> valeur numérique : la fonction doit renvoyer cette valeur, tandis que le
> code appelant prépare le message à afficher. Gardez un test numérique et
> vérifiez aussi que le résultat reste utilisable dans un autre calcul. Je
> n'ai pas exécuté votre projet.

Pour chaque réponse, identifiez ce qu'elle change, ce qu'elle suppose et la
preuve à produire. Laquelle respecte le contrat ? Un test devenu vert suffit-il
si son résultat attendu a changé ? Quel cas supplémentaire rendrait votre
conclusion plus solide ?

Sources : [instructions et personnalisation ChatGPT](https://learn.chatgpt.com/docs/personalize),
[construire une demande](https://learn.chatgpt.com/docs/prompting),
[instructions VS Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions),
[suggestions IA pendant la frappe](https://code.visualstudio.com/docs/editing/ai-powered-suggestions).
