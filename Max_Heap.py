class MaxHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def insert(self,insert):
        ## function takes the heap itself and an integer to insert
        self.heapList.append(insert)

        ## increase the size tracker by one 
        self.currentSize = self.currentSize + 1

        ## call the percup function
        self.percUp(self.currentSize)

    def percUp(self,i):
        ## function takes the heap and an decreasing variable = size
        while i > 0:

            ## if a particular heaped value is greater than its parent:
            ## swap places 
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp

            ## iterate through the entire list
            i = i -1

    def findMax(self):
        ## return the first value in the heap
        return self.heapList[0]

    def delMax(self):
        ## return and pop the first value in the heap
        return self.heapList.pop(0)
        




    
h = MaxHeap()
h.insert(3)
h.insert(5)
h.insert(6)
h.insert(10)
h.insert(15)
h.insert(23)
h.insert(90)
h.findMax()
h.delMax()
