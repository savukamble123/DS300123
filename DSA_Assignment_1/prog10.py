#Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, item):
        self.items.append(item)
        if not self.min_items or item <= self.min_items[-1]:
            self.min_items.append(item)

    def pop(self):
        if not self.items:
            return None

        item = self.items.pop()
        if item == self.min_items[-1]:
            self.min_items.pop()

        return item

    def peek(self):
        if not self.items:
            return None

        return self.items[-1]

    def get_min(self):
        if not self.min_items:
            return None

        return self.min_items[-1]


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(1)
stack.push(9)
print("Smallest number in stack:", stack.get_min())
