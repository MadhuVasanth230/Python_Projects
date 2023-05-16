class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = [None]*size

    # Top Element
    def value_at_top(self):
        return self.stack[self.top]

    # Pushing Method
    def push(self, value):
        if self.top == self.size-1:
            return "Stack Is Full"
        else:
            self.top += 1
            self.stack[self.top] = value

    # Deleting Elements that Last Pushed
    def pop(self):
        if self.top == -1:
            return "Stack is Empty"
        else:
            popped_val = self.stack[self.top]
            self.top -= 1
            return popped_val

    # Printing Contents of the stack
    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i], end=" ")
        print()


# stack object passing with size
stack = Stack(3)

# Pushing Elements
stack.push(10)
stack.push(60)
stack.push(80)

# Top of the stack
print(stack.value_at_top())

# Traverse or printing Elements in the stack
stack.traverse()

# Popping or deleting elements from the stack
print(stack.pop())

print(stack.pop())

print(stack.pop())
