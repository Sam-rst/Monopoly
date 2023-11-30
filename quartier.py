from propriete import Propriete

class Quartier:
    def __init__(self, nom : str, prixParMaison=None) -> None:
        self._nom = nom
        self._lesProprietes = []
        self._prixParMaison = prixParMaison
        
    def __str__(self):
        resultat = f"Quartier {self.nom.upper()} - {self.nbrProprietes()} propriétés : \n"
        for propriete in self.lesProprietes:
            resultat += f"  ({self.nom.upper()}) {str(propriete)} \n"
        return resultat
    
    @property
    def nom(self) -> str:
        return self._nom
    
    @nom.setter
    def nom(self, value : str) -> None:
        self._nom = value
    
    @property
    def lesProprietes(self) -> list:
        return self._lesProprietes
    
    @lesProprietes.setter
    def lesProprietes(self, value : list) -> None:
        self._lesProprietes = value
        
    @property
    def prixParMaison(self):
        return self._prixParMaison

    @prixParMaison.setter
    def prixParMaison(self, value):
        self._prixParMaison = value
        
    def ajouterPropriete(self, value : object) -> None:
        self._lesProprietes.append(value)
        
    def nbrProprietes(self):
        return len(self.lesProprietes)
    
    def combienDeProprieteDuQuartierPossedeCeJoueur(self, joueur : object) -> int:
        """Je suis un super commentaire"""
        nbProprietes = 0
        for propriete in self.lesProprietes:
            if propriete.joueur == joueur:
                nbProprietes += 1
        return nbProprietes
    
    def possedeToutLeQuartier(self, joueur):
        if self.nbrProprietes() == self.combienDeProprieteDuQuartierPossedeCeJoueur(joueur):
            return True
        return False