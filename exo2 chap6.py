print("Me revoila (:")

class Formation:
    def __init__(self, intitule, duree):
        self.intitule = intitule
        self.duree = duree
        
        
class Etudiant:
    def __init__(self, nom, age, formation):
        self.nom = nom
        self.age = age
        self.formation = formation
        
    def afficher_informations(self):
        print(f"Etudiant: {self.nom} | Formation: {self.formation.intitule}")
        
        
formation_info = Formation("Developpement logiciel", 24)


etudiant1 = Etudiant("Haley", 21, formation_info)
etudiant2 = Etudiant("Fiderana", 20, formation_info)
etudiant3 = Etudiant("Ismael", 24, formation_info)


etudiant1.afficher_informations()
etudiant2.afficher_informations()
etudiant3.afficher_informations()