"""Implementing heap data structure using one dimensioanl array """

class Heap:

    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self, data):

        if self.isFull():
            print("heap is full.")
            return

        self.currentPosition += 1
        self.heap[self.currentPosition] = data

        self.fixUpHeap(self.currentPosition)


    def fixUpHeap(self, index):

        parentIndex = 2*(index-1)//2

        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
            parentIndex = index-1//2


    def isFull(self):
        return self.currentPosition == Heap.HEAP_SIZE

    def printHeap(self):
        print(self.heap)

