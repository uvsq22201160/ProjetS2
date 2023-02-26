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


LISTE_JEU = [[]]
LISTE_JEU_COMPLET = []
LISTE_COULEURS = []
LISTE_BOUTTONS = [0]*10
LISTE_HASARD = []
CERCLE = [[]]

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

x=0
for i in range(10):
    LISTE_BOUTTONS[i] = tk.Button(text="", font=("Helvetica", "1"), bg="papaya whip")
    LISTE_BOUTTONS[i].grid(row=8, column=x)
    x += 1



# Canvas victoire #

def Victoire():
    global NB_ESSAIS
    global LISTE_BOUTTONS
    global LISTE_COULEURS
    for i in range(10):
        LISTE_BOUTTONS[i].destroy()
    Gagne = tk.Label(text="Vous avez gagné!", font=("Helvetica", "18"), bg="papaya whip").place(x=320, y=300)
    



# Canvas défaite #

def Defaite():
    global NB_ESSAIS
    global LISTE_BOUTTONS
    global LISTE_COULEURS
    for i in range(10):
        LISTE_BOUTTONS[i].destroy()
    Defaite = tk.Label(text="Vous avez perdu!", font=("Helvetica", "8"),).place(x=320, y=300)
   



# Boutton Menu #

def Menu():
    global LISTE_BOUTTONS
    canvas.delete("all")
    retour.destroy()
    for i in range(10):
        LISTE_BOUTTONS[i].destroy()

    NV_TRES_FACILE = tk.Button(text="Très facile", command=tresFacile, font=("Helvetica", "10"), bg="brown")
    NV_TRES_FACILE.grid(row=1, column=4, columnspan=2)

    NV_FACILE = tk.Button(text="Facile", command=Facile, font=("Helvetica", "10"), bg="brown")
    NV_FACILE.grid(row=3, column=4, columnspan=2)

    NV_MOYEN = tk.Button(text="Moyen", command=Moyen, font=("Helvetica", "10"), bg="brown")
    NV_MOYEN.grid(row=5, column=4, columnspan=2)

    NV_DIFFICILE = tk.Button(text="Difficile", command=Difficile, font=("Helvetica", "10"), bg="brown")
    NV_DIFFICILE.grid(row=7, column=4, columnspan=2)


# Boutton retour #

def Retour():
    global LISTE_JEU_COMPLET
    global LISTE_JEU
    global CERCLE
    colonne = len(LISTE_JEU_COMPLET) % 4
    ligne = int(len(LISTE_JEU_COMPLET) // 4)

    if LISTE_JEU_COMPLET != []:
        if colonne == 0:
            for i in range(4):
                canvas.delete(CERCLE[ligne-1][i])
                LISTE_JEU[ligne-1].pop()
                LISTE_JEU_COMPLET.pop()
        else:
            for j in range(colonne):
                canvas.delete(CERCLE[ligne][j])
                LISTE_JEU[ligne].pop()
                LISTE_JEU_COMPLET.pop()
        
       

    



# Création des pions bien plaçés et mal plaçés #

def bienPlace(n):
    x1, x2, y1, y2 = 300, 320, 50, 70
    for i in range(n):
        canvas.create_oval((x1,y1),(x2,y2), fill="red", tags="bienPlacé")
        x1, x2 = x1+40, x2+40

def malPlace(n):
    x1, x2, y1, y2 = 300, 320, 90, 110
    for i in range(n):
        canvas.create_oval((x1,y1),(x2,y2), fill="white", tags="malPlacé")
        x1, x2 = x1+40, x2+40



# Création partie interactive #

def Jeu(couleur):
    global NB_ESSAIS
    global LISTE_JEU_COMPLET
    global LISTE_JEU
    global LISTE_HASARD
    global CERCLE
    LISTE_JEU_COMPLET.append(couleur)
    colonne = len(LISTE_JEU_COMPLET) % 4
    ligne = int(len(LISTE_JEU_COMPLET) // 4)
    
    if ligne > NB_ESSAIS:
        Defaite()
    else:
        if colonne == 1:
            LISTE_JEU.append([])
            LISTE_JEU[ligne].append(couleur)
            if NB_ESSAIS == 12:
                x1, x2, y1, y2 = 30, 60, 55+40*(ligne), 85+40*(ligne)
                CERCLE[ligne][0] = canvas.create_oval(x1, y1, x2, y2, fill=couleur)
        elif colonne != 0:
            LISTE_JEU[ligne].append(couleur)
            if NB_ESSAIS == 12:
                x1, x2, y1, y2 = 30+70*(colonne-1), 60+70*(colonne-1), 55+40*(ligne), 85+40*(ligne)
                CERCLE[ligne][colonne-1] = canvas.create_oval(x1, y1, x2, y2, fill=couleur)

            elif NB_ESSAIS == 10:
                pass
            else:
                pass
        
        else :
            colonne = 3
            LISTE_JEU[ligne-1].append(couleur)
            # test #
            print(LISTE_JEU[ligne-1], LISTE_HASARD)
            # test #
            if NB_ESSAIS == 12:
                x1, x2, y1, y2 = 30+70*(colonne), 60+70*(colonne), 55+40*(ligne-1), 85+40*(ligne-1)
                CERCLE[ligne-1][colonne] = canvas.create_oval(x1, y1, x2, y2, fill=couleur, tags=str(ligne-1)+"4")
                if LISTE_JEU[ligne-1] == LISTE_HASARD:
                    Victoire()
                else:
                    bien_place = 0
                    mal_place = 0
                    if LISTE_JEU[0][0] != ' ':
                        canvas.delete("bienPlacé")
                        canvas.delete("malPlacé")
                    for j in range(4):
                        if (LISTE_JEU[ligne-1][j] == LISTE_HASARD[j]):
                            bien_place += 1
                        elif (LISTE_JEU[ligne-1][j] in LISTE_HASARD) and (LISTE_JEU[ligne-1][j] != LISTE_HASARD[j]):
                            mal_place += 1
            
                    bienPlace(bien_place)
                    malPlace(mal_place)
                    
            elif NB_ESSAIS == 10:
                pass
            else:
                pass
        
        

# Création fonction un joueur #

def unJoueur(couleurs, essais, intervalle):
    global LISTE_JEU
    global LISTE_JEU_COMPLET
    global MODE
    global LISTE_HASARD
    global CERCLE
    CERCLE = [[0]*4 for x in range(NB_ESSAIS)]
    mode_un_joueur.destroy()
    mode_deux_joueurs.destroy()
   
    # Création du jeu #
    retour.configure(text="←", font=("Helvetica", "8"), bg="papaya whip", command=Retour)
    menu.configure(text="MENU", font=("Helvetica", "8"), bg="papaya whip", command=Menu)

    a = 0
    for i in range(4):
        a = rd.randint(0, len(couleurs)-1)
        LISTE_HASARD.append(couleurs[a])

    # Création de la grille #
    x1, x2, y1 = 10, 80, 50
    y2 = y1+intervalle
    for i in range(essais):
        for j in range(4):
            canvas.create_rectangle(x1,y1, x2,y2, fill="saddle brown", tags="rectangle")
            x1, x2 = x2, x2+70
        x1, x2 = 10, 80
        y1, y2 = y2, y2+intervalle
    
    # Bouttons différents modes #
    if MODE == "Tres facile":
        LISTE_BOUTTONS[0].configure(text="●", font=("Helvetica", "8"), bg=couleurs[0], command=lambda : Jeu(couleurs[0]))
        LISTE_BOUTTONS[1].configure(text="●", font=("Helvetica", "8"), bg=couleurs[1], command=lambda : Jeu(couleurs[1]))
        LISTE_BOUTTONS[2].configure(text="●", font=("Helvetica", "8"), bg=couleurs[2], command=lambda : Jeu(couleurs[2]))
        LISTE_BOUTTONS[3].configure(text="●", font=("Helvetica", "8"), bg=couleurs[3], command=lambda : Jeu(couleurs[3]))
        
        

        

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
    mode_un_joueur.grid(row=2, column=4, columnspan=2)
    mode_deux_joueurs.configure(text="2 JOUEURS", command=lambda : deuxJoueurs(LISTE_COULEURS, NB_ESSAIS, INTERVALLE), font=("Helvetica", "16"), bg="brown")
    mode_deux_joueurs.grid(row=6, column=4, columnspan=2)



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
NV_TRES_FACILE.grid(row=1, column=4, columnspan=2)

NV_FACILE = tk.Button(text="Facile", command=Facile, font=("Helvetica", "10"), bg="brown")
NV_FACILE.grid(row=3, column=4, columnspan=2)

NV_MOYEN = tk.Button(text="Moyen", command=Moyen, font=("Helvetica", "10"), bg="brown")
NV_MOYEN.grid(row=5, column=4, columnspan=2)

NV_DIFFICILE = tk.Button(text="Difficile", command=Difficile, font=("Helvetica", "10"), bg="brown")
NV_DIFFICILE.grid(row=7, column=4, columnspan=2)









fenetre.mainloop()