import tkinter as tk
import random as rd

####################################################################################################################
#                                                                                                                  #
#   Mastermind   :    Gaël FERREIRA RODRIGUEZ / Elise MOULIN / César PITIGLIANO / Noel-Marie N'dri                 #
#                                                                                                                  #
####################################################################################################################




# Conditions initiales #

Dict_liste_jeu = {"Tres facile":[[],[]], "Facile":[[],[]], "Classique":[[],[]], "IMPOSSIBLE":[[],[]]}

MODE = " "
NB_ESSAIS = 0
INTERVALLE_Y = 0 # intervalle nécessaire entre les différentes lignes de la grille
INTERVALLE_X = 0 # intervalle nécessaire entre les différentes colonnes de la grille
CODE = 0

LISTE_JEU = [[]]
LISTE_JEU_COMPLET = []
LISTE_COULEURS = []
LISTE_BOUTTONS = [0]*8
LISTE_CODE = []
CERCLE = [[]]
CERCLE2 = []
PIONS_BP = [[0]*4 for x in range(12)]
PIONS_MP = [[0]*4 for x in range(12)]

FIN_PARTIE = False

test = 0 # nombre de fois que le joueur retourne au menu, permet de générer à nouveau la page d'accueil et de réinitialiser par conséquent les boutons


# Création de la fenêtre #

HEIGHT = 600
WIDTH = 600
fenetre = tk.Tk()
fenetre.title("Mastermind")
canvas = tk.Canvas(fenetre, height=HEIGHT, width=WIDTH, bg='papaya whip')
canvas.grid(row=0, column=0, rowspan=9, columnspan=11)




# Création des bouttons initiales #

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

NV_TRES_FACILE = tk.Button(fenetre)
NV_TRES_FACILE.grid(row=1, column=5)

NV_FACILE = tk.Button(fenetre)
NV_FACILE.grid(row=3, column=5)

NV_CLASSIQUE = tk.Button(fenetre)
NV_CLASSIQUE.grid(row=5, column=5)

NV_IMPOSSIBLE = tk.Button(fenetre)
NV_IMPOSSIBLE.grid(row=7, column=5)



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
    global NB_ESSAIS
    global LISTE_BOUTTONS
    global LISTE_COULEURS
    global FIN_PARTIE
    FIN_PARTIE = True
    for i in range(8):
        LISTE_BOUTTONS[i].destroy()
    retour.destroy()
    gagne.config(text="Vous avez gagné !", font=("Helvetica", "14"), bg="papaya whip").place(x=360, y=300)
    


# Canvas défaite #

def Defaite():
    '''Détruis les boutons et affiche que le joueur a perdu(e)'''
    global NB_ESSAIS
    global LISTE_BOUTTONS
    global LISTE_COULEURS
    global FIN_PARTIE
    FIN_PARTIE = True
    for i in range(8):
        LISTE_BOUTTONS[i].destroy()
    retour.destroy()
    perdu.config(text="Vous avez perdu !", font=("Helvetica", "14"), bg="papaya whip").place(x=360, y=300)
   


# Sauvegarder #

def Sauvegarde():
    global MODE
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    sauvegarder.destroy()
    sauvegarder_oui.destroy()
    sauvegarder_non.destroy()
    Dict_liste_jeu[MODE][0] = LISTE_JEU
    Dict_liste_jeu[MODE][1] = LISTE_JEU_COMPLET
    LISTE_JEU = [[]]
    LISTE_JEU_COMPLET = []
    Accueil()



# Pas de sauvegarde #

def PasdeSauvegarde():
    global Dict_liste_jeu
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    sauvegarder.destroy()
    sauvegarder_oui.destroy()
    sauvegarder_non.destroy()
    LISTE_JEU = [[]]
    LISTE_JEU_COMPLET = []
    Dict_liste_jeu[MODE][0] = LISTE_JEU
    Dict_liste_jeu[MODE][1] = LISTE_JEU_COMPLET
    Accueil()


# Boutton Menu #

def Menu():
    '''Sauvegarde la partie si elle est en cours et relance le programme'''
    global LISTE_BOUTTONS
    global test
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global Dict_liste_jeu
    global MODE
     
    test += 1

    if FIN_PARTIE is True:
        LISTE_JEU = [[]]
        LISTE_JEU_COMPLET = []
        Dict_liste_jeu[MODE][0] = LISTE_JEU
        Dict_liste_jeu[MODE][1] = LISTE_JEU_COMPLET
        for i in range(8):
            LISTE_BOUTTONS[i].destroy()
        menu.destroy()
        retour.destroy()
        gagne.destroy()
        perdu.destroy()
        canvas.delete("all")
        Accueil()
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
        sauvegarder_oui.config(text="Oui", font=("Helvetica", "8"), command=Sauvegarde)
        sauvegarder_oui.grid_configure(row=5, column=4)
        sauvegarder_non.config(text="Non", font=("Helvetica", "8"), command=PasdeSauvegarde)
        sauvegarder_non.grid_configure(row=5, column=6)



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
                canvas.delete(PIONS_BP[ligne-1][i])
                canvas.delete(PIONS_MP[ligne-1][i])
                LISTE_JEU[ligne-1].pop()
                LISTE_JEU_COMPLET.pop()
                
        else:
            for j in range(colonne):
                canvas.delete(CERCLE[ligne][j])
                canvas.delete(PIONS_BP[ligne][j])
                canvas.delete(PIONS_MP[ligne][j])    
                LISTE_JEU[ligne].pop()
                LISTE_JEU_COMPLET.pop()
                 



# Création des pions bien plaçés et mal plaçés #

def bienPlace(n, ligne):
    '''Compte les pions bien plaçés et les affiches'''
    global INTERVALLE_Y
    global PIONS_BP
    global PIONS_MP
    x1, x2 = 300, 310
    y1 = 50 + (INTERVALLE_Y/4 - 5) + (INTERVALLE_Y)*(ligne-1)
    y2 = 50 + (INTERVALLE_Y/4 + 5) + (INTERVALLE_Y)*(ligne-1)
    for i in range(n):
        PIONS_BP[ligne-1][i] = canvas.create_oval((x1,y1),(x2,y2), fill="red")
        x1, x2 = x1+15, x2+15
    

def malPlace(n, ligne):
    '''Compte les pions mal plaçés et les affiches'''
    x1, x2 = 300, 310
    y1 = 50 + (INTERVALLE_Y*(3/4) - 5) + (INTERVALLE_Y)*(ligne-1)
    y2 = 50 + (INTERVALLE_Y*(3/4) + 5) + (INTERVALLE_Y)*(ligne-1)
    for i in range(n):
        PIONS_MP[ligne-1][i] = canvas.create_oval((x1,y1),(x2,y2), fill="white")
        x1, x2 = x1+15, x2+15



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
    
    if ligne >= NB_ESSAIS:
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
                for j in range(CODE):
                    if (LISTE_JEU[ligne-1][j] == LISTE_CODE[j]):
                        bien_place += 1
                    elif (LISTE_JEU[ligne-1][j] in LISTE_CODE) and (LISTE_JEU[ligne-1][j] != LISTE_CODE[j]):
                        mal_place += 1
        
                bienPlace(bien_place, ligne)
                malPlace(mal_place, ligne)
                
        
        



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
    global PIONS_BP
    global PIONS_MP

    mode_un_joueur.destroy()
    mode_deux_joueurs.destroy()
   
    menu.config(text="MENU", font=("Helvetica", "8"), bg="papaya whip", command=Menu)
    menu.place_configure(x=40, y=5)
    retour.config(text="←", font=("Helvetica", "8"), bg="papaya whip", command=Retour)
    retour.place_configure(x=10, y=5)

    PIONS_BP = [[0]*4 for x in range(NB_ESSAIS)]
    PIONS_MP = [[0]*4 for x in range(NB_ESSAIS)]

    # Création de la grille #
    x1, y1 = 10, 50
    x2 = x1+intervalle_x
    y2 = y1+intervalle_y
    for y in range(essais):
        for z in range(CODE):
            canvas.create_rectangle(x1,y1, x2,y2, fill="saddle brown")
            x1, x2 = x2, x2+intervalle_x
        y1, y2 = y2, y2+intervalle_y
        x1 = 10
        x2 = x1+intervalle_x
    
    for i in range(NB_ESSAIS):
        canvas.create_rectangle(290, 50+(intervalle_y*(i)), 360, 50+(intervalle_y*(i+1)))

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
        x=0
        for i in range(4):
            LISTE_BOUTTONS[i].grid_configure(row=8, column=x)
            x += 1
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        
    elif MODE == "Facile":
        CERCLE = [[0]*5 for x in range(NB_ESSAIS)]
        x=0
        for i in range(5):
            LISTE_BOUTTONS[i].grid_configure(row=8, column=x)
            x += 1
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        
    elif MODE == "Classique":
        CERCLE = [[0]*6 for x in range(NB_ESSAIS)]
        x=0
        for i in range(6):
            LISTE_BOUTTONS[i].grid_configure(row=8, column=x)
            x += 1
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        LISTE_BOUTTONS[5].configure(text="●", font=("Helvetica", "8"), bg=couleurs[5], command=lambda : Jeu(couleurs[5]))
 

    else:
        CERCLE = [[0]*8 for x in range(NB_ESSAIS)]
        x=0
        for i in range(8):
            LISTE_BOUTTONS[i].grid_configure(row=8, column=x)
            x += 1
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
    global PIONS_BP
    global PIONS_MP

    mode_un_joueur.destroy()
    mode_deux_joueurs.destroy()
   
    # Création du jeu #
    retour.config(text="←", font=("Helvetica", "8"), bg="papaya whip", command=Retour)
    retour.place_configure(x=10, y=5)
    menu.config(text="MENU", font=("Helvetica", "8"), bg="papaya whip", command=Menu)
    menu.place_configure(x=40, y=5)
    PIONS_BP = [[0]*4 for x in range(NB_ESSAIS)]
    PIONS_MP = [[0]*4 for x in range(NB_ESSAIS)]

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

    for i in range(NB_ESSAIS):
        canvas.create_rectangle(290, 50+(intervalle_y*(i)), 360, 50+(intervalle_y*(i+1)))
    
    # Différents modes #
    if MODE == "Tres facile":
        CERCLE = [[0]*4 for x in range(NB_ESSAIS)]
        x=0
        for i in range(4):
            LISTE_BOUTTONS[i].grid_configure(row=8, column=x)
            x += 1
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        
    elif MODE == "Facile":
        CERCLE = [[0]*5 for x in range(NB_ESSAIS)]
        x=0
        for i in range(5):
            LISTE_BOUTTONS[i].grid_configure(row=8, column=x)
            x += 1
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        
    elif MODE == "Classique":
        CERCLE = [[0]*6 for x in range(NB_ESSAIS)]
        x=0
        for i in range(6):
            LISTE_BOUTTONS[i].grid_configure(row=8, column=x)
            x += 1
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        LISTE_BOUTTONS[5].configure(text="●", font=("Helvetica", "8"), bg=couleurs[5], command=lambda : Jeu(couleurs[5]))

    else:
        CERCLE = [[0]*8 for x in range(NB_ESSAIS)]
        x=0
        for i in range(8):
            LISTE_BOUTTONS[i].grid_configure(row=8, column=x)
            x += 1
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        LISTE_BOUTTONS[4].configure(text="●", font=("Helvetica", "8"), bg=couleurs[4], command=lambda : Jeu(couleurs[4]))
        LISTE_BOUTTONS[5].configure(text="●", font=("Helvetica", "8"), bg=couleurs[5], command=lambda : Jeu(couleurs[5]))
        LISTE_BOUTTONS[6].configure(text="●", font=("Helvetica", "8"), bg=couleurs[6], command=lambda : Jeu(couleurs[6]))
        LISTE_BOUTTONS[7].configure(text="●", font=("Helvetica", "8"), bg=couleurs[7], command=lambda : Jeu(couleurs[7]))




# Création des modes #

def tresFacile():
    '''Permet de démarrer le jeu en mode très facile'''
    global LISTE_COULEURS
    global NB_ESSAIS
    global INTERVALLE_Y
    global INTERVALLE_X
    global MODE
    global CODE
    global Dict_liste_jeu
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    CODE = 3
    MODE = "Tres facile"
    LISTE_COULEURS = ['black', 'green', 'blue', 'purple']
    NB_ESSAIS = 12
    INTERVALLE_Y = 40 #540
    INTERVALLE_X = 93.3 #289
    LISTE_JEU = Dict_liste_jeu[MODE][0]
    LISTE_JEU_COMPLET = Dict_liste_jeu[MODE][1]

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_CLASSIQUE.destroy()
    NV_IMPOSSIBLE.destroy()

    mode_un_joueur.config(text="1 JOUEUR", command=lambda : unJoueur(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_un_joueur.grid(row=2, column=5)
    mode_deux_joueurs.config(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.grid(row=6, column=5)



def Facile():
    '''Permet de démarrer le jeu en mode facile'''
    global LISTE_COULEURS
    global NB_ESSAIS
    global INTERVALLE_Y
    global INTERVALLE_X
    global MODE
    global CODE
    global Dict_liste_jeu
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    CODE = 4
    MODE = "Facile"
    LISTE_COULEURS = ['black', 'green', 'blue', 'purple', 'yellow']
    NB_ESSAIS = 12
    INTERVALLE_Y = 40 #540
    INTERVALLE_X = 70 #290
    LISTE_JEU = Dict_liste_jeu[MODE][0]
    LISTE_JEU_COMPLET = Dict_liste_jeu[MODE][1]

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_CLASSIQUE.destroy()
    NV_IMPOSSIBLE.destroy()

    mode_un_joueur.configure(text="1 JOUEUR", command=lambda : unJoueur(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_un_joueur.grid(row=2, column=5)
    mode_deux_joueurs.configure(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.grid(row=6, column=5)

def Classique():
    '''Permet de démarrer le jeu en mode classique'''
    global LISTE_COULEURS
    global NB_ESSAIS
    global INTERVALLE_Y
    global INTERVALLE_X
    global MODE
    global CODE
    global Dict_liste_jeu
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    CODE = 4
    MODE = "Classique"
    LISTE_COULEURS = ['black', 'green', 'blue', 'purple', 'yellow', 'orange']
    NB_ESSAIS = 10
    INTERVALLE_Y = 48 #530
    INTERVALLE_X = 70 #290
    LISTE_JEU = Dict_liste_jeu[MODE][0]
    LISTE_JEU_COMPLET = Dict_liste_jeu[MODE][1]

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_CLASSIQUE.destroy()
    NV_IMPOSSIBLE.destroy()

    mode_un_joueur.configure(text="1 JOUEUR", command=lambda : unJoueur(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_un_joueur.grid(row=2, column=5)
    mode_deux_joueurs.configure(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.grid(row=6, column=5)


def IMPOSSIBLE():
    '''Permet de démarrer le jeu en mode IMPOSSIBLE'''
    global LISTE_COULEURS
    global NB_ESSAIS
    global INTERVALLE_Y
    global INTERVALLE_X
    global MODE
    global CODE
    global Dict_liste_jeu
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    CODE = 5
    MODE = "IMPOSSIBLE"
    LISTE_COULEURS = ['black', 'green', 'blue', 'purple', 'yellow', 'orange', 'pink', 'cyan']
    NB_ESSAIS = 8
    INTERVALLE_Y = 60 #530
    INTERVALLE_X = 55 #290
    LISTE_JEU = Dict_liste_jeu[MODE][0]
    LISTE_JEU_COMPLET = Dict_liste_jeu[MODE][1]

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_CLASSIQUE.destroy()
    NV_IMPOSSIBLE.destroy()

    mode_un_joueur.configure(text="1 JOUEUR", command=lambda : unJoueur(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_un_joueur.grid(row=2, column=5)
    mode_deux_joueurs.configure(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE_Y, INTERVALLE_X), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.grid(row=6, column=5)




# Création du menu #

def Accueil():
    global test
    global NV_TRES_FACILE
    global NV_FACILE
    global NV_CLASSIQUE
    global NV_IMPOSSIBLE
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

        NV_TRES_FACILE = tk.Button(fenetre)
        NV_TRES_FACILE.grid(row=1, column=5)

        NV_FACILE = tk.Button(fenetre)
        NV_FACILE.grid(row=3, column=5)

        NV_CLASSIQUE = tk.Button(fenetre)
        NV_CLASSIQUE.grid(row=5, column=5)

        NV_IMPOSSIBLE = tk.Button(fenetre)
        NV_IMPOSSIBLE.grid(row=7, column=5)

        for i in range(8):
            LISTE_BOUTTONS[i] = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
            LISTE_BOUTTONS[i].place(x=1000, y=0)

        for j in range(12):
            for k in range(4):
                PIONS_BP[j][k] = canvas.create_oval((0,0),(1,1), fill="papaya whip")

        for l in range(12):
            for m in range(4):
                PIONS_MP[l][m] = canvas.create_oval((0,0),(1,1), fill="papaya whip")


    NV_TRES_FACILE.config(text="Très facile", command=tresFacile, font=("Helvetica", "10"), bg="brown")
    NV_FACILE.config(text="Facile", command=Facile, font=("Helvetica", "10"), bg="brown")
    NV_CLASSIQUE.config(text="Classique", command=Classique, font=("Helvetica", "10"), bg="brown")
    NV_IMPOSSIBLE.config(text="IMPOSSIBLE", command=IMPOSSIBLE, font=("Helvetica", "10"), bg="brown")





Accueil()
fenetre.mainloop()