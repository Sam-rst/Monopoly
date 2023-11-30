from joueur import Joueur

class Banque(Joueur):
    cashInitial = 1000000
    pseudo = "Banque"
    _instance = None
    
    @staticmethod
    def getInstance():
        if Banque._instance is None:
            Banque._instance = Banque()
            Banque._instance._cash = Banque.cashInitial

        return Banque._instance

    def __init__(self) -> None:
        super().__init__(Banque.pseudo)

    def __str__(self):
        return f"{self.pseudo}"