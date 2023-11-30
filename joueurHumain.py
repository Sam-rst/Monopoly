from joueur import Joueur

class JoueurHumain(Joueur):
    
    def __init__(self, pseudo) -> None:
        super().__init__(pseudo)