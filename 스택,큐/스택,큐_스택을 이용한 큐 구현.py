from collections import deque

class Queue:
    def __init__(self) -> None:
        self.q=deque()
    
    def push(self,x:int):
        self.q.append(x)

    def pop(self):
        tmp=self.q.popleft()
        return tmp

    def peek(self):
        tmp=self.q.popleft()
        self.q.appendleft(tmp)
        return tmp
    
    def empty(self):
        if self.q:
            return False
        else: 
            return True

