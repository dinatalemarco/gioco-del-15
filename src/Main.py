from Heuristic import ManhattanDistance
from Game import Game




# Matrice sul quale vogliamo eseguire l'algoritmo

StartMatrix = [[1,6,2,3],
               [9,5,8,7],
               [14,11,0,4],
               [13,15,10,12]]

#StartMatrix = [[2,5,3,4],
#               [1,10,6,7],
#               [0,9,14,12],
#               [13,11,15,8]]

#StartMatrix = [[0,2,3,4],
#               [1,6,11,7],
#               [5,10,13,15],
#               [9,14,12,8]]

#StartMatrix = [[1,3,6,4],
#               [5,13,2,8],
#               [0,10,7,11],
#               [9,14,15,12]]


heuristic = ManhattanDistance() 

astar = Game()            				# Applico all'algoritmo A* l'euristica da usare
astar.start(StartMatrix, heuristic)     # Avvio il risolutore del gioco






