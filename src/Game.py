import time
from Node import Node
from AStar import AStar


class Game:

    def nextNode(self, node):

        children = []

        iSpace, jSpace = node.getCoordByValue(0)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i * j != 0 or i == j:
                    continue
                iSwap, jSwap = iSpace + i, jSpace + j
                if not (0 <= iSwap <= 3) or not (0 <= jSwap <= 3):
                    continue
                matrix = node.getMatrix()
                    
                matrix[iSpace][jSpace] = matrix[iSwap][jSwap]
                matrix[iSwap][jSwap] = 0
                moves = node.getMoves()
                moves.append( self.printMove(i, j))
          
                child = Node(matrix,moves,node.getHeuristic())
                children.append(child)
                
        return children
    
    
    def printMove(self, iDelta, jDelta):
        if iDelta == -1:
            return 'up'
        if iDelta == 1:
            return 'down'
        if jDelta == -1:
            return 'left'
        if jDelta == 1:
            return 'right'    
    


    def getMatrix(self, step ,matrix):
        print ("###### TABLE: %d ######" % (step))
        print "------------------------"
        for row in matrix:
            if row[0]==0 or row[1]==0 or row[2]==0 or row[3]==0:
                if row[0]==0:
                    print("| %3s | %3d | %3d |%3d |" % ("", row[1], row[2], row[3]))
                if row[1]==0:
                    print("| %3d | %3s | %3d |%3d |" % (row[0], "", row[2], row[3]))
                if row[2]==0:
                    print("| %3d | %3d | %3s |%3d |" % (row[0], row[1], "", row[3]))
                if row[3]==0:
                    print("| %3d | %3d | %3d |%3s |" % (row[0], row[1], row[2], "")) 
            else: print("| %3d | %3d | %3d |%3d |" % (row[0], row[1], row[2], row[3]))
        print "------------------------"


    def start(self, matrix ,heuristic):

        startTime = time.time()                           # Avio il tempo di esecuzione
        moves = heuristic.compute(Node(matrix, [], None)) # Numero di mosse minime
        
     
        res = AStar(heuristic, self).solve(matrix)

        if res == None:
            print('No solution found')
        else:
            # Sono arrivato alla soluzione e restituisco la lista dei movimenti
            print('L\'euristica impiegare minimo %d movimenti per essere completata.' % moves)        
            print('Tempo di risoluzione %d secondi.' % (time.time() - startTime))