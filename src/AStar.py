from LinkedList import LinkedList
from Node import Node

class AStar:


    def __init__(self,heuristic,g):
        self.heuristic = heuristic
        self.list = LinkedList()
        self.game = g

    def solve(self,matrix):

        # Creo il nodo iniziale con la matrice nelle condizioni iniziali
        node = Node(matrix, [], self.heuristic)
        self.list.add(node)

        step=0
        # Scorro tutta la lista di nodi fino ad arrivare alla fine
        while not self.list.isEmpty():
            # Pop best node from priority queque
            currentNode = self.list.pop()
            
            # Stampiamo lo step 
            self.game.getMatrix(step,currentNode.getMatrix())
            step = step+1
           
            # Verifico di essere arrivato sulla casella vuota
            if currentNode.getHScore() == 0:
                return currentNode.getMoves()
            # Compute child nodes and add them to the queue
            children = self.game.nextNode(currentNode)

            for child in children:
                self.list.add(child)
        
        return None
   