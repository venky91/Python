class Stack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        self.stack.append(value)

        if len(self.minStack) == 0:
            self.minStack.append(value)

        else:
            if value < self.minStack[-1]:
                self.minStack.append(value)

    def pop(self):
        value = self.stack.pop()
        if value == self.minStack[-1]:
            self.minStack.pop()
        return value

    def peek(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

                

            


