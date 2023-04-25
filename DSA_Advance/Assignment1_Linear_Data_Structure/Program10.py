#10:Implement a queue using the stack data structure

class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, item):
        self.in_stack.append(item)
    
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("Queue is empty")
        return self.out_stack.pop()
    def is_empty(self):
        return not self.in_stack and not self.out_stack
    
    def size(self):
        return len(self.in_stack) + len(self.out_stack)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue()) 
print(q.dequeue())
q.enqueue(4)
print(q.dequeue())
print(q.dequeue()) 
print(q.is_empty()) 