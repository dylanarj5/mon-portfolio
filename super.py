print("Salu,oui c'est encore moi")

class Employee:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
    def se_presenter(self):
        print(f"nom: {self.nom}")
        print(f"age: {self.age} ans")
        

class Developpeur(Employee):
    def __init__(self, nom, age, langage_prefere):
        super().__init__(nom, age)
        self.langage_prefere = langage_prefere
        
    def se_presenter(self):
        super().se_presenter()
        print(f"langage prefere: {self.langage_prefere}")

dev = Developpeur("Soa", 25, "python")
dev.se_presenter()