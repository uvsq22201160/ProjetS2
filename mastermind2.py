import tkinter as tk
import random as rd
from json import *

     #################################################################################################
    #                                                                                                 #
   #   Mastermind   :    Gaël FERREIRA RODRIGUEZ / Elise MOULIN / César PITIGLIANO / Noel-Marie N'dri  #
    #                                                                                                 #
     #################################################################################################




# Conditions initiales #

Dict_liste_jeu = {"Liste du jeu 2D":[[]], "Liste du jeu complet":[], "Liste code":[], "ligne":0, "colonne":0, "Joueurs":""}

Dict_couleurs = {'black':0, 'green':0, 'blue':0, 'purple':0, 'yellow':0, 'orange':0, 'pink':0, 'cyan':0, 'grey':0, 'darkblue':0}

JOUEURS = 0

LISTE_JEU = [[]]
LISTE_JEU_COMPLET = []
LISTE_COULEURS = ['black', 'green', 'blue', 'purple', 'yellow', 'orange', 'pink', 'cyan', 'grey', 'darkblue']
LISTE_BOUTTONS = [0]*10
LISTE_CODE = []
CERCLE = [[]]
CERCLE2 = []
PIONS_BP = [[0]*4 for x in range(12)]
PIONS_MP = [[0]*4 for x in range(12)]

FIN_PARTIE = False

RECUPERATION = 0

test = 0 # nombre de fois que le joueur retourne au menu, permet de générer à nouveau la page d'accueil et de réinitialiser par conséquent les boutons


# Création de la fenêtre #

HEIGHT = 600
WIDTH = 600
fenetre = tk.Tk()
fenetre.title("Mastermind")
canvas = tk.Canvas(fenetre, height=HEIGHT, width=WIDTH, bg='papaya whip')
canvas.grid(row=0, column=0, rowspan=9, columnspan=11)




# Création des bouttons initiaux #

mode_un_joueur = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
mode_un_joueur.place(x=1000, y=0)
mode_deux_joueurs = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
mode_deux_joueurs.place(x=1000, y=0)
retour = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
retour.place(x=1000, y=0)
menu = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
menu.place(x=1000, y=0)
sauvegarder_oui = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
sauvegarder_oui.place(x=1000, y=0)
sauvegarder_non = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
sauvegarder_non.place(x=1000, y=0)
sauvegarder = tk.Label(text="", font=("Helvetica", "1"), bg="papaya whip")
sauvegarder.place(x=1000, y=0)
code = tk.Label(text="", font=("Helvetica", "1"), bg="papaya whip")
code.grid(row=0, column=5)
gagne = tk.Label(text="", font=("Helvetica", "1"), bg="papaya whip")
gagne.place(x=390, y=300)
perdu = tk.Label(text="", font=("Helvetica", "1"), bg="papaya whip")
perdu.place(x=390, y=300)

CHARGER_PARTIE = tk.Button(fenetre)
CHARGER_PARTIE.grid(row=3, column=5)
PARTIE_PERSONNALISE = tk.Button(fenetre)
PARTIE_PERSONNALISE.grid(row=7, column=5)

for i in range(8):
    LISTE_BOUTTONS[i] = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
    LISTE_BOUTTONS[i].place(x=1000, y=0)
for j in range(12):
    for k in range(4):
        PIONS_BP[j][k] = canvas.create_oval((0,0),(1,1), fill="papaya whip")
for l in range(12):
    for m in range(4):
        PIONS_MP[l][m] = canvas.create_oval((0,0),(1,1), fill="papaya whip")

# Canvas victoire #

def Victoire():
    '''Détruis les boutons et affiche que le joueur a gagné(e)'''
    global LISTE_BOUTTONS
    global LISTE_COULEURS
    global FIN_PARTIE
    global Dict_liste_jeu
    global LISTE_CODE
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global JOUEURS

    FIN_PARTIE = True
    for i in range(8):
        LISTE_BOUTTONS[i].destroy()
    retour.destroy()
    gagne.config(text="Vous avez gagné !", font=("Helvetica", "14"), bg="papaya whip")
    Dict_liste_jeu["ligne"]
    fichier = open("./sauvegarde.py", "w")
    dump(Dict_liste_jeu, fichier)
    fichier.close()
    LISTE_JEU = [[]]
    LISTE_JEU_COMPLET = []
    LISTE_CODE = []
    JOUEURS = 0


# Canvas défaite #

def Defaite():
    '''Détruis les boutons et affiche que le joueur a perdu(e)'''
    global LISTE_BOUTTONS
    global FIN_PARTIE
    global Dict_liste_jeu
    global LISTE_CODE
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global JOUEURS
    
    FIN_PARTIE = True
    for i in range(8):
        LISTE_BOUTTONS[i].destroy()
    retour.destroy()
    perdu.config(text="Vous avez perdu !", font=("Helvetica", "14"), bg="papaya whip")
    Dict_liste_jeu[MODE][0] = LISTE_JEU
    Dict_liste_jeu[MODE][1] = LISTE_JEU_COMPLET
    Dict_liste_jeu[MODE][2] = LISTE_CODE
    Dict_liste_jeu["Mode"] = MODE
    Dict_liste_jeu["Joueurs"] = JOUEURS
    fichier = open("./sauvegarde.py", "w")
    dump(Dict_liste_jeu, fichier)
    fichier.close()
    LISTE_JEU = [[]]
    LISTE_JEU_COMPLET = []
    LISTE_CODE = []
    JOUEURS = 0


# Sauvegarder #

def Sauvegarde():
    global MODE
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global JOUEURS
    global LISTE_CODE
    sauvegarder.destroy()
    sauvegarder_oui.destroy()
    sauvegarder_non.destroy()
    Dict_liste_jeu[MODE][0] = LISTE_JEU
    Dict_liste_jeu[MODE][1] = LISTE_JEU_COMPLET
    Dict_liste_jeu[MODE][2] = LISTE_CODE
    Dict_liste_jeu["Mode"] = MODE
    Dict_liste_jeu["Joueurs"] = JOUEURS
    fichier = open("./sauvegarde.py", "w")
    dump(Dict_liste_jeu, fichier)
    fichier.close()
    LISTE_JEU = [[]]
    LISTE_JEU_COMPLET = []
    LISTE_CODE = []
    JOUEURS = 0
    Accueil()

# Pas de sauvegarde #

def PasdeSauvegarde():
    global Dict_liste_jeu
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global LISTE_CODE
    global JOUEURS
    sauvegarder.destroy()
    sauvegarder_oui.destroy()
    sauvegarder_non.destroy()
    LISTE_JEU = [[]]
    LISTE_JEU_COMPLET = []
    LISTE_CODE = []
    JOUEURS = 0
    Dict_liste_jeu["Liste du jeu 2D"] = LISTE_JEU
    Dict_liste_jeu["Liste du jeu complet"] = LISTE_JEU_COMPLET
    Dict_liste_jeu["Liste code"] = LISTE_CODE
    Dict_liste_jeu["Joueurs"] = JOUEURS
    Accueil()


# Boutton Menu #

def Menu(ligne, colonne):
    '''Sauvegarde la partie si elle est en cours et relance le programme'''
    global LISTE_BOUTTONS
    global test
    global FIN_PARTIE
     
    test += 1

    if FIN_PARTIE == True:
        for i in range(8):
            LISTE_BOUTTONS[i].destroy()
        menu.destroy()
        retour.destroy()
        gagne.destroy()
        perdu.destroy()
        canvas.delete("all")
        PasdeSauvegarde()
    else:
        for i in range(8):
            LISTE_BOUTTONS[i].destroy()
        menu.destroy()
        retour.destroy()
        gagne.destroy()
        perdu.destroy()
        canvas.delete("all")
        sauvegarder.config(text="Souhaitez-vous sauvegarder ?", font=("Helvetica", "16"))
        sauvegarder.grid_configure(row=3, column=5)
        sauvegarder_oui.config(text="Oui", font=("Helvetica", "8"), command=lambda : Sauvegarde(ligne, colonne))
        sauvegarder_oui.grid_configure(row=5, column=4)
        sauvegarder_non.config(text="Non", font=("Helvetica", "8"), command=PasdeSauvegarde())
        sauvegarder_non.grid_configure(row=5, column=6)



# Boutton retour #

def Retour(colonne_total):
    '''Permet un retour en arrière (essais en plus) lors du jeu'''
    global LISTE_JEU_COMPLET
    global LISTE_JEU
    global CERCLE
   
    colonne = len(LISTE_JEU_COMPLET) % colonne_total
    ligne = int(len(LISTE_JEU_COMPLET) // colonne_total)

    if LISTE_JEU_COMPLET != []:
        if colonne == 0:
            for i in range(colonne_total):
                canvas.delete(CERCLE[ligne-1][i])
                canvas.delete(PIONS_BP[ligne-1][i])
                canvas.delete(PIONS_MP[ligne-1][i])
                LISTE_JEU[ligne-1].pop()
                LISTE_JEU_COMPLET.pop()
                
        else:
            for j in range(colonne_total):
                canvas.delete(CERCLE[ligne][j])
                canvas.delete(PIONS_BP[ligne][j])
                canvas.delete(PIONS_MP[ligne][j])    
                LISTE_JEU[ligne].pop()
                LISTE_JEU_COMPLET.pop()
                 



# Création des pions bien plaçés et mal plaçés #

def bienPlace(n, ligne, intervalleY):
    '''Compte les pions bien plaçés et les affiches'''
    global PIONS_BP
    global PIONS_MP
    x1, x2 = 300, 310
    y1 = 50 + (intervalleY/4 - 5) + (intervalleY)*(ligne-1)
    y2 = 50 + (intervalleY/4 + 5) + (intervalleY)*(ligne-1)
    for i in range(n):
        PIONS_BP[ligne-1][i] = canvas.create_oval((x1,y1),(x2,y2), fill="red")
        x1, x2 = x1+15, x2+15
    

def malPlace(n, ligne, intervalleY):
    '''Compte les pions mal plaçés et les affiches'''
    x1, x2 = 300, 310
    y1 = 50 + (intervalleY*(3/4) - 5) + (intervalleY)*(ligne-1)
    y2 = 50 + (intervalleY*(3/4) + 5) + (intervalleY)*(ligne-1)
    for i in range(n):
        PIONS_MP[ligne-1][i] = canvas.create_oval((x1,y1),(x2,y2), fill="white")
        x1, x2 = x1+15, x2+15



# Création partie interactive #

def Jeu(couleur, ligne_total, colonne_total, intervalleY, intervalleX):
    '''Permet d'afficher les actions exerçés par le joueur et vérifie si le joueur à gagné(e) ou perdu(e)'''
    global LISTE_JEU_COMPLET
    global LISTE_JEU
    global LISTE_CODE
    global CERCLE
    global LISTE_CODE
    global Dict_couleurs

    LISTE_JEU_COMPLET.append(couleur)
    colonne = len(LISTE_JEU_COMPLET) % colonne_total
    ligne = int(len(LISTE_JEU_COMPLET) // colonne_total)
    
    if ligne >= ligne_total:
        Defaite(ligne, colonne)
    else:
        if colonne == 1:
            LISTE_JEU.append([])
            LISTE_JEU[ligne].append(couleur)
            x1 = 10 + (intervalleX/2 - 10)
            x2 = 10 + (intervalleX/2 + 10)
            y1 = 50 + (intervalleY/2 - 10) + (intervalleY)*(ligne)
            y2 = 50 + (intervalleY/2 + 10) + (intervalleY)*(ligne)
            CERCLE[ligne][0] = canvas.create_oval(x1, y1, x2, y2, fill=couleur)
        elif colonne != 0:
            LISTE_JEU[ligne].append(couleur)
            x1 = 10 + (intervalleX/2 - 10) + (intervalleX)*(colonne-1)
            x2 = 10 + (intervalleX/2 + 10) + (intervalleX)*(colonne-1)
            y1 = 50 + (intervalleY/2 - 10) + (intervalleY)*(ligne)
            y2 = 50 + (intervalleY/2 + 10) + (intervalleY)*(ligne)
            CERCLE[ligne][colonne-1] = canvas.create_oval(x1, y1, x2, y2, fill=couleur)
        
        else :
            colonne = colonne - 1
            LISTE_JEU[ligne-1].append(couleur)
            # test #
            print(LISTE_CODE, LISTE_JEU)
            # test #
            x1 = 10 + (intervalleX/2 - 10) + (intervalleX)*(colonne)
            x2 = 10 + (intervalleX/2 + 10) + (intervalleX)*(colonne)
            y1 = 50 + (intervalleY/2 - 10) + (intervalleY)*(ligne-1)
            y2 = 50 + (intervalleY/2 + 10) + (intervalleY)*(ligne-1)
            CERCLE[ligne-1][colonne] = canvas.create_oval(x1, y1, x2, y2, fill=couleur)
            if LISTE_JEU[ligne-1] == LISTE_CODE:
                Victoire(ligne, colonne)
            else:
                bien_place = 0
                mal_place = 0
                for i in range(colonne_total):
                    Dict_couleurs[LISTE_CODE[i]] = LISTE_CODE.count(LISTE_CODE[i])
                for j in range(colonne_total):
                    Dict_couleurs[LISTE_JEU[ligne-1][j]] -= 1
                    if Dict_couleurs[LISTE_JEU[ligne-1][j]] >= 0:
                        if (LISTE_JEU[ligne-1][j] == LISTE_CODE[j]):
                            bien_place += 1
                        elif (LISTE_JEU[ligne-1][j] in LISTE_CODE) and (LISTE_JEU[ligne-1][j] != LISTE_CODE[j]):
                            mal_place += 1
                    elif Dict_couleurs[LISTE_JEU[ligne-1][j]] < 0 and (LISTE_JEU[ligne-1][j] == LISTE_CODE[j]):
                        bien_place += 1
                        mal_place -= 1

                bienPlace(bien_place, ligne, intervalleY)
                malPlace(mal_place, ligne, intervalleY)
                
        
        

def Recuperation(condition, ligne_total, colonne_total, intervalleY, intervalleX):
    global LISTE_JEU_COMPLET
    global LISTE_JEU
    global CERCLE
    global LISTE_CODE
    global Dict_couleurs
    global Dict_liste_jeu

    if condition == 1:
        LISTE_CODE = Dict_liste_jeu["Liste code"]
        for i in range(len(LISTE_JEU_COMPLET)):
            colonne = (i+1) % colonne_total
            ligne = int((i+1) // colonne_total)
            if ligne > ligne_total:
                Defaite(ligne, colonne)
            else:
                if colonne == 1:
                    x1 = 10 + (intervalleX/2 - 10)
                    x2 = 10 + (intervalleX/2 + 10)
                    y1 = 50 + (intervalleY/2 - 10) + (intervalleY)*(ligne)
                    y2 = 50 + (intervalleY/2 + 10) + (intervalleY)*(ligne)
                    CERCLE[ligne][0] = canvas.create_oval(x1, y1, x2, y2, fill=LISTE_JEU_COMPLET[i])
                elif colonne != 0:
                    x1 = 10 + (intervalleX/2 - 10) + (intervalleX)*(colonne-1)
                    x2 = 10 + (intervalleX/2 + 10) + (intervalleX)*(colonne-1)
                    y1 = 50 + (intervalleY/2 - 10) + (intervalleY)*(ligne)
                    y2 = 50 + (intervalleY/2 + 10) + (intervalleY)*(ligne)
                    CERCLE[ligne][colonne-1] = canvas.create_oval(x1, y1, x2, y2, fill=LISTE_JEU_COMPLET[i])  
                else :
                    colonne = colonne - 1
                    x1 = 10 + (intervalleX/2 - 10) + (intervalleX)*(colonne)
                    x2 = 10 + (intervalleX/2 + 10) + (intervalleX)*(colonne)
                    y1 = 50 + (intervalleY/2 - 10) + (intervalleY)*(ligne-1)
                    y2 = 50 + (intervalleY/2 + 10) + (intervalleY)*(ligne-1)
                    CERCLE[ligne-1][colonne] = canvas.create_oval(x1, y1, x2, y2, fill=LISTE_JEU_COMPLET[i])

                    if LISTE_JEU[ligne-1] == LISTE_CODE:
                        Victoire(ligne, colonne)
                    else:
                        bien_place = 0
                        mal_place = 0
                        for j in range(colonne_total):
                            Dict_couleurs[LISTE_CODE[j]] = LISTE_CODE.count(LISTE_CODE[j])
                        for k in range(colonne_total):
                            Dict_couleurs[LISTE_JEU[ligne-1][k]] -= 1
                            if Dict_couleurs[LISTE_JEU[ligne-1][k]] >= 0:
                                if (LISTE_JEU[ligne-1][k] == LISTE_CODE[k]):
                                    bien_place += 1
                                elif (LISTE_JEU[ligne-1][k] in LISTE_CODE) and (LISTE_JEU[ligne-1][k] != LISTE_CODE[k]):
                                    mal_place += 1
                            elif Dict_couleurs[LISTE_JEU[ligne-1][k]] < 0 and (LISTE_JEU[ligne-1][k] == LISTE_CODE[k]):
                                bien_place += 1
                                mal_place -= 1

                        bienPlace(bien_place, ligne, intervalleY)
                        malPlace(mal_place, ligne, intervalleY)



# Création fonction deux joueurs #

def deuxJoueurs(couleurs, ligne, colonne, intervalleY, intervalleX, recuperation):
    '''Permet de démarrer le jeu à 2 joueurs'''
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global LISTE_CODE
    global CERCLE
    global PIONS_BP
    global PIONS_MP
    global JOUEURS
    global Dict_couleurs

    JOUEURS = 2

    mode_un_joueur.destroy()
    mode_deux_joueurs.destroy()
   
    menu.config(text="MENU", font=("Helvetica", "8"), bg="papaya whip", command=Menu)
    menu.place_configure(x=40, y=5)
    retour.config(text="←", font=("Helvetica", "8"), bg="papaya whip", command=Retour(colonne))
    retour.place_configure(x=10, y=5)

    PIONS_BP = [[0]*4 for x in range(ligne)]
    PIONS_MP = [[0]*4 for x in range(ligne)]
    CERCLE = [[0]*colonne for x in range(ligne)]


    # Création de la grille #
    x1, y1 = 10, 50
    x2 = x1+intervalleX
    y2 = y1+intervalleY
    for y in range(ligne):
        for z in range(colonne):
            canvas.create_rectangle(x1,y1, x2,y2, fill="saddle brown")
            x1, x2 = x2, x2+intervalleX
        y1, y2 = y2, y2+intervalleY
        x1 = 10
        x2 = x1+intervalleX
    
    for i in range(ligne):
        canvas.create_rectangle(290, 50+(intervalleY*(i)), 360, 50+(intervalleY*(i+1)))

    # Création du jeu (colonne secret) #
    for a in range(colonne):
        print(couleurs)
        couleur_secret = str(input("Choisissez la couleur numéro "+str(a+1)+" parmi les couleurs présentes :\n"))
        while not (couleur_secret in couleurs):
            print(couleurs)
            couleur_secret = str(input("Choisissez la couleur numéro "+str(a+1)+" parmi les couleurs présentes :\n"))
        LISTE_CODE.append(couleur_secret)

    for j in range(colonne):
        Dict_couleurs[LISTE_CODE[j]] = LISTE_CODE.count(LISTE_CODE[j])
    
    Recuperation(recuperation, ligne, colonne, intervalleY, intervalleX)

    nb_couleurs = len(couleurs)
    x = 0
    for i in range(nb_couleurs):
        LISTE_BOUTTONS[i].grid_configure(row=8, column=x)
        x += 1
    for j in range(nb_couleurs):
        def fonction_lambda(z = couleurs[j]):
            Jeu(z, ligne, colonne, intervalleY, intervalleX)
        LISTE_BOUTTONS[j].configure(text="●", font=("Helvetica", "8"), bg=couleurs[j], command=fonction_lambda)


# Création fonction un joueur #

def unJoueur(couleurs, ligne, colonne, intervalleY, intervalleX, recuperation):
    '''Permet de démarrer le jeu à 1 joueur'''
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global LISTE_CODE
    global CERCLE
    global PIONS_BP
    global PIONS_MP
    global JOUEURS
    global Dict_couleurs
    global LISTE_BOUTTONS

    JOUEURS = 1

    mode_un_joueur.destroy()
    mode_deux_joueurs.destroy()
   
    # Création du jeu #
    retour.config(text="←", font=("Helvetica", "8"), bg="papaya whip", command=lambda: Retour(colonne))
    retour.place_configure(x=10, y=5)
    menu.config(text="MENU", font=("Helvetica", "8"), bg="papaya whip", command=Menu)
    menu.place_configure(x=40, y=5)

    PIONS_BP = [[0]*4 for x in range(ligne)]
    PIONS_MP = [[0]*4 for x in range(ligne)]
    CERCLE = [[0]*colonne for x in range(ligne)]
       
    a = 0
    for i in range(colonne):
        a = rd.randint(0, len(couleurs)-1)
        LISTE_CODE.append(couleurs[a])

    for j in range(colonne):
        Dict_couleurs[LISTE_CODE[j]] = LISTE_CODE.count(LISTE_CODE[j])

    # Création de la grille #
    x1, y1 = 10, 50
    x2 = x1+intervalleX
    y2 = y1+intervalleY
    for k in range(ligne):
        for l in range(colonne):
            canvas.create_rectangle(x1,y1, x2,y2, fill="saddle brown")
            x1, x2 = x2, x2+intervalleX
        y1, y2 = y2, y2+intervalleY
        x1 = 10
        x2 = x1+intervalleX

    for m in range(ligne):
        canvas.create_rectangle(290, 50+(intervalleY*(m)), 360, 50+(intervalleY*(m+1)))
    
    Recuperation(recuperation, ligne, colonne, intervalleY, intervalleX)

    # Création des boûtons
    nb_couleurs = len(couleurs)
    b = 0
    for n in range(nb_couleurs):
        LISTE_BOUTTONS[n].grid_configure(row=8, column=b)
        b += 1
    for o in range(nb_couleurs):
        def fonction_lambda(a=couleurs[o]):
            Jeu(a, ligne, colonne, intervalleY, intervalleX)
        LISTE_BOUTTONS[o].configure(text="●", font=("Helvetica", "8"), bg=couleurs[o], command=fonction_lambda)
    

# Création de la pré-partie #

def Partie_personnalise(liste_couleurs):

    CHARGER_PARTIE.destroy()
    PARTIE_PERSONNALISE.destroy()

    ligne = int(input("Combien d'essais (entre 3 et 15)"))
    while ligne<3 or ligne>15:
        ligne = int(input("Combien d'essais (entre 3 et 15)"))
    colonne = int(input("Longueur du colonne (entre 2 et 6)"))
    while colonne<2 or colonne>6:
        colonne = int(input("Combien d'essais (entre 2 et 6)"))
    nb_couleurs = int(input("Nombre de couleurs (entre 2 et 10)"))
    while nb_couleurs<2 or nb_couleurs>10:
        nb_couleurs = int(input("Nombre de couleurs (entre 2 et 10)"))

    couleurs = liste_couleurs[:nb_couleurs]
    intervalleX = 280/colonne
    intervalleY = 480/ligne

    if JOUEURS == 1:
        unJoueur(couleurs, ligne, colonne, intervalleY, intervalleX, RECUPERATION)
    elif JOUEURS == 2:
        deuxJoueurs(couleurs, ligne, colonne, intervalleY, intervalleX, RECUPERATION)
    else:
        mode_un_joueur.config(text="1 JOUEUR", command=lambda : unJoueur(couleurs, ligne, colonne, intervalleY, intervalleX, RECUPERATION), font=("Helvetica", "16"), bg="brown")
        mode_un_joueur.grid(row=2, column=5)
        mode_deux_joueurs.config(text="2 JOUEURS", command=lambda : deuxJoueurs(couleurs, ligne, colonne, intervalleY, intervalleX, RECUPERATION), font=("Helvetica", "16"), bg="brown")
        mode_deux_joueurs.grid(row=6, column=5)
    
    return ligne, colonne, couleurs, intervalleY, intervalleX

# Charger la partie précédente #

def Charger():
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global Dict_liste_jeu
    global RECUPERATION
    global JOUEURS

    RECUPERATION = 1

    # Récupération des données #
    fichier = open("./sauvegarde.py")
    data = fichier.read()
    fichier.close()
    Dict_liste_jeu = loads(data)
    print(Dict_liste_jeu)

    JOUEURS = Dict_liste_jeu["Joueurs"]

    if Dict_liste_jeu["Mode"] == "Tres facile":
        LISTE_JEU = Dict_liste_jeu["Tres facile"][0]
        LISTE_JEU_COMPLET = Dict_liste_jeu["Tres facile"][1]
        tresFacile()
    elif Dict_liste_jeu["Mode"] == "Facile":
        LISTE_JEU = Dict_liste_jeu["Facile"][0]
        LISTE_JEU_COMPLET = Dict_liste_jeu["Facile"][1]
        Facile()
    elif Dict_liste_jeu["Mode"] == "Classique":
        LISTE_JEU = Dict_liste_jeu["Classique"][0]
        LISTE_JEU_COMPLET = Dict_liste_jeu["Classique"][1]
        Classique()
    else:
        LISTE_JEU = Dict_liste_jeu["IMPOSSIBLE"][0]
        LISTE_JEU_COMPLET = Dict_liste_jeu["IMPOSSIBLE"][1]
        IMPOSSIBLE()



# Création du menu #

def Accueil(liste_couleurs):
    global test
    global PARTIE_PERSONNALISE
    global CHARGER_PARTIE
    global mode_un_joueur
    global mode_deux_joueurs
    global retour
    global menu
    global code
    global sauvegarder
    global sauvegarder_oui
    global sauvegarder_non

    if test > 0:
        mode_un_joueur = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
        mode_un_joueur.place(x=1000, y=0)
        mode_deux_joueurs = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
        mode_deux_joueurs.place(x=1000, y=0)

        retour = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
        retour.place(x=1000, y=0)

        menu = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
        menu.place(x=1000, y=0)

        sauvegarder_oui = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
        sauvegarder_oui.place(x=1000, y=0)

        sauvegarder_non = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
        sauvegarder_non.place(x=1000, y=0)

        sauvegarder = tk.Label(text="", font=("Helvetica", "1"), bg="papaya whip")
        sauvegarder.place(x=1000, y=0)

        code = tk.Label(text="", font=("Helvetica", "1"), bg="papaya whip")
        code.grid(row=0, column=5)

        gagne = tk.Label(text="", font=("Helvetica", "1"), bg="papaya whip")
        gagne.place(x=390, y=300)

        perdu = tk.Label(text="", font=("Helvetica", "1"), bg="papaya whip")
        perdu.place(x=390, y=300)

        CHARGER_PARTIE = tk.Button(fenetre)
        CHARGER_PARTIE.grid(row=0, column=5)
        PARTIE_PERSONNALISE = tk.Button(fenetre)
        PARTIE_PERSONNALISE.grid(row=7, column=5)

        for i in range(8):
            LISTE_BOUTTONS[i] = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
            LISTE_BOUTTONS[i].place(x=1000, y=0)

        for j in range(12):
            for k in range(4):
                PIONS_BP[j][k] = canvas.create_oval((0,0),(1,1), fill="papaya whip")

        for l in range(12):
            for m in range(4):
                PIONS_MP[l][m] = canvas.create_oval((0,0),(1,1), fill="papaya whip")
     
    CHARGER_PARTIE.config(text="Charger partie précédente", command=Charger, font=("Helvetica", "8"), bg="brown")
    PARTIE_PERSONNALISE.config(text="Partie personnalisée", command=lambda : Partie_personnalise(liste_couleurs), font=("Helvetica", "8"), bg="brown")





Accueil(LISTE_COULEURS)
fenetre.mainloop()
