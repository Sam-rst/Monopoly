from banque import *

class Joueur:
    cashInitial = 1500
    
    def __init__(self, pseudo) -> None:
        self._pseudo = pseudo
        self._cash = Joueur.cashInitial
        self._lesProprietes = []
    
    def __str__(self):
        message = f"{self.pseudo} possède {self.cash} € "
        if self.possedeDesProprietes():
            message +=  "et possède ces propriétés : \n"
            for propriete in self.lesProprietes:
                message += f"{str(propriete)}\n"
        else:
            message += "et ne possède pas de propriétés"
        return message
    
    @property
    def pseudo(self):
        return self._pseudo
    
    @pseudo.setter
    def pseudo(self, value):
        self._pseudo = value
    
    @property
    def lesProprietes(self):
        return self._lesProprietes
    
    @lesProprietes.setter
    def lesProprietes(self, value):
        self._lesProprietes = value
        
    @property
    def cash(self) -> int:
        return self._cash
    
    @cash.setter
    def cash(self, value) -> None:
        self._cash = value
        
    def acheterPropriete(self, propriete : object, leVendeur) -> None:
        self.lesProprietes.append(propriete)
        propriete.acheteePar(self)
        
    def vendre(self, propriete) -> None:
        self.lesProprietes.pop(self.rechercherProprieteID(propriete))
    
    def payer(self, montant, destinataire):
        self.cash -= montant
        destinataire.encaisse(montant)
        
    def peutConstruire(self, leTerrain):
        return leTerrain.leQuartier.possedeToutLeQuartier(self) and self.estSolvable()
        
    def encaisser(self, montant) -> None:
        self.cash += montant
        
    def possedeDesProprietes(self):
        return self.nbrProprietes() > 0
    
    def nbrProprietes(self):
        return len(self.lesProprietes)
    
    def estSolvable(self, leTerrain):
        return self.cash > leTerrain.leQuartier.prixParMaison
    
    def rechercherProprieteID(self, propriete : object) -> int:
        for i in range(len(self.lesProprietes)-1):
            if self.lesProprietes[i] == propriete:
                return i
        return