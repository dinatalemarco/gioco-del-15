# -*- coding: UTF-8 -*-
class LinkedList:

    def __init__(self):
        self.list = []
        self._history = {}

    def add(self, node):
        if str(node.getMatrix()) in self._history:
            # duplicate entry
            return
        self._history[str(node.getMatrix())] = True
        self._insort(node)

    def pop(self):
        return self.list.pop(0)

    def isEmpty(self):
        return len(self.list) == 0

    def _insort(self, node):
        lo = 0
        hi = len(self.list)
        while lo < hi:
            mid = (lo+hi)//2
            if node.getFScore() < self.list[mid].getFScore(): hi = mid
            else: lo = mid + 1
        self.list.insert(lo, node)