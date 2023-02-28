import tkinter as tk
import random as rd

####################################################################################################################
#                                                                                                                  #
#   Mastermind   :    Gaël FERREIRA RODRIGUEZ  /     /      /                                                      #
#                                                                                                                  #
####################################################################################################################




# Conditions initiales #

MODE = " "
NB_ESSAIS = 0
INTERVALLE_Y = 0 # intervalle nécessaire entre les différentes lignes de la grille
INTERVALLE_X = 0 # intervalle nécessaire entre les différentes colonnes de la grille
CODE = 0

LISTE_JEU = [[]]
LISTE_JEU_COMPLET = []
LISTE_COULEURS = []
LISTE_BOUTTONS = [0]*10
LISTE_BOUTTONS2 = [0]*10
LISTE_CODE = []
CERCLE = [[]]
CERCLE2 = []


# Création de la fenêtre #

HEIGHT = 600
WIDTH = 600
fenetre = tk.Tk()
fenetre.title("Mastermind")
canvas = tk.Canvas(fenetre, height=HEIGHT, width=WIDTH, bg='papaya whip')
canvas.grid(row=0, column=0, rowspan=9, columnspan=10)




# Création des bouttons initiales #

mode_un_joueur = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
mode_un_joueur.place(x=5, y=5)
mode_deux_joueurs = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
mode_deux_joueurs.place(x=6, y=5)

retour = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
retour.place(x=10, y=5)

menu = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
menu.place(x=40, y=5)

code = tk.Label(text="", font=("Helvetica", "1"), bg="papaya whip")
code.grid(row=0, column=4, columnspan=2)


x=0
for i in range(10):
    LISTE_BOUTTONS[i] = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
    LISTE_BOUTTONS[i].grid(row=8, column=x)
    x += 1



# Canvas victoire #

def Victoire():
    '''Détruis les boutons et affiche que le joueur a gagné(e)'''
    global NB_ESSAIS
    global LISTE_BOUTTONS
    global LISTE_COULEURS
    for i in range(10):
        LISTE_BOUTTONS[i].destroy()
    Gagne = tk.Label(text="Vous avez gagné!", font=("Helvetica", "18"), bg="papaya whip").place(x=320, y=300)
    



# Canvas défaite #

def Defaite():
    '''Détruis les boutons et affiche que le joueur a perdu(e)'''
    global NB_ESSAIS
    global LISTE_BOUTTONS
    global LISTE_COULEURS
    for i in range(10):
        LISTE_BOUTTONS[i].destroy()
    Defaite = tk.Label(text="Vous avez perdu!", font=("Helvetica", "8"),).place(x=320, y=300)
   



# Boutton Menu #

def Menu():
    '''Sauvegarde la partie si elle est en cours et relance le programme'''
    



# Boutton retour #

def Retour():
    '''Permet un retour en arrière (essais en plus) lors du jeu'''
    global LISTE_JEU_COMPLET
    global LISTE_JEU
    global CERCLE
    global CODE
    colonne = len(LISTE_JEU_COMPLET) % CODE
    ligne = int(len(LISTE_JEU_COMPLET) // CODE)

    if LISTE_JEU_COMPLET != []:
        if colonne == 0:
            for i in range(CODE):
                canvas.delete(CERCLE[ligne-1][i])
                LISTE_JEU[ligne-1].pop()
                LISTE_JEU_COMPLET.pop()
                canvas.delete("bienPlacé")
                canvas.delete("malPlacé")
        else:
            for j in range(colonne):
                canvas.delete(CERCLE[ligne][j])
                LISTE_JEU[ligne].pop()
                LISTE_JEU_COMPLET.pop()
                canvas.delete("bienPlacé")
                canvas.delete("malPlacé")       



# Création des pions bien plaçés et mal plaçés #

def bienPlace(n):
    '''Compte les pions bien plaçés et les affiches'''
    x1, x2, y1, y2 = 300, 320, 50, 70
    for i in range(n):
        canvas.create_oval((x1,y1),(x2,y2), fill="red", tags="bienPlacé")
        x1, x2 = x1+40, x2+40

def malPlace(n):
    '''Compte les pions mal plaçés et les affiches'''
    x1, x2, y1, y2 = 300, 320, 90, 110
    for i in range(n):
        canvas.create_oval((x1,y1),(x2,y2), fill="white", tags="malPlacé")
        x1, x2 = x1+40, x2+40



# Création partie interactive #

def Jeu(couleur):
    '''Permet d'afficher les actions exerçés par le joueur et vérifie si le joueur à gagné(e) ou perdu(e)'''
    global NB_ESSAIS
    global LISTE_JEU_COMPLET
    global LISTE_JEU
    global CERCLE
    global CODE
    global INTERVALLE_X
    global INTERVALLE_Y
    global LISTE_CODE
    LISTE_JEU_COMPLET.append(couleur)
    colonne = len(LISTE_JEU_COMPLET) % CODE
    ligne = int(len(LISTE_JEU_COMPLET) // CODE)
    
    if ligne > NB_ESSAIS:
        Defaite()
    else:
        if colonne == 1:
            LISTE_JEU.append([])
            LISTE_JEU[ligne].append(couleur)
            x1 = 10 + (INTERVALLE_X/2 - 10)
            x2 = 10 + (INTERVALLE_X/2 + 10)
            y1 = 50 + (INTERVALLE_Y/2 - 10) + (INTERVALLE_Y)*(ligne)
            y2 = 50 + (INTERVALLE_Y/2 + 10) + (INTERVALLE_Y)*(ligne)
            CERCLE[ligne][0] = canvas.create_oval(x1, y1, x2, y2, fill=couleur)
        elif colonne != 0:
            LISTE_JEU[ligne].append(couleur)
            x1 = 10 + (INTERVALLE_X/2 - 10) + (INTERVALLE_X)*(colonne-1)
            x2 = 10 + (INTERVALLE_X/2 + 10) + (INTERVALLE_X)*(colonne-1)
            y1 = 50 + (INTERVALLE_Y/2 - 10) + (INTERVALLE_Y)*(ligne)
            y2 = 50 + (INTERVALLE_Y/2 + 10) + (INTERVALLE_Y)*(ligne)
            CERCLE[ligne][colonne-1] = canvas.create_oval(x1, y1, x2, y2, fill=couleur)
        
        else :
            colonne = CODE - 1
            LISTE_JEU[ligne-1].append(couleur)
            # test #
            print(LISTE_JEU[ligne-1], LISTE_CODE, LISTE_JEU)
            # test #
            x1 = 10 + (INTERVALLE_X/2 - 10) + (INTERVALLE_X)*(colonne)
            x2 = 10 + (INTERVALLE_X/2 + 10) + (INTERVALLE_X)*(colonne)
            y1 = 50 + (INTERVALLE_Y/2 - 10) + (INTERVALLE_Y)*(ligne-1)
            y2 = 50 + (INTERVALLE_Y/2 + 10) + (INTERVALLE_Y)*(ligne-1)
            CERCLE[ligne-1][colonne] = canvas.create_oval(x1, y1, x2, y2, fill=couleur)
            if LISTE_JEU[ligne-1] == LISTE_CODE:
                Victoire()
            else:
                bien_place = 0
                mal_place = 0
                if len(LISTE_JEU_COMPLET) != 0:
                    canvas.delete("bienPlacé")
                    canvas.delete("malPlacé")
                for j in range(CODE):
                    if (LISTE_JEU[ligne-1][j] == LISTE_CODE[j]):
                        bien_place += 1
                    elif (LISTE_JEU[ligne-1][j] in LISTE_CODE) and (LISTE_JEU[ligne-1][j] != LISTE_CODE[j]):
                        mal_place += 1
        
                bienPlace(bien_place)
                malPlace(mal_place)
        
        



# Création fonction deux joueurs #

def deuxJoueurs(couleurs, essais, intervalle_y, intervalle_x):
    '''Permet de démarrer le jeu à 2 joueurs'''
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global MODE
    global LISTE_CODE
    global CERCLE
    global CODE
    global LISTE_COULEURS

    mode_un_joueur.destroy()
    mode_deux_joueurs.destroy()
   
    menu.configure(text="MENU", font=("Helvetica", "8"), bg="papaya whip", command=Menu)
    retour.configure(text="←", font=("Helvetica", "8"), bg="papaya whip", command=Retour)

    # Création de la grille #
    x1, y1 = 10, 50
    x2 = x1+intervalle_x
    y2 = y1+intervalle_y
    for i in range(essais):
        for j in range(CODE):
            canvas.create_rectangle(x1,y1, x2,y2, fill="saddle brown")
            x1, x2 = x2, x2+intervalle_x
        y1, y2 = y2, y2+intervalle_y
        x1 = 10
        x2 = x1+intervalle_x

    # Création du jeu (code secret) #
    for a in range(CODE):
        print(couleurs)
        couleur_secret = str(input("Choisissez la couleur numéro "+str(a+1)+" parmi les couleurs présentes :\n"))
        while not (couleur_secret in couleurs):
            print(couleurs)
            couleur_secret = str(input("Choisissez la couleur numéro "+str(a+1)+" parmi les couleurs présentes :\n"))
        LISTE_CODE.append(couleur_secret)

    
    # Différents modes #
    if MODE == "Tres facile":
        CERCLE = [[0]*4 for x in range(NB_ESSAIS)]
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        
    elif MODE == "Facile":
        CERCLE = [[0]*5 for x in range(NB_ESSAIS)]
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        
    elif MODE == "Classique":
        CERCLE = [[0]*6 for x in range(NB_ESSAIS)]
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        LISTE_BOUTTONS[5].configure(text="●", font=("Helvetica", "8"), bg=couleurs[5], command=lambda : Jeu(couleurs[5]))
 

    else:
        CERCLE = [[0]*8 for x in range(NB_ESSAIS)]
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        LISTE_BOUTTONS[5].configure(text="●", font=("Helvetica", "8"), bg=couleurs[5], command=lambda : Jeu(couleurs[5]))
        LISTE_BOUTTONS[6].configure(text="●", font=("Helvetica", "8"), bg=couleurs[6], command=lambda : Jeu(couleurs[6]))
        LISTE_BOUTTONS[7].configure(text="●", font=("Helvetica", "8"), bg=couleurs[7], command=lambda : Jeu(couleurs[7]))




# Création fonction un joueur #

def unJoueur(couleurs, essais, intervalle_y, intervalle_x):
    '''Permet de démarrer le jeu à 1 joueur'''
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global MODE
    global LISTE_CODE
    global CERCLE
    global CODE

    mode_un_joueur.destroy()
    mode_deux_joueurs.destroy()
   
    # Création du jeu #
    retour.configure(text="←", font=("Helvetica", "8"), bg="papaya whip", command=Retour)
    menu.configure(text="MENU", font=("Helvetica", "8"), bg="papaya whip", command=Menu)

    a = 0
    for i in range(CODE):
        a = rd.randint(0, len(couleurs)-1)
        LISTE_CODE.append(couleurs[a])


    # Création de la grille #
    x1, y1 = 10, 50
    x2 = x1+intervalle_x
    y2 = y1+intervalle_y
    for i in range(essais):
        for j in range(CODE):
            canvas.create_rectangle(x1,y1, x2,y2, fill="saddle brown")
            x1, x2 = x2, x2+intervalle_x
        y1, y2 = y2, y2+intervalle_y
        x1 = 10
        x2 = x1+intervalle_x

    
    # Différents modes #
    if MODE == "Tres facile":
        CERCLE = [[0]*6 for x in range(NB_ESSAIS)]
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        LISTE_BOUTTONS[5].configure(text="●", font=("Helvetica", "8"), bg=couleurs[5], command=lambda : Jeu(couleurs[5]))
        
    elif MODE == "Facile":
        CERCLE = [[0]*6 for x in range(NB_ESSAIS)]
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        LISTE_BOUTTONS[5].configure(text="●", font=("Helvetica", "8"), bg=couleurs[5], command=lambda : Jeu(couleurs[5]))
        
    elif MODE == "Classique":
        CERCLE = [[0]*8 for x in range(NB_ESSAIS)]
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        LISTE_BOUTTONS[5].configure(text="●", font=("Helvetica", "8"), bg=couleurs[5], command=lambda : Jeu(couleurs[5]))
        LISTE_BOUTTONS[6].configure(text="●", font=("Helvetica", "8"), bg=couleurs[6], command=lambda : Jeu(couleurs[6]))
        LISTE_BOUTTONS[7].configure(text="●", font=("Helvetica", "8"), bg=couleurs[7], command=lambda : Jeu(couleurs[7]))

    else:
        CERCLE = [[0]*10 for x in range(NB_ESSAIS)]
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        LISTE_BOUTTONS[5].configure(text="●", font=("Helvetica", "8"), bg=couleurs[5], command=lambda : Jeu(couleurs[5]))
        LISTE_BOUTTONS[6].configure(text="●", font=("Helvetica", "8"), bg=couleurs[6], command=lambda : Jeu(couleurs[6]))
        LISTE_BOUTTONS[7].configure(text="●", font=("Helvetica", "8"), bg=couleurs[7], command=lambda : Jeu(couleurs[7]))
        LISTE_BOUTTONS[8].configure(text="●", font=("Helvetica", "8"), bg=couleurs[8], command=lambda : Jeu(couleurs[8]))
        LISTE_BOUTTONS[9].configure(text="●", font=("Helvetica", "8"), bg=couleurs[9], command=lambda : Jeu(couleurs[9]))

        

    





# Création des modes #

def tresFacile():
    '''Permet de démarrer le jeu en mode très facile'''
    global LISTE_COULEURS
    global NB_ESSAIS
    global INTERVALLE_Y
    global INTERVALLE_X
    global MODE
    global CODE
    CODE = 3
    MODE = "Tres facile"
    LISTE_COULEURS = ['black', 'green', 'blue', 'purple']
    NB_ESSAIS = 12
    INTERVALLE_Y = 40 #540
    INTERVALLE_X = 93 #289

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_CLASSIQUE.destroy()
    NV_IMPOSSIBLE.destroy()

    mode_un_joueur.configure(text="1 JOUEUR", command=lambda : unJoueur(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_un_joueur.grid(row=2, column=4, columnspan=2)
    mode_deux_joueurs.configure(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.grid(row=6, column=4, columnspan=2)



def Facile():
    '''Permet de démarrer le jeu en mode facile'''
    global LISTE_COULEURS
    global NB_ESSAIS
    global INTERVALLE_Y
    global INTERVALLE_X
    global MODE
    global CODE
    CODE = 4
    MODE = "Facile"
    LISTE_COULEURS = ['black', 'green', 'blue', 'purple', 'yellow']
    NB_ESSAIS = 12
    INTERVALLE_Y = 40 #540
    INTERVALLE_X = 70 #290

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_CLASSIQUE.destroy()
    NV_IMPOSSIBLE.destroy()

    mode_un_joueur.configure(text="1 JOUEUR", command=lambda : unJoueur(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_un_joueur.grid(row=2, column=4, columnspan=2)
    mode_deux_joueurs.configure(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.grid(row=6, column=4, columnspan=2)

def Classique():
    '''Permet de démarrer le jeu en mode tclassique'''
    global LISTE_COULEURS
    global NB_ESSAIS
    global INTERVALLE_Y
    global INTERVALLE_X
    global MODE
    global CODE
    CODE = 4
    MODE = "Classique"
    LISTE_COULEURS = ['black', 'green', 'blue', 'purple', 'yellow', 'orange']
    NB_ESSAIS = 10
    INTERVALLE_Y = 48 #530
    INTERVALLE_X = 70 #290

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_CLASSIQUE.destroy()
    NV_IMPOSSIBLE.destroy()

    mode_un_joueur.configure(text="1 JOUEUR", command=lambda : unJoueur(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_un_joueur.grid(row=2, column=4, columnspan=2)
    mode_deux_joueurs.configure(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.grid(row=6, column=4, columnspan=2)


def IMPOSSIBLE():
    '''Permet de démarrer le jeu en mode IMPOSSIBLE'''
    global LISTE_COULEURS
    global NB_ESSAIS
    global INTERVALLE_Y
    global INTERVALLE_X
    global MODE
    global CODE
    CODE = 5
    MODE = "IMPOSSIBLE"
    LISTE_COULEURS = ['black', 'green', 'blue', 'purple', 'yellow', 'orange', 'pink', 'cyan']
    NB_ESSAIS = 8
    INTERVALLE_Y = 60 #530
    INTERVALLE_X = 55 #290

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_CLASSIQUE.destroy()
    NV_IMPOSSIBLE.destroy()

    mode_un_joueur.configure(text="1 JOUEUR", command=lambda : unJoueur(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_un_joueur.grid(row=2, column=4, columnspan=2)
    mode_deux_joueurs.configure(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.grid(row=6, column=4, columnspan=2)




# Création du menu #

NV_TRES_FACILE = tk.Button(text="Très facile", command=tresFacile, font=("Helvetica", "10"), bg="brown")
NV_TRES_FACILE.grid(row=1, column=4, columnspan=2)

NV_FACILE = tk.Button(text="Facile", command=Facile, font=("Helvetica", "10"), bg="brown")
NV_FACILE.grid(row=3, column=4, columnspan=2)

NV_CLASSIQUE = tk.Button(text="Classique", command=Classique, font=("Helvetica", "10"), bg="brown")
NV_CLASSIQUE.grid(row=5, column=4, columnspan=2)

NV_IMPOSSIBLE = tk.Button(text="IMPOSSIBLE", command=IMPOSSIBLE, font=("Helvetica", "10"), bg="brown")
NV_IMPOSSIBLE.grid(row=7, column=4, columnspan=2)









fenetre.mainloop()