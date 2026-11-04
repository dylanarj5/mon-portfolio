print("Bonjour, besoin d'un café?")

class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        
    def afficher_details(self):
        print(f"Titre: {self.titre} | Auteur: {self.auteur} | Annee: {self.annee}")
        
        
class Bibliotheque:
    def __init__(self):
        self.livres = []
        
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        
    def afficher_catalogue(self):
        print("===Catalogue de la bibliotheque===")
        for livre in self.livres:
            livre.afficher_details()
            
            
            
livre1 = Livre("Je repars de moi", "Chloé Miel", 2025)
livre2 = Livre("Je choisis d'avancer", "Laura Elsa", 2025)
livre3 = Livre("A travers ma fenêtre", "Ariana Godoy", 2023)
livre4 = Livre("A contre sens", "Mercedes Ron", 2018)



ma_bibliotheque = Bibliotheque()
ma_bibliotheque.ajouter_livre(livre1)
ma_bibliotheque.ajouter_livre(livre2)
ma_bibliotheque.ajouter_livre(livre3)
ma_bibliotheque.ajouter_livre(livre4)


ma_bibliotheque.afficher_catalogue()


print("Merci de m'avoir suivi (:")