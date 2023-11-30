# MONOPOLY - main
from terrain import Terrain
from gare import Gare
from quartier import Quartier
from banque import Banque
from joueurHumain import JoueurHumain
from compagnieEE import CompagnieEE

try:
    #=====Création du quartier Bleu Foncé=====#
    quartierBleuFonce = Quartier("Bleu Foncé", prixParMaison=200)
    terrainChampsElysees = Terrain("Avenue des Champs Elysées", 350, [35, 175, 500, 1100, 1300, 1500], quartierBleuFonce)
    terrainRueDeLaPaix = Terrain("Rue de la Paix ", 400, [50, 200, 600, 1400, 1700, 2000], quartierBleuFonce)
    print(quartierBleuFonce)
    
    #=====Création des Gares=====#
    quartierDesGares = Quartier("Gares")
    gareSaintLazare = Gare("Gare Saint Lazare", 200, quartierDesGares)
    gareDuNord = Gare("Gare du Nord", 200, quartierDesGares)
    gareMontParnasse = Gare("Gare MontParnasse", 200, quartierDesGares)
    gareDeLyon = Gare("Gare de Lyon", 200, quartierDesGares)
    # print(quartierDesGares)
    
    #=====Création des Compagnies=====#
    
    #=====Création des joueurs=====#
    banque = Banque.getInstance()
    
    joueur1 = JoueurHumain("Samort")
    print(joueur1)
    
    listeQuartiers = [quartierBleuFonce, quartierDesGares]
    for quartier in listeQuartiers:
        for propriete in quartier.lesProprietes:
            propriete.acheteePar(banque)
    
    #=====Lancement du Jeu=====#
    print(quartierBleuFonce)
    joueur1.acheterPropriete(terrainChampsElysees, banque)
    print(quartierBleuFonce)
    
except ValueError as e:
    print("ATTENTION : ", e)