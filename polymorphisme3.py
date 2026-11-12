print("Coucou, enfin partie 3 (:")

from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base
        
        @abstractmethod
        def calculer_salaire(self):
            return self.salaire_base
        
class developpeur(Employe):
    def __init__(self, nom, salaire_base, prime_technique):
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique
        
    def calculer_salaire(self):
        return self.salaire_base + self.prime_technique
    
    
class commercial(Employe):
    def __init__(self, nom, salaire_base, commission):
        super().__init__(nom, salaire_base)
        self.commission = commission
        
    def calculer_salaire(self):
        return self.salaire_base + self.commission
        
        
dev1 = developpeur("Ismael", 1500000, 350000)
dev2 = developpeur("Domer", 1000000, 200000)
com1 = commercial("Mialy", 850000, 150000)
com2 = commercial("Ranto kely", 700000, 90000)

employes = [dev1, dev2, com1, com2]

for employe in employes:
    print("employe:", employe.nom)
    print(f"salaire: {employe.calculer_salaire()} Ariary")
    print()