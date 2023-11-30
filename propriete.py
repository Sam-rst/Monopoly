from abc import ABC, abstractmethod
from banque import *

class Propriete(ABC):

    def __init__(self, titre : str, prix : int, leQuartier : object) -> None:
        """Constructeur de la classe Propriete qui demande en paramètre :
                - titre : le titre de la propriété
                - prix : le prix de la propriété
                """
        self._titre = titre
        self._prix = prix
        self._proprietaire = None
        
        self._leQuartier = leQuartier
        self.leQuartier.ajouterPropriete(self)
        
    def __str__(self) -> str:
        """Affiche l'objet"""
        if self.proprietaire == None:
            return f"{self.titre} ({self.prix}€) => Pas de propriétaire"
        else:
            return f"{self.titre} ({self.prix}€) => {self.proprietaire.pseudo}"
            
        
    @property
    def titre(self) -> str:
        """Permet de récupérer le titre de la propriété"""
        return self._titre

    @titre.setter
    def titre(self, value : str) -> None:
        """Permet d'insérer un nouveau titre de la propriété"""
        self._titre = value

    @property
    def prix(self) -> None:
        """Permet de récupérer le prix de la propriété"""
        return self._prix

    @prix.setter
    def prix(self, value):
        """Permet d'insérer le prix de la propriété"""
        if value < 0:
            raise ValueError("Valeur négative")
        else:
            self._prix = value
            
    @property
    def leQuartier(self) -> object:
        return self._leQuartier
    
    @leQuartier.setter
    def leQuartier(self, value : object) -> None:
        self._leQuartier  = value
        
    @property
    def proprietaire(self) -> object:
        return self._proprietaire
    
    @proprietaire.setter
    def proprietaire(self, value : object) -> None:
        self._proprietaire  = value
        
    
    @abstractmethod
    def calculerLoyer(self):
        """Permet de calculer le loyer"""
        pass
    
    def estAchetee(self):
        return self.proprietaire != None
    
    def acheteePar(self, proprietaire):
        self.proprietaire = proprietaire
    
    def addInQuartier(self, propriete : object) -> None:
        self.monQuartier = propriete