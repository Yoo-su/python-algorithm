from collections import deque

class Stack():
    def __init__(self) -> None:
        self.myStack=deque()

    def push(self,element):
        self.myStack.append(element)

    def pop(self):
        return self.myStack.pop()

    def top(self):
        tmp=self.myStack.pop()
        self.myStack.append(tmp)
        return tmp

    def empty(self):
        if self.myStack:
            return False
        else:
            return True

    
maStack=Stack()

maStack.push(1)
maStack.push(2)

print(maStack.top())
print(maStack.pop())
print(maStack.empty())