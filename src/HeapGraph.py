# Nama : Muhammad Gilang Ramadhan
# NIM  : 13520137
# HeapGraph.py

class HeapGraph:
    """
    Class to Generates Heap Graph
    """
    def __init__(self):
        self.currSize = 0
        self.heapList = [(0, 0)]

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i // 2][1] > self.heapList[i][1]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i //= 2

    def percDown(self, i):
        while (i * 2) <= self.currSize:
            mc = self.ChildMinimum(i)
            if self.heapList[i][1] > self.heapList[mc][1]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def insert(self, k):
        self.heapList.append(k)
        self.currSize += 1
        self.percUp(self.currSize)

    def ChildMinimum(self, i):
        if (i*2 + 1 <= self.currSize):
            if self.heapList[i*2+1][1] <= self.heapList[i*2][1]:
                return i*2 + 1
            else:
                return i * 2
        else:
            return i * 2

    def extract_min(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currSize]
        self.currSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def delete(self, node):
        i = self.heapList.index(node)
        self.heapList[i] = self.heapList[self.currSize]
        self.currSize -= 1
        self.heapList.pop()
        self.percDown(i)

    def heapify(self, alist):
        i = len(alist) // 2
        self.currSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1
