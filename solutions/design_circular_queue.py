class MyCircularQueue:
    def __init__(self, k: int):
        self.head = -1
        self.tail = -1
        self.list = [-1 for i in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.head == -1:
            self.head += 1
            
        self.tail = self.getNextIndex(self.tail)
        self.list[self.tail] = value
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = self.tail = -1
            return True
            
        self.head = self.getNextIndex(self.head)
        
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.list[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.list[self.tail]
        

    def isEmpty(self) -> bool:
        return self.head == self.tail and self.head == -1
        
    def isFull(self) -> bool:
        return self.getNextIndex(self.tail) == self.head
    
    def getNextIndex(self, index):
        if index + 1 == len(self.list):
            return 0
        
        return index + 1


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()