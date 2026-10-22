print("Coucou, ceci est une code")

class Voiture:
    def __init__(self, marque, modele, immatriculation, disponible=True):
        self.marque = marque
        self.modele = modele
        self.immatriculation = immatriculation
        self.disponible = disponible
        
    def louer(self):
        if self.disponible:
            self.disponible = False
            print(f"{self.marque} {self.modele} est maintenant louee.")
        else:
            print(f"{self.marque} {self.modele}n'est pas disponible.")
            
    def retourner(self):
        self.disponible = True
        print(f"{self.marque} {self.modele} a ete retournee.")
        
    def afficher_infos(self):
        etat = "disponible" if self.disponible else "louee"
        print(f"{self.marque} {self.modele} {self.immatriculation} {etat}")
        
        
voiture1 = Voiture("hyundai","Terracan","3077 TBC")
voiture2 = Voiture("Kia","Pride",'3555 TBS')
voiture3 = Voiture("Nissan","Patrol","0960 TBJ")

voiture1.afficher_infos()
voiture2.louer()
voiture3.afficher_infos()
voiture1.retourner()

