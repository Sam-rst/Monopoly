from propriete import Propriete

class CompagnieEE(Propriete):
    
    prixParCompagnie = [0, 4, 10]
    
    def __init__(self, titre: str, prix: int) -> None:
        super().__init__(titre, prix)
        
    def calculerLoyer(self):
        """Lancer de dés x loyerParCompagnie"""
        return "Je calcule le loyer d'une compagnie Eau et Electricité"
