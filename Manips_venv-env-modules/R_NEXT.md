# Découvrir R après cette séance

R est un langage et un environnement d'exécution distinct de Python.

RStudio est un environnement de travail pour R : son installation ne remplace pas celle de R.

L'installation collective de R ne fait pas partie des exercices de cette séance.

| Système | Parcours à préparer |
| --- | --- |
| Windows | Installer R depuis [CRAN pour Windows](https://cran.r-project.org/bin/windows/base/), puis une version compatible de [RStudio Desktop](https://posit.co/download/rstudio-desktop/). Vérifier le système Windows pris en charge avant de choisir une version. |
| Linux | Suivre les instructions CRAN de [la distribution concernée](https://cran.r-project.org/bin/linux/) — par exemple [Ubuntu](https://cran.r-project.org/bin/linux/ubuntu/) — puis installer le paquet RStudio adapté à cette distribution. |

`pip` installe des packages Python. `rpy2` est une interface entre Python et R ; installer ce package ne fournit pas à lui seul l'environnement R nécessaire.

Les versions de R, Python, `rpy2` et le système doivent être compatibles.

Cette passerelle ajoute une couche à diagnostiquer : commencez par exécuter un petit script directement dans R, puis examinez l'intégration si elle répond à un besoin concret.

Une première comparaison pourra reprendre le même petit tableau dans les deux langages : vérifier les types, calculer un résumé, puis expliquer ce qui est identique dans le raisonnement et ce qui change dans l'écriture.

Sources : [documentation RStudio](https://docs.posit.co/ide/user/), [présentation et prérequis de rpy2](https://rpy2.github.io/doc/latest/html/overview.html).