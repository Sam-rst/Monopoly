from propriete import Propriete

class Terrain(Propriete):
    
    def __init__(self, titre: str, prix: int, loyers : list, leQuartier : object) -> None:
        super().__init__(titre, prix, leQuartier)
        
        self._loyers = loyers
        self._nbrMaisons = 0
        
    @property
    def loyers(self) -> list:
        return self._loyers

    @loyers.setter
    def loyers(self, value : list) -> None:
        self._loyers = value
        
    @property
    def nbrMaisons(self) -> int:
        return self._nbrMaisons
    
    @nbrMaisons.setter
    def nbrMaisons(self, value : int) -> None:
        self._nbrMaisons = value

    def calculerLoyer(self):
        return self.loyers[self.nbrMaisons]