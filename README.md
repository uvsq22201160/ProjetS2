# Mastermind
[mastermind.pdf](https://github.com/uvsq22201160/ProjetS2/files/10745164/mastermind.pdf)

URL : https://github.com/uvsq22201160/ProjetS2/

# Groupe : LDDMP
Gaël FERREIRA RODRIGUEZ, Elise MOULIN, César PITIGLIANO, Noel-Marie N'dri

# Utilisation du programme
Afin de pouvoir bénéficier du jeu Mastermind, veuillez télécharger les documents : [mastermind.py](https://github.com/uvsq22201160/ProjetS2/blob/main/mastermind.py) et [sauvegarde.py](https://github.com/uvsq22201160/ProjetS2/blob/main/sauvegarde.py). Veuillez au préalable vérifier que le document sauvegarde.py est vide. Une fois le code présent dans votre interface, exécutez-le... et profitez 

# Mastermind : règles du jeu
Le Mastermind est un jeu de réflexion pour deux joueurs, où l'objectif est de deviner une combinaison secrète de couleurs choisie par l'autre joueur. 
Voici les règles de base* :

-Le joueur qui crée la combinaison secrète(le codificateur) choisit une série de couleurs.

-Le joueur qui devine doit proposer(le décodeur) une combinaison de couleurs ou de chiffres.

-Le joueur qui a créé la combinaison secrète donne à chaque essais des indications sur le code. 
    
    Ces dernières sont données grâce à des pions rouges ou blancs :

-un pion rouge signifie qu'un élément de la proposition à deviner est non seulement de la bonne couleur mais aussi à la bonne place.

-un pion blanc signifie qu'un élément de la proposition à decoder est de la bonne couleur mais n'est pas situé à la bonne position.

-le décodeur doit ainsi utiliser les différents indices qui lui sont donnés après chaque essai poour réajuster sa prochaine tentative.

-le but de ce jeu est de trouver par déductions successives la combinaison de couleurs donnée par le codificateur en un nombre limité d'essais

-Enfin,une partie se termine lorsque le joueur qui devine parvient à trouver la combinaison secrète ou atteint le nombre maximal d'essais autorisés
    



*Selon les versions du jeu, les paramètres de base (nombres de couleures différentes, nombres de couleures dans le code, nombre d'essais...) peuvent varier.
