class Stack:

    stack = []

    def __init__(self):
        self.stack = []
 
    def isEmpty(self):
        return len(self.stack)==0

    def pop(self):
        return self.stack.pop()

    def push(self, element):
        self.stack.append(element)

    def top(self):
        return self.stack[-1]

class minMaxStack():

    def __init__(self):
        self.stack = Stack()
        self.minStack = Stack()
        self.maxStack = Stack()

    def getMin(self):
        return self.minStack.top()

    def getMax(self):
        return self.maxStack.top()

    def push(self,element):
        self.stack.push(element)
        
        if self.minStack.isEmpty():
            self.minStack.push(element)
        else:
            top = self.minStack.top()
            if element>top:
                self.minStack.push(top)
            else:
                self.minStack.push(element)

        if self.maxStack.isEmpty():
            self.maxStack.push(element)
        else:
            top = self.maxStack.top()
            if element>top:
                self.maxStack.push(element)
            else:
                self.maxStack.push(top)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
        self.maxStack.pop()

 
ms = minMaxStack()
ms.push(5)
ms.push(-5)
ms.push(2)
ms.push(-100)
ms.push(40)
print ms.getMin()
print ms.getMax()

