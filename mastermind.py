import tkinter as tk
import random as rd
from json import *

   ###############################################################################################
 #                                                                                                 #
#   Mastermind   :    Gaël FERREIRA RODRIGUEZ / Elise MOULIN / César PITIGLIANO / Noël-Marie N'dri  #
 #                                                                                                 #
   ###############################################################################################


# Initialisation des variables #

Dict_liste_jeu = {
    "Liste du jeu 2D":[[]],
    "Liste du jeu complet":[],
    "Liste code":[], "ligne":0,
    "colonne":0,
    "Nombre de couleurs":0,
    "Joueurs":"",
    "Fin de partie":0
    }
Dict_couleurs = {'black':0,'green':0, 'blue':0, 'purple':0, 'yellow':0, 'orange':0, 'pink':0, 'cyan':0, 'grey':0, 'darkblue':0}
LISTE_COULEURS = ['black', 'green', 'blue', 'purple', 'yellow', 'orange', 'pink', 'cyan', 'grey', 'darkblue']
LISTE_JEU = [[]]
LISTE_JEU_COMPLET = []
LISTE_CODE = []
CERCLE = [[]]
CERCLE2 = [[]]
PIONS_BP = [[]]
PIONS_MP = [[]]
LISTE_BOUTTONS = [0]*15
JOUEURS = 0
FIN_DE_PARTIE = 0



# Initialisation de la fenêtre #

HEIGHT = 600
WIDTH = 600
fenetre = tk.Tk()
fenetre.title("Mastermind")
canvas = tk.Canvas(fenetre, height=HEIGHT, width=WIDTH, bg='black')
canvas.grid(row=0, column=0, rowspan=9, columnspan=11)



# Initialisation des boûtons et des labels pour une suppression future possible #

mode_un_joueur = tk.Button(fenetre)
mode_un_joueur.place(x=1000, y=0)
mode_deux_joueurs = tk.Button(fenetre)
mode_deux_joueurs.place(x=1000, y=0)
retour = tk.Button(fenetre)
retour.place(x=1000, y=0)
menu = tk.Button(fenetre)
menu.place(x=1000, y=0)
sauvegarder_oui = tk.Button(fenetre)
sauvegarder_oui.place(x=1000, y=0)
sauvegarder_non = tk.Button(fenetre)
sauvegarder_non.place(x=1000, y=0)
sauvegarder = tk.Label(fenetre)
sauvegarder.place(x=1000, y=0)
help = tk.Button(fenetre)
help.place(x=1000, y=0)
gagne = tk.Label(fenetre)
gagne.place(x=1000, y=0)
perdu = tk.Label(fenetre)
perdu.place(x=1000, y=0)

CHARGER_PARTIE = tk.Button(fenetre)
CHARGER_PARTIE.grid(row=2, column=5)
PARTIE = tk.Button(fenetre)
PARTIE.grid(row=6, column=5)

for i in range(15):
    LISTE_BOUTTONS[i] = tk.Button(fenetre)
    LISTE_BOUTTONS[i].place(x=1000, y=0)



def fonctionNull():
    ''' Fonction qui a pour but de ne rien faire '''
    pass



def Victoire():
    '''Détruis les boutons et affiche que le joueur a gagné'''
    global LISTE_BOUTTONS, FIN_DE_PARTIE

    if FIN_DE_PARTIE > 0:
        retour.destroy()
        help.destroy()
        gagne.config(text="Vous avez gagné !", font=("Calibri", "14"), bg="black", fg="white")
        gagne.place_configure(x=420, y=300)
    else:
        for i in range(15):
            LISTE_BOUTTONS[i].destroy()
        retour.destroy()
        help.destroy()
        gagne.config(text="Vous avez gagné !", font=("Calibri", "14"), bg="black", fg="white")
        gagne.place_configure(x=420, y=300)
    FIN_DE_PARTIE += 1
    



def Defaite():
    '''Détruis les boutons et affiche que le joueur a perdu'''
    global LISTE_BOUTTONS, FIN_DE_PARTIE

    if FIN_DE_PARTIE > 0:
        retour.destroy()
        help.destroy()
        perdu.config(text="Vous avez perdu !", font=("Calibri", "14"), bg="black", fg="white")
        perdu.place_configure(x=420, y=300)
    else:
        for i in range(15):
            LISTE_BOUTTONS[i].destroy()
        retour.destroy()
        help.destroy()
        perdu.config(text="Vous avez perdu !", font=("Calibri", "14"), bg="black", fg="white")
        perdu.place_configure(x=420, y=300)
    FIN_DE_PARTIE += 1


def Sauvegarde(ligne, colonne, nb_couleurs):
    ''' Sauvegarde la partie en cours '''
    global LISTE_JEU, LISTE_JEU_COMPLET, LISTE_CODE, JOUEURS, FIN_DE_PARTIE

    sauvegarder.destroy()
    sauvegarder_oui.destroy()
    sauvegarder_non.destroy()

    Dict_liste_jeu["Liste du jeu 2D"] = LISTE_JEU
    Dict_liste_jeu["Liste du jeu complet"] = LISTE_JEU_COMPLET
    Dict_liste_jeu["Liste code"] = LISTE_CODE
    Dict_liste_jeu["Joueurs"] = JOUEURS
    Dict_liste_jeu["ligne"] = ligne
    Dict_liste_jeu["colonne"] = colonne
    Dict_liste_jeu["Nombre de couleurs"] = nb_couleurs
    Dict_liste_jeu["Fin de partie"] = FIN_DE_PARTIE

    fichier = open("./sauvegarde.py", "w")
    dump(Dict_liste_jeu, fichier, indent=1)
    fichier.close()

    LISTE_JEU = [[]]
    LISTE_JEU_COMPLET = []
    LISTE_CODE = []
    JOUEURS = 0
    FIN_DE_PARTIE = 0

    Accueil(LISTE_COULEURS, repetition = 1)



def PasdeSauvegarde():
    ''' Ne sauvegarde pas la partie en cours '''
    global LISTE_JEU, LISTE_JEU_COMPLET, LISTE_CODE, JOUEURS, FIN_DE_PARTIE

    sauvegarder.destroy()
    sauvegarder_oui.destroy()
    sauvegarder_non.destroy()

    LISTE_JEU = [[]]
    LISTE_JEU_COMPLET = []
    LISTE_CODE = []
    FIN_DE_PARTIE = 0
    JOUEURS = 0

    Accueil(LISTE_COULEURS, repetition = 1)



def Menu(ligne, colonne, nb_couleurs):
    '''Sauvegarde la partie si elle est en cours et relance le programme'''
    global LISTE_BOUTTONS

    for i in range(nb_couleurs):
        LISTE_BOUTTONS[i].destroy()
    menu.destroy()
    retour.destroy()
    gagne.destroy()
    perdu.destroy()
    help.destroy()
    canvas.delete("all")

    sauvegarder.config(text="Souhaitez-vous sauvegarder ?", font=("Calibri", "18"), bg="black", fg="snow", \
                       cursor="cross", activebackground="black", activeforeground="white", border=3)
    sauvegarder.grid_configure(row=3, column=5)
    sauvegarder_oui.config(text="Oui", font=("Calibri", "16"), bg="snow", command=lambda : Sauvegarde(ligne, colonne, nb_couleurs), \
                           cursor="cross", activebackground="black", activeforeground="white", border=3)
    sauvegarder_oui.grid_configure(row=5, column=4)
    sauvegarder_non.config(text="Non", font=("Calibri", "16"), bg="snow", command=PasdeSauvegarde, \
                           cursor="cross", activebackground="black", activeforeground="white", border=3)
    sauvegarder_non.grid_configure(row=5, column=6)



def Retour(colonne_total):
    '''Permet un retour en arrière (essais en plus) lors du jeu'''
    global LISTE_JEU_COMPLET, LISTE_JEU, CERCLE, CERCLE2, PIONS_BP, PIONS_MP

    colonne = len(LISTE_JEU_COMPLET) % colonne_total
    ligne = int(len(LISTE_JEU_COMPLET) // colonne_total)

    if LISTE_JEU_COMPLET != []:
        if colonne == 0:
            for i in range(colonne_total):
                canvas.delete(CERCLE[ligne-1][i])
                canvas.delete(CERCLE2[ligne-1][i])
                canvas.delete(PIONS_BP[ligne-1][i])
                canvas.delete(PIONS_MP[ligne-1][i])
                LISTE_JEU[ligne-1].pop()
                LISTE_JEU_COMPLET.pop()     
        else:
            for j in range(colonne):
                canvas.delete(CERCLE[ligne][j])
                canvas.delete(CERCLE2[ligne][j])
                canvas.delete(PIONS_BP[ligne][j])
                canvas.delete(PIONS_MP[ligne][j])    
                LISTE_JEU[ligne].pop()
                LISTE_JEU_COMPLET.pop()



def creation_cercle2(liste_aide, ligne):
    ''' Créée des cercles de couleurs dans la grille d'aide '''
    global CERCLE2

    intervalleX = 175 / len(liste_aide)
    intervalleY = 110 / len(liste_aide)
    y1, y2 = 65 + (intervalleY/2 - 10), 65 + (intervalleY/2 + 10)
    for i in range(len(liste_aide)):
        x1 = 400 + (intervalleX/2 - 10) + (intervalleX)*(i)
        x2 = 400 + (intervalleX/2 + 10) + (intervalleX)*(i)
        CERCLE2[ligne][i] = canvas.create_oval(x1, y1, x2, y2, fill=liste_aide[i])  



def Help(pionsBP, pionsMP, liste_jeu, liste_couleurs, ligne):
    ''' Créée une suite de couleurs compatible avec l'essai précédent '''
    liste_aide = [0]*len(liste_jeu)
    numero_couleur = 0
    numero_couleur2 = 0

    for i in range(pionsBP):
        numero_couleur = rd.randint(0, len(liste_jeu)-1)
        while liste_aide[numero_couleur] != 0:
            numero_couleur = rd.randint(0, len(liste_jeu)-1)
        liste_aide[numero_couleur] = liste_jeu[numero_couleur]

    for j in range(pionsMP):
        numero_couleur = rd.randint(0, len(liste_jeu)-1)
        numero_couleur2 = rd.randint(0, len(liste_jeu)-1)
        while (liste_aide[numero_couleur] != 0) or (liste_aide[numero_couleur2] != 0) or (numero_couleur == numero_couleur2):
            numero_couleur = rd.randint(0, len(liste_jeu)-1)
            numero_couleur2 = rd.randint(0, len(liste_jeu)-1)
        liste_aide[numero_couleur2] = liste_jeu[numero_couleur]

    for k in range(len(liste_jeu)):
        numero_couleur = rd.randint(0, len(liste_couleurs)-1)
        if liste_aide[k] == 0:
            liste_aide[k] = liste_couleurs[numero_couleur]

    creation_cercle2(liste_aide, ligne)
    help.config(command=fonctionNull)



def bienPlace(n, ligne, intervalleY):
    '''Compte les pions bien plaçés et les affiches'''
    global PIONS_BP
    x1, x2 = 300, 310
    y1 = 50 + (intervalleY/4 - 5) + (intervalleY)*(ligne)
    y2 = 50 + (intervalleY/4 + 5) + (intervalleY)*(ligne)
    for i in range(n):
        PIONS_BP[ligne][i] = canvas.create_oval((x1,y1),(x2,y2), fill="red")
        x1, x2 = x1+15, x2+15



def malPlace(n, ligne, intervalleY):
    '''Compte les pions mal plaçés et les affiches'''
    global PIONS_MP
    x1, x2 = 300, 310
    y1 = 50 + (intervalleY*(3/4) - 5) + (intervalleY)*(ligne)
    y2 = 50 + (intervalleY*(3/4) + 5) + (intervalleY)*(ligne)
    for i in range(n):
        PIONS_MP[ligne][i] = canvas.create_oval((x1,y1),(x2,y2), fill="white")
        x1, x2 = x1+15, x2+15



def verification_post_jeu(ligne, ligne_total, colonne_total, intervalleY):
    ''' Vérifie si le joueurs a gagné ou perdu '''
    global LISTE_JEU, LISTE_CODE, Dict_couleurs

    if ligne+1 >= ligne_total:
        Defaite()
        return "fin"
    else:
        if LISTE_JEU[ligne] == LISTE_CODE:
            Victoire()
            return "fin"
        else:
            bien_place = 0
            mal_place = 0
            for i in range(colonne_total):
                Dict_couleurs[LISTE_CODE[i]] = LISTE_CODE.count(LISTE_CODE[i])
            for j in range(colonne_total):
                Dict_couleurs[LISTE_JEU[ligne][j]] -= 1
                if Dict_couleurs[LISTE_JEU[ligne][j]] >= 0:
                    if (LISTE_JEU[ligne][j] == LISTE_CODE[j]):
                        bien_place += 1
                    elif (LISTE_JEU[ligne][j] in LISTE_CODE) and (LISTE_JEU[ligne][j] != LISTE_CODE[j]):
                        mal_place += 1
                elif Dict_couleurs[LISTE_JEU[ligne][j]] < 0 and (LISTE_JEU[ligne][j] == LISTE_CODE[j]):
                    bien_place += 1
                    mal_place -= 1
            bienPlace(bien_place, ligne, intervalleY)
            malPlace(mal_place, ligne, intervalleY)



def creation_cercle(ligne, colonne, intervalleY, intervalleX, couleur):
    ''' Créée des cercles de couleurs dans la grille principale '''
    global CERCLE

    x1 = 10 + (intervalleX/2 - 10) + (intervalleX)*(colonne)
    x2 = 10 + (intervalleX/2 + 10) + (intervalleX)*(colonne)
    y1 = 50 + (intervalleY/2 - 10) + (intervalleY)*(ligne)
    y2 = 50 + (intervalleY/2 + 10) + (intervalleY)*(ligne)  
    CERCLE[ligne][colonne] = canvas.create_oval(x1, y1, x2, y2, fill=couleur)  



def Jeu(couleur, ligne_total, colonne_total, intervalleY, intervalleX, liste_couleurs):
    ''' Permet d'afficher les actions exerçées par le joueurs '''
    global LISTE_JEU_COMPLET, LISTE_JEU, LISTE_CODE, CERCLE, PIONS_BP, PIONS_MP, Dict_couleurs

    help.config(command=fonctionNull)

    LISTE_JEU_COMPLET.append(couleur)
    colonne = len(LISTE_JEU_COMPLET) % colonne_total
    ligne = int(len(LISTE_JEU_COMPLET) // colonne_total)
    Ligne = 0
    Colonne = 0

    if colonne == 1:
        LISTE_JEU.append([])
        LISTE_JEU[ligne].append(couleur)
        Colonne = 0
        creation_cercle(ligne, Colonne, intervalleY, intervalleX, couleur)
    elif colonne != 0:
        LISTE_JEU[ligne].append(couleur)
        Colonne = colonne-1
        creation_cercle(ligne, Colonne, intervalleY, intervalleX, couleur)
    else :
        LISTE_JEU[ligne-1].append(couleur)
        Colonne = colonne_total-1
        Ligne = ligne-1
        # print(LISTE_CODE, LISTE_JEU) # TEST
        creation_cercle(Ligne, Colonne, intervalleY, intervalleX, couleur)
        verification_post_jeu(Ligne, ligne_total, colonne_total, intervalleY)
        if not verification_post_jeu(Ligne, ligne_total, colonne_total, intervalleY) == "fin":
            pionsBP = len(PIONS_BP[Ligne]) - PIONS_BP[Ligne].count(0)
            pionsMP = len(PIONS_MP[Ligne]) - PIONS_MP[Ligne].count(0)
            help.config(command=lambda : Help(pionsBP, pionsMP, LISTE_JEU[Ligne], liste_couleurs, Ligne))



def Recuperation(recuperation, ligne_total, colonne_total, intervalleY, intervalleX, liste_couleurs):
    ''' Permet de recréer la partie précédente si le joueur a décidé de charger la partie précédente '''
    global LISTE_JEU_COMPLET, LISTE_JEU, CERCLE, LISTE_CODE, Dict_couleurs, Dict_liste_jeu

    Colonne = 0
    Ligne = 0

    if recuperation is True:
        LISTE_CODE = Dict_liste_jeu["Liste code"]
        for i in range(len(LISTE_JEU_COMPLET)):
            colonne = (i+1) % colonne_total
            ligne = int((i+1) // colonne_total)
            if colonne == 1:
                Colonne = 0
                creation_cercle(ligne, Colonne, intervalleY, intervalleX, LISTE_JEU_COMPLET[i])
            elif colonne != 0:
                Colonne = colonne-1
                creation_cercle(ligne, Colonne, intervalleY, intervalleX, LISTE_JEU_COMPLET[i]) 
            else :
                Colonne = colonne_total-1
                Ligne = ligne-1
                creation_cercle(Ligne, Colonne, intervalleY, intervalleX, LISTE_JEU_COMPLET[i]) 
                verification_post_jeu(Ligne, ligne_total, colonne_total, intervalleY)
                if not verification_post_jeu(Ligne, ligne_total, colonne_total, intervalleY) == "fin":
                    pionsBP = len(PIONS_BP[Ligne]) - PIONS_BP[Ligne].count(0)
                    pionsMP = len(PIONS_MP[Ligne]) - PIONS_BP[Ligne].count(0)
                    help.config(command=lambda : Help(pionsBP, pionsMP, LISTE_JEU[Ligne], liste_couleurs, Ligne))




def creation_grille(x1, x2, y1, y2, ligne, colonne, intervalleY, intervalleX):
    ''' Créée une grille '''
    x_initial = x1
    for i in range(ligne):
        for j in range(colonne):
            canvas.create_rectangle(x1, y1, x2, y2, fill="saddle brown", outline="white", width=2)
            x1, x2 = x2, x2+intervalleX
        y1, y2 = y2, y2+intervalleY
        x1 = x_initial
        x2 = x1+intervalleX



def creation_code_secret(colonne, liste_couleurs, joueurs):
    ''' Créée un code secret '''
    global LISTE_CODE

    if joueurs == 1:
        a = 0 # Création du code secret
        for i in range(colonne):
            a = rd.randint(0, len(liste_couleurs)-1)
            LISTE_CODE.append(liste_couleurs[a])
    elif joueurs == 2:
        for a in range(colonne):  
            print(liste_couleurs)
            couleur_secret = str(input("Choisissez la couleur numéro "+str(a+1)+"/"+str(colonne)+ " parmi les couleurs présentes :\n"))
            while not (couleur_secret in liste_couleurs):
                print(liste_couleurs)
                couleur_secret = str(input("Choisissez la couleur numéro "+str(a+1)+"/"+str(colonne)+" parmi les couleurs présentes :\n"))
            LISTE_CODE.append(couleur_secret)



def deuxJoueurs(liste_couleurs, ligne, colonne, intervalleY, intervalleX, recuperation):
    '''Permet de démarrer le jeu à 2 joueurs'''
    global LISTE_CODE, CERCLE, CERCLE2, PIONS_BP, PIONS_MP, JOUEURS, LISTE_BOUTTONS, Dict_couleurs

    JOUEURS = 2 # Initialisation des variables 
    nb_couleurs = len(liste_couleurs)
    PIONS_BP = [[0]*colonne for x in range(ligne)]
    PIONS_MP = [[0]*colonne for x in range(ligne)]
    CERCLE = [[0]*colonne for x in range(ligne)]
    CERCLE2 = [[0]*colonne for x in range(ligne)]

    mode_un_joueur.destroy() # Initialisation des boûtons
    mode_deux_joueurs.destroy()
    menu.config(text="MENU", font=("Calibri", "12"), bg="snow", command=lambda : Menu(ligne, colonne, nb_couleurs), \
                cursor="cross", activebackground="black", activeforeground="white", border=3)
    menu.place_configure(x=40, y=5)
    retour.config(text="←", font=("Calibri", "12"), bg="snow", command=lambda : Retour(colonne), \
                  cursor="cross", activebackground="black", activeforeground="white", border=3)
    retour.place_configure(x=10, y=5)
    help.config(text="?", font=("Calibri", "12"), bg="snow", \
                cursor="cross", activebackground="black", activeforeground="white", border=3)
    help.place_configure(x=400, y=5)

    creation_code_secret(colonne, liste_couleurs, joueurs = 2) # Création du code secret

    for j in range(colonne): # Ajout des couleurs du code secret dans le dictionnaire 
        Dict_couleurs[LISTE_CODE[j]] = LISTE_CODE.count(LISTE_CODE[j])

    x2, y2 = 10+intervalleX, 50+intervalleY # Création de la grille principale
    creation_grille(10, x2, 50, y2, ligne, colonne, intervalleY, intervalleX)
    for i in range(ligne):
        canvas.create_rectangle(290, 50+(intervalleY*(i)), 390, 50+(intervalleY*(i+1)), fill="sandy brown", outline="snow", width=2)

    x1, y1, y2 = 400, 50, 110 # Création de la grille aide
    x2 = x1+ (175/colonne)
    creation_grille(x1, x2, y1, y2, 1, colonne, 0, (175/colonne))

    Recuperation(recuperation, ligne, colonne, intervalleY, intervalleX, liste_couleurs) # Création du jeu à partir des éventuelles données récupérées

    b = 0  # Création des boûtons
    for n in range(nb_couleurs):
        def fonction_lambda(a=liste_couleurs[n]):
            Jeu(a, ligne, colonne, intervalleY, intervalleX, liste_couleurs)
        LISTE_BOUTTONS[n].configure(text="●", font=("Calibri", "8"), bg=liste_couleurs[n], command=fonction_lambda)
        LISTE_BOUTTONS[n].grid_configure(row=8, column=b)
        b += 1



def unJoueur(liste_couleurs, ligne, colonne, intervalleY, intervalleX, recuperation):
    '''Permet de démarrer le jeu à 1 joueur'''
    global LISTE_CODE, CERCLE, CERCLE2, PIONS_BP, PIONS_MP, JOUEURS, LISTE_BOUTTONS, Dict_couleurs

    JOUEURS = 1 # Initialisation des variables
    nb_couleurs = len(liste_couleurs) 
    PIONS_BP = [[0]*colonne for x in range(ligne)]
    PIONS_MP = [[0]*colonne for x in range(ligne)]
    CERCLE = [[0]*colonne for x in range(ligne)]  
    CERCLE2 = [[0]*colonne for x in range(ligne)]

    mode_un_joueur.destroy() # Initialisation des boûtons
    mode_deux_joueurs.destroy()
    retour.config(text="←", font=("Calibri", "12"), bg="snow", command=lambda: Retour(colonne), \
                  cursor="cross", activebackground="black", activeforeground="white", border=3)
    retour.place_configure(x=10, y=5)
    menu.config(text="MENU", font=("Calibri", "12"), bg="snow", command=lambda : Menu(ligne, colonne, nb_couleurs), \
                cursor="cross", activebackground="black", activeforeground="white", border=3)
    menu.place_configure(x=50, y=5)
    help.config(text="?", font=("Calibri", "12"), bg="snow", \
                cursor="cross", activebackground="black", activeforeground="white", border=3)
    help.place_configure(x=400, y=5)

    creation_code_secret(colonne, liste_couleurs, joueurs = 1) # Création du code secret

    for j in range(colonne): # Ajout des couleurs du code secret dans le dictionnaire 
        Dict_couleurs[LISTE_CODE[j]] = LISTE_CODE.count(LISTE_CODE[j])

    x2, y2 = 10+intervalleX, 50+intervalleY # Création de la grille principale
    creation_grille(10, x2, 50, y2, ligne, colonne, intervalleY, intervalleX)
    for m in range(ligne):
        canvas.create_rectangle(290, 50+(intervalleY*(m)), 390, 50+(intervalleY*(m+1)), fill="sandy brown", outline="snow", width=2)

    x1, y1, y2 = 400, 50, 110 # Création de la grille aide
    x2 = x1+ (175/colonne)
    creation_grille(x1, x2, y1, y2, 1, colonne, 0, (175/colonne))

    Recuperation(recuperation, ligne, colonne, intervalleY, intervalleX, liste_couleurs) # Création du jeu à partir des éventuelles données récupérées

    b = 0  # Création des boûtons
    for n in range(nb_couleurs):
        def fonction_lambda(a=liste_couleurs[n]):
            Jeu(a, ligne, colonne, intervalleY, intervalleX, liste_couleurs)
        LISTE_BOUTTONS[n].config(text="●", font=("Calibri", "8"), bg=liste_couleurs[n], command=fonction_lambda)
        LISTE_BOUTTONS[n].grid(row=8, column=b)
        b += 1



### Inspiré de https://pynative.com/python-check-user-input-is-number-or-string/ ###
def vérifEntrees(valeur):
    try:
        int(valeur)
        condition = True
    except ValueError:
        condition = False
    return condition



def Partie(liste_couleurs, ligne, colonne):
    ''' Permet de choisir les différents paramètres de la partie'''
    global JOUEURS

    CHARGER_PARTIE.destroy()
    PARTIE.destroy()

    if JOUEURS == 1: 
        intervalleX = 280/colonne
        intervalleY = 480/ligne
        unJoueur(liste_couleurs, ligne, colonne, intervalleY, intervalleX, True)
    elif JOUEURS == 2:
        intervalleX = 280/colonne
        intervalleY = 480/ligne
        deuxJoueurs(liste_couleurs, ligne, colonne, intervalleY, intervalleX, True)
    else:
        mode_classique = input("Voulez-vous faire une partie en mode classique ? (taper 'oui' ou n'importe quoi d'autre)\n")
        if mode_classique == "oui":
            Ligne, Colonne, nb_couleurs = 12, 4, 8
        else:
            ligne1 = input("Combien d'essais (entre 3 et 15)")
            while (vérifEntrees(ligne1) is False) or (not 3<=int(ligne1)<=15):
                ligne1 = input("Combien d'essais (un chiffre entre 3 et 15)")
            colonne1 = input("Longueur du colonne (entre 2 et 6)")
            while (vérifEntrees(colonne1) is False) or (not 2<=int(colonne1)<=6):
                colonne1 = input("Combien d'essais (un chiffre entre 2 et 6)")
            nb_couleurs1 = input("Nombre de couleurs (entre 2 et 10)")
            while (vérifEntrees(nb_couleurs1) is False) or (not 2<=int(nb_couleurs1)<=10):
                nb_couleurs1 = input("Nombre de couleurs (un chiffre entre 2 et 10)")

            Ligne, Colonne, nb_couleurs = int(ligne1), int(colonne1), int(nb_couleurs1)

        couleurs = liste_couleurs[:nb_couleurs]
        intervalleX = 280/Colonne
        intervalleY = 480/Ligne

        mode_un_joueur.config(text="1 JOUEUR", command=lambda : unJoueur(couleurs, Ligne, Colonne, intervalleY, intervalleX, False), \
                              font=("Calibri", "16"), bg="snow", cursor="cross", activebackground="black", activeforeground="white", border=8)
        mode_un_joueur.grid(row=2, column=5)
        mode_deux_joueurs.config(text="2 JOUEURS", command=lambda : deuxJoueurs(couleurs, Ligne, Colonne, intervalleY, intervalleX, False), \
                                 font=("Calibri", "16"), bg="snow", cursor="cross", activebackground="black", activeforeground="white", border=8)
        mode_deux_joueurs.grid(row=6, column=5)



def Charger(liste_couleurs):
    ''' Permet de charger la partie précédente si celle-ci a été sauvegardée '''
    global LISTE_JEU, LISTE_JEU_COMPLET, JOUEURS, FIN_DE_PARTIE, Dict_liste_jeu

    fichier = open("./sauvegarde.py")  # Récupération des données 
    data = fichier.read()
    fichier.close()
    Dict_liste_jeu = loads(data)

    JOUEURS = Dict_liste_jeu["Joueurs"]  # Modification des variables
    LISTE_JEU = Dict_liste_jeu["Liste du jeu 2D"]
    LISTE_JEU_COMPLET = Dict_liste_jeu["Liste du jeu complet"]
    FIN_DE_PARTIE = Dict_liste_jeu["Fin de partie"]
    ligne = Dict_liste_jeu["ligne"]
    colonne = Dict_liste_jeu["colonne"]
    nb_couleurs = Dict_liste_jeu["Nombre de couleurs"]
    nv_liste_couleurs = liste_couleurs[:nb_couleurs]

    Partie(nv_liste_couleurs, ligne, colonne)  # Lancement de la partie avec les variables modifiées



def Accueil(liste_couleurs, repetition):
    ''' Permet de créer le menu '''
    global PARTIE, CHARGER_PARTIE, LISTE_BOUTTONS
    global mode_un_joueur, mode_deux_joueurs, retour, menu, help, sauvegarder, sauvegarder_oui, sauvegarder_non, gagne, perdu

    if repetition == 1:  # Si la fenêtre est lancée une deuxième fois, reinitialisé tous les boutons et "label"
        mode_un_joueur = tk.Button(fenetre)
        mode_un_joueur.place(x=1000, y=0)
        mode_deux_joueurs = tk.Button(fenetre)
        mode_deux_joueurs.place(x=1000, y=0)
        retour = tk.Button(fenetre)
        retour.place(x=1000, y=0)
        menu = tk.Button(fenetre)
        menu.place(x=1000, y=0)
        sauvegarder_oui = tk.Button(fenetre)
        sauvegarder_oui.place(x=1000, y=0)
        sauvegarder_non = tk.Button(fenetre)
        sauvegarder_non.place(x=1000, y=0)
        sauvegarder = tk.Label(fenetre)
        sauvegarder.place(x=1000, y=0)
        help = tk.Button(fenetre)
        help.place(x=1000, y=0)
        gagne = tk.Label(fenetre)
        gagne.place(x=1000, y=0)
        perdu = tk.Label(fenetre)
        perdu.place(x=1000, y=0)

        CHARGER_PARTIE = tk.Button(fenetre)
        CHARGER_PARTIE.grid(row=2, column=5)
        PARTIE = tk.Button(fenetre)
        PARTIE.grid(row=6, column=5)

        for i in range(15):
            LISTE_BOUTTONS[i] = tk.Button(fenetre)
            LISTE_BOUTTONS[i].place(x=1000, y=0)

    CHARGER_PARTIE.config(text="Charger partie précédente", command=lambda : Charger(liste_couleurs), font=("Calibri", "16"), bg="snow", \
                          cursor="cross", activebackground="black", activeforeground="white", border=8)
    PARTIE.config(text="Partie", command=lambda : Partie(liste_couleurs, 0, 0), font=("Calibri", "16"), bg="snow", \
                  cursor="cross", activebackground="black", activeforeground="white", border=8)


Accueil(LISTE_COULEURS, repetition = 0) # Initialise le menu
fenetre.mainloop() # Initialise la fenêtre