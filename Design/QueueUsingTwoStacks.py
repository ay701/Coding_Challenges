# Leetcode - 232. Implement Queue using Stacks
# Easy
#
# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Example:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# Notes:
#
# You must use only standard operations of a stack
# -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively.
# You may simulate a stack by using a list or deque (double-ended queue),
# as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example,
# no pop or peek operations will be called on an empty queue).


class Stack:
    def __init__(self):
        self.elements = []

    def pop(self):
        return self.elements.pop()

    def push(self, x):
        self.elements.append(x)

    def empty(self):
        return len(self.elements) == 0

    def peek(self):
        return self.elements[-1]


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def dequeue(self):

        if self.s1.empty() and self.s2.empty():
            raise Exception('There is no element.')
            return

        while not self.s1.empty():
            self.s2.push(self.s1.pop())

        return self.s2.pop()

    def enqueue(self, x):
        self.s1.push(x)


# driver code
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

