# -*- coding: UTF-8 -*-
import copy

class Node:

    def __init__(self, matrix, moves, heuristic):
        # Definisco un costruttore che identifica un nodo
        self._matrix = matrix           #matrice corrente
        self._moves = moves             #mosse consetite
        self._heuristic = heuristic     #euristica applicata
        self._hScore = None

    def getMatrix(self):
        return copy.deepcopy(self._matrix)

    def getGScore(self):
        return len(self._moves)

    def getHScore(self):
        if self._hScore is None:
            self._hScore = self._heuristic.compute(self)
        return self._hScore

    def getFScore(self):
        return self.getGScore() + self.getHScore()

    def getMoves(self):
        return copy.copy(self._moves)

    def getHeuristic(self):
        return self._heuristic

    def getCoordByValue(self, value):
        i = 0
        for row in self._matrix:
            j = 0
            for cell in row:
                if cell == value:
                    return [i, j]
                j += 1
            i += 1