class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop_stack(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)


my_stack = Stack()

print(my_stack.pop_stack())
print(my_stack.peek())

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.pop_stack())
print(my_stack.peek())

print(my_stack.size())
