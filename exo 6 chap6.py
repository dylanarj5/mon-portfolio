print("Enfin derniere ligne droite")

class Module:
    def __init__(self, titre, duree):
        self.titre = titre
        self.duree = duree
        
        
class Formation:
    def __init__(self, intitule):
        self.intitule = intitule
        self.modules = []
        
    def ajouter_module(self, module):
        self.modules.append(module)
        
    def duree_totale(self):
        return sum(module.duree for module in self.modules)
    
    
class Apprenant:
    def __init__(self, nom):
        self.nom = nom
        self.formations = []
        
    def s_inscrire(self, formation):
        if formation in self.formations:
            print(f"{self.nom} est deja inscrit(e) a {formation.intitule}.")
        else:
            self.formations.append(formation)
            print(f"{self.nom} s'est inscrit(e) a {formation.intitule}.")
            
    def afficher_parcours(self):
        print(f"\nParcours de {self.nom}:")
        if not self.formations:
            print("Aucune formation suivie.")
            return
        for formation in self.formations:
            print(f"Formation: {formation.intitule} {formation.duree_totale()}h")
            for module in formation.modules:
                print(f" -{module.titre} {module.duree}h")
                
                
                
python_formation = Formation("Python bases")
python_formation.ajouter_module(Module("Variable et types", 3))
python_formation.ajouter_module(Module("Condition et boucles", 4))
python_formation.ajouter_module(Module("Programmation orientee objet", 7))


web_formation = Formation("Developpement Web")
web_formation.ajouter_module(Module("HTML et CSS", 5))
web_formation.ajouter_module(Module("JavaScript", 6))
web_formation.ajouter_module(Module("Node.JS", 7))



Isma = Apprenant("Isma")
Fiderana = Apprenant("Fiderana")

Fiderana.s_inscrire(python_formation)
Fiderana.s_inscrire(web_formation)
Isma.s_inscrire(web_formation)
Isma.s_inscrire(web_formation)

Isma.afficher_parcours()
Fiderana.afficher_parcours()


print("Merci de m'avoir suivi durant ce parcours ")