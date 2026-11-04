print("Salu, c'est encore moi (:")

class Module:
    def __init__(self, titre, nombre_heures):
        self.titre = titre
        self.nombre_heures = nombre_heures
        
        
        
class Apprenant:
    def __init__(self, nom, identifiant):
        self.nom = nom
        self.identifiant = identifiant
        self.modules = []
        
    def inscrire(self, module):
        if module not in self.modules:
            self.modules.append(module)
            
    def afficher_modules(self):
        print(f"Apprenant: {self.nom} (ID: {self.identifiant})")
        if not self.modules:
            print("Aucun module.")
        for m in self.modules:
            print(f" -{m.titre} ({m.nombre_heures}h)")
            
            
            
python = Module("Python", 40)
bd = Module("Base de donnees", 30)
web = Module("Developpement web", 35)


a1 = Apprenant("Isma","A001")
a2 = Apprenant("Fiderana", "A005")

a1.inscrire(python)
a1.inscrire(bd)

a2.inscrire(python)
a2.inscrire(web)


a1.afficher_modules()
print()
a2.afficher_modules()