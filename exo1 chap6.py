print("Bonjour, c'est encore moi votre Dylan (:")

class Moteur:
    def __init__(self, marque, puissance):
        self.marque = marque
        self.puissance = puissance
        
    def demarrer(self):
        print(f"Le moteur {self.marque} de {self.puissance} Ch demarre")
        
        
class Voiture:
    def __init__(self, modele, moteur):
        self.modele = modele
        self.moteur = moteur
        
    def demarrer(self):
        print(f"La voiture {self.modele} se prepare a demarer.....")
        self.moteur.demarrer()
        
        
moteur1 = Moteur("Nissan", 280)
voiture1 = Voiture("Skyline", moteur1)

moteur2 = Moteur("Toyota", 320)
voiture2 = Voiture("Supra", moteur2)

moteur3 = Moteur("Mazda", 275)
voiture3 = Voiture("RX7", moteur3)

voiture1.demarrer()
voiture2.demarrer()
voiture3.demarrer()
