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
INTERVALLE = 0 # intervalle nécessaire entre les différentes lignes de la grille


LISTE_JEU = []
LISTE_JEU_COMPLET = []
LISTE_COULEURS = []
LISTE_BOUTTONS = [0]*10
LISTE_HASARD = []

# Création de la fenêtre #

HEIGHT = 600
WIDTH = 600
fenetre = tk.Tk()
fenetre.title("Mastermind")
canvas = tk.Canvas(fenetre, height=HEIGHT, width=WIDTH, bg='papaya whip')
canvas.grid(row=0, column=0, rowspan=9, columnspan=2)

mode_un_joueur = tk.Button(text=" ", font=("Helvetica", "1"), bg="papaya whip")
mode_un_joueur.grid(row=2, column=0, columnspan=2)
mode_deux_joueurs = tk.Button(text=" ", font=("Helvetica", "1"), bg="papaya whip")
mode_deux_joueurs.grid(row=6, column=0, columnspan=2)



# Canvas victoire #

def Victoire():
    Gagne = tk.Label(text="Vous avez gagné!", font=("Helvetica", "8"),).place(x=10, y=10)
    



# Canvas défaite #

def Defaite():
    Defaite = tk.Label(text="Vous avez perdu!", font=("Helvetica", "8"),).place(x=10, y=10)
   


# Création des pions bien plaçés et mal plaçés #





# Création partie interactive #

def Cercle(couleur):
    global NB_ESSAIS
    global LISTE_JEU_COMPLET
    global LISTE_JEU
    global LISTE_HASARD
    LISTE_JEU_COMPLET.append(couleur)
    colonne = len(LISTE_JEU_COMPLET) % 4
    ligne = int(len(LISTE_JEU_COMPLET) // 4)
    bien_place = 0
    mal_place = 0

    if ligne > NB_ESSAIS:
        Defaite()

    else:
        if colonne != 0:
            LISTE_JEU[ligne][colonne-1] = couleur
            if NB_ESSAIS == 12:
                x1, x2, y1, y2 = 30+70*(colonne-1), 60+70*(colonne-1), 55+40*(ligne), 85+40*(ligne)
                canvas.create_oval(x1, y1, x2, y2, fill=couleur)
            elif NB_ESSAIS == 10:
                pass
            else:
                pass

        else :
            colonne = 3
            LISTE_JEU[ligne-1][colonne] = couleur
            if NB_ESSAIS == 12:
                x1, x2, y1, y2 = 30+70*(colonne), 60+70*(colonne), 55+40*(ligne-1), 85+40*(ligne-1)
                canvas.create_oval(x1, y1, x2, y2, fill=couleur)
                    
            elif NB_ESSAIS == 10:
                pass
            else:
                pass
 
        
        

# Création fonction un joueur #

def unJoueur(couleurs, essais, intervalle):
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global MODE
    LISTE_JEU = [[' ']*4 for x in range(essais)]
    mode_un_joueur.destroy()
    mode_deux_joueurs.destroy()

    
    # Création du jeu #
    LISTE_HASARD = []
    for i in range(4):
        a = rd.randint(0, len(couleurs)-1)
        LISTE_HASARD.append(couleurs[a])
    print(LISTE_HASARD)

    ligne = int(len(LISTE_JEU_COMPLET) // 4)
    colonne = len(LISTE_JEU_COMPLET) % 4
    

    # Création de la grille #
    x1, x2, y1 = 10, 80, 50
    y2 = y1+intervalle
    for i in range(essais):
        for j in range(4):
            canvas.create_rectangle((x1,y1), (x2,y2), fill="saddle brown")
            x1, x2 = x2, x2+70
        x1, x2 = 10, 80
        y1, y2 = y2, y2+intervalle
    
    # fonctions des différents modes #
    if MODE == "Tres facile":
        LISTE_BOUTTONS[0] = tk.Button(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Cercle(couleurs[0])).place(x=300, y=560)
        LISTE_BOUTTONS[1] = tk.Button(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Cercle(couleurs[1])).place(x=320, y=560)
        LISTE_BOUTTONS[2] = tk.Button(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Cercle(couleurs[2])).place(x=340, y=560)
        LISTE_BOUTTONS[3] = tk.Button(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Cercle(couleurs[3])).place(x=360, y=560)
        if colonne == 0:
            if LISTE_JEU[ligne-1] == LISTE_HASARD:
                Victoire()
            else:
                bien_place = 0
                mal_place = 0
                if LISTE_JEU[0][0] != ' ':
                    canvas.delete("bienPlacé")
                    canvas.delete("malPlacé")
                for j in range(4):
                    if (LISTE_JEU[ligne-1][j] == LISTE_HASARD):
                        bien_place += 1
                    elif (LISTE_JEU[ligne-1][j] in LISTE_HASARD) and (LISTE_JEU[ligne-1][l] != LISTE_HASARD[l]):
                        mal_place += 1

                a1, a2, b1, b2 = 300, 340, 50, 90
                for k in range(bien_place):
                    canvas.create_oval((a1,b1),(a2,b2), fill="red", tags="bienPlacé")
                    a1, a2 = a1+40, a2+40
                for l in range(mal_place):
                    b1, b2 = 110, 150
                    canvas.create_oval((a1,b1),(a2,b2), fill="white", tags="malPlacé")
                    a1, a2 = a1+40, a2+40
        

        

    elif MODE == "Facile":
        pass
    elif MODE == "moyen":
        pass
    else:
        pass


    





# Création fonction deux joueurs #

def deuxJoueurs(couleurs, essais, intervalle):
    mode_un_joueur.destroy()
    mode_deux_joueurs.destroy()


# Création des modes #

def tresFacile():
    global LISTE_COULEURS
    global NB_ESSAIS
    global INTERVALLE
    global MODE
    MODE = "Tres facile"
    LISTE_COULEURS = ['black', 'green', 'blue', 'purple']
    NB_ESSAIS = 12
    INTERVALLE = 40 #540

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_MOYEN.destroy()
    NV_DIFFICILE.destroy()

    mode_un_joueur.configure(text="1 JOUEUR", command=lambda : unJoueur(LISTE_COULEURS, NB_ESSAIS, INTERVALLE), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.configure(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE), font=("Helvetica", "16"), bg="brown")



def Facile():
    global LISTE_COULEURS
    global NB_ESSAIS
    LISTE_COULEURS = ["black", "green", "blue", "purple", "yellow", "orange"]
    NB_ESSAIS = 12

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_MOYEN.destroy()
    NV_DIFFICILE.destroy()


def Moyen():
    global LISTE_COULEURS
    global NB_ESSAIS
    LISTE_COULEURS = ["black", "green", "blue", "purple", "yellow", "orange", "pink", "cyan"]
    NB_ESSAIS = 10

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_MOYEN.destroy()
    NV_DIFFICILE.destroy()


def Difficile():
    global LISTE_COULEURS
    global NB_ESSAIS
    LISTE_COULEURS = ["black", "green", "blue", "purple", "yellow", "orange", "pink", "cyan", "gray", "azur"]
    NB_ESSAIS = 8

    NV_TRES_FACILE.destroy()
    NV_FACILE.destroy()
    NV_MOYEN.destroy()
    NV_DIFFICILE.destroy()



# Création du menu #

NV_TRES_FACILE = tk.Button(text="Très facile", command=tresFacile, font=("Helvetica", "10"), bg="brown")
NV_TRES_FACILE.grid(row=1, column=0, columnspan=2)

NV_FACILE = tk.Button(text="Facile", command=Facile, font=("Helvetica", "10"), bg="brown")
NV_FACILE.grid(row=3, column=0, columnspan=2)

NV_MOYEN = tk.Button(text="Moyen", command=Moyen, font=("Helvetica", "10"), bg="brown")
NV_MOYEN.grid(row=5, column=0, columnspan=2)

NV_DIFFICILE = tk.Button(text="Difficile", command=Difficile, font=("Helvetica", "10"), bg="brown")
NV_DIFFICILE.grid(row=7, column=0, columnspan=2)









fenetre.mainloop()