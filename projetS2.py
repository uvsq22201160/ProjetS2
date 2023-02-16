import tkinter as tk
import random as rd

### Création de la grille et de la fenêtre ###
HEIGHT = 600
WIDTH = 820
colonne = 4
x1, x2, y1, y2 = 10, 210, 100, 300
fenetre = tk.Tk()
fenetre.title("Mastermind")
canvas = tk.Canvas(fenetre, height=HEIGHT, width=WIDTH, bg='papaya whip')
canvas.grid()
for loop in range(colonne):
    canvas.create_rectangle((x1,y1), (x2,y2), fill='gray77')
    x1, x2 = x2, x2+200


### Fonctions pions bien plaçés et mal plaçés ###

def bien_place(n):
    x1, x2, y1, y2 = 10, 20, 350, 360
    for loop in range(n):
        canvas.create_oval((x1,y1),(x2,y2), fill='red')
        x1, x2 = x1+30, x2+30

def mal_place(n):
    x1, x2, y1, y2 = 10, 20, 380, 390
    for loop in range(n):
        canvas.create_oval((x1,y1),(x2,y2), fill='white')
        x1, x2 = x1+30, x2+30

### Fonction victoire ###
def Victoire():

### Fonction défaite ###
def Defaite():

### Fonction un joueur ###

Liste_couleur = ['blue', 'green', 'white', 'yellow', 'purple', 'orange', 'red', 'black']

def unJoueur():
    couleurs_grille = []
    for i in range(4):
        couleurs_grille.append(Liste_couleur[rd.randint(0,7)])
    cercle1 = canvas.create_oval((60,150),(160,250), fill=couleurs_grille[0])
    cercle2 = canvas.create_oval((260,150),(360,250), fill=couleurs_grille[1])
    cercle3 = canvas.create_oval((460,150),(560,250), fill=couleurs_grille[2])
    cercle4 = canvas.create_oval((660,150),(760,250), fill=couleurs_grille[3])
    


    essais = 0
    bienPlace = 0
    malPlace = 0
    couleurs_joueur = []
    while (couleurs_joueur != couleurs_grille) or essais > 10:
        for i in range(colonne):
            couleur = str(input('Choisissez la couleur '+ str(i+1) +'(en anglais et en minuscule) : '))
            while not (couleur in Liste_couleur):
                couleur = str(input('Choisissez une autre couleur (en anglais et en minuscule) ou vérifier votre écriture : '))
            couleurs_joueur.append(couleur)
        if couleurs_joueur == couleurs_grille:
            Victoire()
        else:
            for k in range(4):
                if (couleurs_joueur[k] == couleurs_grille[k]):
                    bienPlace += 1
                elif (couleurs_joueur[k] in couleurs_grille) and (couleurs_joueur[k] != couleurs_grille[k]):
                    malPlace += 1
                
        bien_place(bienPlace)
        mal_place(malPlace)
        couleurs_joueur = []
        essais += 1
    Defaite()

### Fonction un joueur ###


unJoueur()
fenetre.mainloop()