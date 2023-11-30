# MONOPOLY - main
from engine import Game
from quartier import Quartier
from terrain import Terrain
from gare import Gare
from compagnieEE import CompagnieEE

try:
    print("==========Création des quartiers==========\n")
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
    print(quartierDesGares)
    
    #=====Création des Compagnies=====#
    quartierDesCompagnies = Quartier("Compagnies")
    compagnieElectricite = CompagnieEE("Compagnie Electricité", 150, quartierDesCompagnies)
    compagnieEau = CompagnieEE("Compagnie Eau", 150, quartierDesCompagnies)
    print(quartierDesCompagnies)
    
    
    
    
    
    #=====Lancement du Jeu=====#
    print("\n \n ==========Lancement du Jeu==========")
    
    game = Game()
    game.ajouterJoueur("Samuel")
    game.ajouterJoueur("Paul")
    game.ajouterJoueur("Bastien")
    
    listeQuartiers = [quartierBleuFonce, quartierDesGares, quartierDesCompagnies]
    for quartier in listeQuartiers:
        for propriete in quartier.lesProprietes:
            propriete.acheteePar(game.banque)
    
    game.start()
    print(game.joueurCourant)
    
    game.joueurCourant.acheterPropriete(terrainChampsElysees, game.banque)
    
    game.joueurCourant.acheterPropriete(compagnieElectricite, game.banque)
    game.joueurCourant.acheterPropriete(terrainChampsElysees, game.banque)
    
    game.joueurCourant.acheterPropriete(gareDeLyon, game.banque)
    
    game.pairDeDes.roll()
    print(compagnieElectricite.calculerLoyer(game))
    
    game.pairDeDes.roll()
    print(compagnieEau.calculerLoyer(game))
    
    game.joueurSuivant()
    print(gareDuNord.calculerLoyer())
    print(gareDeLyon.calculerLoyer())
    print(terrainChampsElysees.calculerLoyer())
    
    game.joueurSuivant()
    game.joueurCourant.acheterPropriete(gareDuNord, game.banque)
    game.joueurCourant.acheterPropriete(gareSaintLazare, game.banque)
    game.joueurCourant.acheterPropriete(gareMontParnasse, game.banque)
    
    game.joueurSuivant()
    print(gareSaintLazare.calculerLoyer())
    print(gareDuNord.calculerLoyer())
    print(gareMontParnasse.calculerLoyer())
    
except ValueError as e:
    print("ATTENTION : ", e)