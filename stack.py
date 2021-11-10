class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if not self.stack:
            return True
        return False

    def push(self, element):
        self.stack.insert(0, element)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)