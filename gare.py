from propriete import Propriete
from engine import Game

class Gare(Propriete):
    
    loyerParGare = [0, 25, 50, 100, 200]
    
    def __init__(self, titre: str, prix: int, leQuartier : object) -> None:
        super().__init__(titre, prix, leQuartier)

    def calculerLoyer(self):
        """Nombre de gares du joueur x prixParGare"""
        if self.proprietaire is None or self.proprietaire == Game.joueurCourant or self.proprietaire.pseudo == "Banque":
            return f"Le loyer {self.titre} coute {Gare.loyerParGare[0]}€"
        else:
            nbrGares = self.leQuartier.combienDeProprieteDuQuartierPossedeCeJoueur(self.proprietaire)
            return f"Le loyer {self.titre} coute {Gare.loyerParGare[nbrGares]}€"