print("Coucou,c'est encore une code")

class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
        
    def afficher_solde(self):
        print(f"titulaire: {self.titulaire}")
        print(f"solde dispo: {self.solde} Ariary")
        
        
class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde, taux_interet):
        super().__init__(titulaire, solde)
        self.taux_interet = taux_interet
        
    def afficher_solde(self):
        super().afficher_solde()
        print(f"taux d'interet: {self.taux_interet}%")
        
        
    def calculer_interet(self):
        return self.solde * self.taux_interet / 100
    
compte = CompteEpargne("Miora", 500000, 5)
compte.afficher_solde()

print(f"interet: {compte.calculer_interet():.0f} Ariary")

print("===Merci de m'avoir suivi, a la prochaine (: ===")