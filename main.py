class Personne:
    def __init__(self, prenom, nom, age):
        self.nom = nom
        self.age = age
        self.prenom = prenom

    def __str__(self):
        return self.prenom + " " + self.nom + " a " + str(self.age) + " ans"


Henri = Personne("Henri", "Salard", 21)

print(Henri)

class Matrice:
    def __init__(self):
        self.largeur = 0
        self.hauteur = 0
        self.contenu = []

    def ajouterElement(self, element, ligne, colonne):
        if self.largeur < colonne-1 or self.hauteur < ligne-1 or ligne == 0 or colonne == 0:
            print("Erreur taille de la matrice")
            return
        else:
            if self.largeur == colonne-1:
                self.largeur = colonne
                for boucle in range(1,self.hauteur):
                    self.contenu[boucle * (colonne-1)] = 0 # on remplit la nouvelle colonne de zero

            if self.hauteur == ligne-1:
                self.hauteur = ligne+1
                for boucle in range(1,self.largeur):
                    self.contenu[boucle * (ligne-1)] = 0 # on remplit la nouvelle ligne de zero

            indice = ligne * colonne # l'indice de l'element dans la liste
            self.contenu[indice] = element

    def lireElement(self, ligne, colonne):
        return self.contenu[ligne*colonne]




M1 = Matrice()
M1.ajouterElement(10,1,1)


