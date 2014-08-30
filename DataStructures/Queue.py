class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]




