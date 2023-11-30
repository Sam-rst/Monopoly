# MONOPOLY - classe Game

from banque import Banque
from joueurHumain import JoueurHumain
from dice import PairOfDice

class Game:
    joueurCourant = None
    
    def __init__(self):
        self._banque = Banque.getInstance()
        self._pairDeDes = PairOfDice.getInstance()
        self._joueurs = []

        self._joueurCourantId = None

    @property
    def banque(self):
        return self._banque
    
    @property
    def pairDeDes(self):
        return self._pairDeDes
    
    @property
    def joueurs(self):
        return self._joueurs
    
    @property
    def joueurCourantId(self):
        return self._joueurCourantId
    
    @joueurCourantId.setter
    def joueurCourantId(self, value):
        self._joueurCourantId = value

    def ajouterJoueur(self, pseudo):
        nouveauJoueur = JoueurHumain(pseudo)
        self.joueurs.append(nouveauJoueur)

    def joueurSuivant(self):
        if len(self.joueurs) == 0:
            raise Exception ("Aucun joueur !")
        if self.joueurCourantId is None:
            self.joueurCourantId=0
        else:
            self.joueurCourantId = (self.joueurCourantId+1) % len(self.joueurs)

        Game.joueurCourant = self.joueurs[self.joueurCourantId]
        return Game.joueurCourant
        
    def start(self):        
        # todo : boucle infinie sur la liste des joueurs
        self.joueurSuivant()
        
