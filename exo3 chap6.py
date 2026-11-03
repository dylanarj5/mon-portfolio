print("Coucou, encore moi Dylan (:")

class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        
        
class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite
        
        
    def calculer_total(self):
        return self.produit.prix * self.quantite
    
    
    def afficher_commande(self):
        print("Produit:", self.produit.nom)
        print("Quantite:", self.quantite)
        print("Montant total:", self.calculer_total())
        
        
produit1 = Produit("Clavier-mecanique", 120000)
produit2 = Produit("Souris", 25000)
produit3 = Produit("Ecran", 350000)
produit4 = Produit("Casque", 60000)

commande1 = Commande(produit1, 3)
commande2 = Commande(produit2, 5)
commande3 = Commande(produit3, 1)
commande4 = Commande(produit4, 2)


print("Total commande1:", commande1.calculer_total())
print("Total commande2:", commande2.calculer_total())
print("Total commande3:", commande3.calculer_total())
print("Total commande4:", commande4.calculer_total())

commande1.afficher_commande()
commande2.afficher_commande()
commande3.afficher_commande()
commande4.afficher_commande()