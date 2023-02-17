import tkinter as tk
import random as rd
import time
### Création de la fenêtre ###

HEIGHT = 600
WIDTH = 820
colonne = 4
fenetre = tk.Tk()
fenetre.title("Mastermind")
canvas = tk.Canvas(fenetre, height=HEIGHT, width=WIDTH, bg='papaya whip')
canvas.grid()

### Création de la grille principale ###
def grille():
    x1, x2, y1, y2 = 10, 210, 100, 300
    for loop in range(colonne):
        canvas.create_rectangle((x1,y1), (x2,y2), fill='gray77')
        x1, x2 = x2, x2+200

### Création de la grille secondaire ###
def grille2():
    x1, x2, y1, y2 = 10, 40, 420, 450
    for loop in range(colonne):
        canvas.create_rectangle((x1,y1), (x2,y2), fill='gray77')
        x1, x2 = x2, x2+30

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
    canvas.delete("all")
    victoire = tk.Label(fenetre, text="Vous avez gagné(e)",font = ("helvetica", "60"))
    victoire.grid(column=0, row=0, pady=50)

### Fonction défaite ###
def Defaite():
    canvas.delete("all")
    victoire = tk.Label(fenetre, text="Vous avez perdu(e)",font = ("helvetica", "60"))
    victoire.grid(column=0, row=0, pady=50)
    
### Fonction un joueur ###
Liste_couleur = ['blue', 'green', 'white', 'yellow', 'purple', 'orange', 'red', 'black']

def unJoueur():
    grille()
    grille2()
    couleurs_grille = []
    essais = 0
    bienPlace = 0
    malPlace = 0
    couleurs_joueur = []
    pions = [0, 0, 0, 0]
    for i in range(4):
        couleurs_grille.append(Liste_couleur[rd.randint(0,7)])
    for loop in range(11):
        x1, x2, y1, y2 = 60, 160, 150, 250
        x3, x4, y3, y4 = 20, 30, 430, 440
        for i in range(colonne):
            couleur = str(input('Choisissez la couleur '+ str(i+1) +'(en anglais et en minuscule) : '))
            while not (couleur in Liste_couleur):
                couleur = str(input('Choisissez une autre couleur (en anglais et en minuscule) ou vérifier votre écriture : '))
            couleurs_joueur.append(couleur)
            pions[i] = canvas.create_oval((x1,y1),(x2,y2), fill=couleurs_joueur[i])
            x1, x2 = x1+200, x2+200
        if couleurs_joueur == couleurs_grille:
            Victoire()
            continue
        elif essais > 10:
            Defaite()
            continue
        else:
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
        bien_place(bienPlace)
        mal_place(malPlace)
        couleurs_joueur = []
        essais += 1
    
    

### Fonction un joueur ###


unJoueur()
fenetre.mainloop()