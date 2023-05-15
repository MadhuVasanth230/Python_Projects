class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.n = 0

    # Empty Stack or Not
    def isempty(self):
        return self.top == None

    # Stack Element Added
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.n += 1

    # Stack Element Deleted
    def pop(self):
        if (self.isempty()):
            return "Empty Stack"
        else:
            data = self.top.data
            self.top = self.top.next
            self.n -= 1
            return data

    # Stack Top Element
    def peek(self):
        if (self.isempty()):
            return "Empty Stack"
        else:
            return self.top.data

    # Stack Size
    def size(self):
        return self.n

    # Stack Print
    def traverse(self):
        curr = self.top
        while curr != None:
            print(curr.data)
            curr = curr.next


# object creation
stack = Stack()

# elements Pushed
stack.push(1)
stack.push(2)
stack.push(3)

# size of stack
print(stack.size())

# stack elements printed
stack.traverse()

# stack top element
print(stack.peek())

# stack Last Element Poped
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
