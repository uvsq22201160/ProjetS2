import tkinter as tk
import random as rd



Liste_couleur = ['blue', 'green', 'white', 'yellow', 'purple', 'orange', 'red', 'black']
Texte_couleur = ''
for i in range(len(Liste_couleur)):
    if i == len(Liste_couleur)-1:
        Texte_couleur += Liste_couleur[i]+'.'
    else:
        Texte_couleur += Liste_couleur[i]+', '
### Création de la fenêtre ###
HEIGHT = 400
WIDTH = 620
colonne = 4
fenetre = tk.Tk()
fenetre.title("Mastermind")
canvas = tk.Canvas(fenetre, height=HEIGHT, width=WIDTH, bg='papaya whip')
canvas.grid()

### Création de la grille principale ###


def grille():
    x1, x2, y1, y2 = 10, 150, 50, 200
    for loop in range(colonne):
        canvas.create_rectangle((x1,y1), (x2,y2), fill='gray77')
        x1, x2 = x2, x2+140
    help = tk.Button(text="?", command=Help, font=("Helvetica", "5")).place(x=570, y=8)

### Création de la grille secondaire ###
def grille2():
    x1, x2, y1, y2 = 10, 40, 270, 300
    for loop in range(colonne):
        canvas.create_rectangle((x1,y1), (x2,y2), fill='gray77')
        x1, x2 = x2, x2+30

### Fonctions pions bien plaçés et mal plaçés ###
def bien_place(n, essais):
    if essais > 0:
        canvas.delete("bienPlacé")
    x1, x2, y1, y2 = 10, 20, 220, 230
    for loop in range(n):
        pions = canvas.create_oval((x1,y1),(x2,y2), fill='red', tags="bienPlacé")
        x1, x2 = x1+30, x2+30

def mal_place(n, essais):
    if essais > 0:
        canvas.delete("malPlacé")
    x1, x2, y1, y2 = 10, 20, 240, 250
    for loop in range(n):
        canvas.create_oval((x1,y1),(x2,y2), fill='white', tags = "malPlacé")
        x1, x2 = x1+30, x2+30

### Fonction Help ###
def Help():
    fenetre_help = tk.Tk()
    fenetre.title("Aide pions")
    canvas = tk.Canvas(fenetre_help, height=300, width=400, bg='papaya whip')
    canvas.grid()
    couleur = tk.Label(fenetre_help, text='Couleurs : ', font = ("helvetica", "8"), bg='papaya whip').place(x=10, y=20)
    listeCouleurs = tk.Label(fenetre_help, text=Texte_couleur, font = ("helvetica", "8"), bg='papaya whip').place(x=70, y=20)
    canvas.create_oval((10,95),(20,105), fill='red')
    canvas.create_oval((10, 195),(20,205), fill='white')
    bienPlace = tk.Label(fenetre_help, text=": correspond aux pions BIEN plaçés.", font = ("helvetica", "10"), bg='papaya whip').place(x=25, y=90)
    malPlace = tk.Label(fenetre_help, text=": correspond aux pions MAL plaçés.", font = ("helvetica", "10"), bg='papaya whip').place(x=25, y=190)


### Fonction retour ###
def Retour(essais):
    essais += 1

### Fonction victoire ###
def Victoire():
    canvas.delete('all')
    victoire = tk.Label(fenetre, text="Vous avez gagné(e) !", font = ("helvetica", "30"), bg='papaya whip').place(x=10, y=200)

### Fonction défaite ###
def Defaite():
    canvas.delete('all')
    defaite = tk.Label(fenetre, text="Vous avez perdu(e) !",font = ("helvetica", "30"), bg='papaya whip').place(x=10, y=200)
    
### Fonction un joueur ###
def unJoueur():
    grille()
    grille2()
    couleurs_grille = []
    essais = 10
    couleurs_joueur = []
    pions = [0, 0, 0, 0]
    for i in range(4):
        couleurs_grille.append(Liste_couleur[rd.randint(0,7)])
    while essais > 0 :
        retour = tk.Button(text="←", font=("helvetica", "8"), command=lambda : Retour(essais)).place(x=10, y=10)
        essais_restants = tk.Label(text="essais restant(s) :" + str(essais), font=("helvetica", "8"), bg='papaya whip').place(x=10, y=320)
        x1, x2, y1, y2 = 50, 110, 100, 150
        x3, x4, y3, y4 = 20, 30, 280, 290
        for i in range(colonne):
            couleur = str(input('Choisissez la couleur '+ str(i+1) +'(en anglais et en minuscule) : '))
            while not (couleur in Liste_couleur):
                couleur = str(input('Choisissez une autre couleur (en anglais et en minuscule) ou vérifier votre écriture : '))
            couleurs_joueur.append(couleur)
            pions[i] = canvas.create_oval((x1,y1),(x2,y2), fill=couleurs_joueur[i])
            x1, x2 = x1+140, x2+140
        if couleurs_joueur == couleurs_grille:
            Victoire()
            continue
        else:
            bienPlace = 0
            malPlace = 0
            for k in range(4):
                if (couleurs_joueur[k] == couleurs_grille[k]):
                    bienPlace += 1
                elif (couleurs_joueur[k] in couleurs_grille) and (couleurs_joueur[k] != couleurs_grille[k]):
                    malPlace += 1
        for l in range(4):
            canvas.delete(pions[l])
        for m in range(4):
            canvas.create_oval((x3,y3),(x4,y4), fill=couleurs_joueur[m])
            x3, x4 = x3+30, x4+30
        bien_place(bienPlace, essais)
        mal_place(malPlace, essais)
        couleurs_joueur = []
        essais = essais - 1
    Defaite()


unJoueur()
fenetre.mainloop()
