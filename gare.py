from propriete import Propriete

class Gare(Propriete):
    
    prixParGare = 50
    
    def __init__(self, titre: str, prix: int, leQuartier : object) -> None:
        super().__init__(titre, prix, leQuartier)

    def calculerLoyer(self):
        """Nombre de gares du joueur x prixParGare"""
        return "Je caclule le loyer d'une gare"