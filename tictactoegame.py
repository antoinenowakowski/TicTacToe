import sys

# tableau vide
array = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
# print le tableau
def afficheLeTableau():
    for i in array:
        for j in i:
            print(j, "|", end="")
        print("\n-------")
print(afficheLeTableau())

# fonction qui permet de vérifier si la grille est bonne
def verify():

    # vérifie les lignes du tableau
    for i in array:
        if i == ["x", "x", "x"]:
            print("Joueur x a gagné !")
            sys.exit()
        elif i == ["o", "o", "o"]:
            print("Joueur o a gagné !")
            sys.exit()

    # vérifie la colonne 0
    if array[0][0] and array[1][0] and array[2][0] == "x":
        print("Le joueur x a gagné !")
        sys.exit()
    elif array[0][0] and array[1][0] and array[2][0] == "o":
        print("Le joueur x a gagné !")
        sys.exit()

    # vérifie la colonne 1
    if array[0][1] and array[1][1] and array[2][1] == "x":
        print("Le joueur x a gagné !")
        sys.exit()
    elif array[0][1] and array[1][1] and array[2][1] == "o":
        print("Le joueur x a gagné !")
        sys.exit()

    # vérifie la colonne 2
    if array[0][2] and array[1][2] and array[2][2] == "x":
        print("Le joueur x a gagné !")
        sys.exit()
    elif array[0][2] and array[1][2] and array[2][2] == "o":
        print("Le joueur x a gagné !")
        sys.exit()

    # vérifier la diagonale
    if array[0][0] and array[1][1] and array[2][2] == "x":
        print("le joueur x a gagné !")
        sys.exit()
    elif array[0][0] and array[1][1] and array[2][2] == "o":
        print("le joueur o a gagné !")
        sys.exit()
    elif array[0][2] and array[1][1] and array[2][0] == "x":
        print("le joueur x a gagné")
        sys.exit()
    elif array[0][2] and array[1][1] and array[2][0] == "o":
        print("le joueur o a gagné !")
        sys.exit()

# symbole des joueurs
SymbolOfPlayerX = "x"
SymbolOfPlayerO = "o"

# fonction qui ajoute le symbole dans le tableau
def addInTheArray(jouer, Symbol):
    # first line
    if jouer == 1:
        array[0][0] = Symbol
    elif jouer == 2:
        array[0][1] = Symbol
    elif jouer == 3:
        array[0][2] = Symbol
    # second line
    elif jouer == 4:
        array[1][0] = Symbol
    elif jouer == 5:
        array[1][1] = Symbol
    elif jouer == 6:
        array[1][2] = Symbol
    # third line
    elif jouer == 7:
        array[2][0] = Symbol
    elif jouer == 8:
        array[2][1] = Symbol
    elif jouer == 9:
        array[2][2] = Symbol

# jeu
while True:
    print("De 1 à 9")

    joueur_x = int(input("Vous voulez mettre le croix dans quelle case ?"))
    addInTheArray(joueur_x, SymbolOfPlayerX)
    print(afficheLeTableau())
    verify()

    joueur_o = int(input("Vous voulez mettre le rond dans quelle case ?"))
    addInTheArray(joueur_o, SymbolOfPlayerO)
    print(afficheLeTableau())
    verify()