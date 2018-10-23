#Simplest solution would be to use two stacks (back, forward).
#Clicking the back button will pop from the back stack and push the current page on the forward stack (and go to the popped value on the back stack).
#Clicking on any link on a page (following a link) will clear the forward stack and push the current page on the back stack.
#Clicking on the forward button will pop from the forward stack and push the current page on the back stack (and go to the popped value on the forward stack).
#The back and forward buttons are disabled when the appropriate stack is empty.

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


class Browser:

    def __init__(self):
        self.f_s = Stack()
        self.b_s = Stack()
        self.cur_url = "Blank"

    def click(self, url):
        self.f_s = Stack()
        self.b_s.push(self.cur_url)
        self.cur_url = url

    def forward(self):
        if not self.f_s.isEmpty():
            self.b_s.push(self.cur_url)
            self.cur_url = self.f_s.pop()

    def backward(self):
        if not self.b_s.isEmpty():
            self.f_s.push(self.cur_url)
            self.cur_url = self.b_s.pop()


