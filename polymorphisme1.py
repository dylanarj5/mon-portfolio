print("Bonjour, bien dormi?")


from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def se_deplacer(self):
        pass
    
class Voiture(Transport):
    def se_deplacer(self):
        print("la voiture roule sur la route.")
        
class Avion(Transport):
    def se_deplacer(self):
        print("l'avion vole dans les airs.")
        
class Bateau(Transport):
    def se_deplacer(self):
        print("le bateau navigue sur l'eau.")
        
transports = [Voiture(), Avion(), Bateau()]

for transport in transports:
    transport.se_deplacer()

