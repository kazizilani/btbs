#user defined data structures

#stack

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            print("The Stack Is Empty")
        else:
            self.stack.pop()
    def peek(self):
        print(self.stack[-1])


#Queue
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            print("The Queue Is Clear")
        else:
            self.queue.pop(0)

    def front(self):
        print(self.queue[0])

    