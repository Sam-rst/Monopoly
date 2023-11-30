from random import randint

class Dice:
    nbrFaces = 6
    
    def __init__(self) -> None:
        self._value = self.roll()
        
    def __eq__(self, dice: object) -> bool:
        return self.value == dice.value
        
    def __str__(self) -> str:
        return f"[{self.value}]"
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
    
    def roll(self):
        self.value = randint(1, Dice.nbrFaces)


class PairOfDice:
    dice1 = None
    dice2 = None
    pair = None
    _instance = None
    
    @staticmethod
    def getInstance():
        if PairOfDice._instance is None:
            PairOfDice._instance = PairOfDice()
            PairOfDice.dice1 = Dice()
            PairOfDice.dice2 = Dice()
            PairOfDice.pair = (PairOfDice.dice1, PairOfDice.dice2)

        return PairOfDice._instance
    
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        if PairOfDice.isDouble():
            return f"{PairOfDice.dice1} {PairOfDice.dice2}   =>   DOUBLE"
        else:
            return f"{PairOfDice.dice1} {PairOfDice.dice2}"
    
    @property
    def dice1(self):
        return PairOfDice.dice1
    
    @property
    def dice2(self):
        return PairOfDice.dice2
    
    @property
    def pair(self):
        return PairOfDice.pair
    
    def roll(self):
        PairOfDice.dice1.roll()
        PairOfDice.dice2.roll()
        PairOfDice.pair = (PairOfDice.dice1, PairOfDice.dice2)
    
    def isDouble():
        return PairOfDice.dice1.value == PairOfDice.dice2.value
    
    def count(self):
        return PairOfDice.dice1.value + PairOfDice.dice2.value
    
if __name__ == "__main__":
    pairDeDes = PairOfDice.getInstance()
    pairDeDes.roll()
    print(pairDeDes)