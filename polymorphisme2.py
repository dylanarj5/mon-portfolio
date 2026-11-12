print("Coucou, partie2")

from math import pi

class Forme:
    nom = "Forme"
    def calculer_surface(self):
        pass
    
class rectangle(Forme):
    nom = "rectangle"
    
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    def calculer_surface(self):
        return self.longueur*self.largeur
    
class carre(Forme):
    nom = "carre"
    
    def __init__(self, cote):
        self.cote = cote
        
    def calculer_surface(self):
        return self.cote**2
    
class cercle(Forme):
    nom = "cercle"
    
    def __init__(self, rayon):
        self.rayon = rayon
        
    def calculer_surface(self):
        return pi*self.rayon**2
    
formes = [rectangle(5, 4), carre(5), cercle(5)]
for forme in formes:
    print(f"{forme.nom}: surface={round(forme.calculer_surface(),2)}")