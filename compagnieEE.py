from propriete import Propriete
from engine import Game

class CompagnieEE(Propriete):
    loyerParCompagnie = [0, 4, 10]
    
    def __init__(self, titre: str, prix: int, leQuartier : object) -> None:
        super().__init__(titre, prix, leQuartier)
        
    def calculerLoyer(self, game):
        """Lancer de dés x loyerParCompagnie"""
        if self.proprietaire is None or self.proprietaire == Game.joueurCourant or self.proprietaire.pseudo == "Banque":
            return f"Le loyer {self.titre} coute {CompagnieEE.loyerParCompagnie[0]}€"
        else:
            nbrCompagnies = self.leQuartier.combienDeProprieteDuQuartierPossedeCeJoueur(self.proprietaire)
            resultat = game.pairDeDes.count() * CompagnieEE.prixParCompagnie[nbrCompagnies]
            return f"Le loyer {self.titre} coute {resultat}€"