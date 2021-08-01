from collections import deque

class MyCircularQueue:
    
    def __init__(self, k: int):
        self.cq=deque()
        self.maxSize=k

    def enQueue(self, value: int) -> bool:
        if len(self.cq)==self.maxSize:
            return False
        else:
            self.cq.append(value)
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.cq.popleft()
            return True

    def Front(self) -> int:
        if not self.cq:
            return -1
        else:
            return self.cq[0]

    def Rear(self) -> int:
        if not self.cq:
            return -1
        else:
            return self.cq[-1]

    def isEmpty(self) -> bool:
        if self.cq:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if len(self.cq)==self.maxSize:
            return True
        else:
            return False