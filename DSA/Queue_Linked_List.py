class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.n = 0

    # Adding Elements
    def enqueue(self, value):
        new_node = Node(value)
        if self.front == None:
            self.front = new_node
            self.rear = self.front
            self.n += 1
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.n += 1

    # Deleting Elements
    def dequeue(self):
        if self.front == None:
            return "Empty Queue"
        else:
            self.front = self.front.next
            self.n -= 1

    # Print Elements
    def traverse(self):
        curr = self.front
        while curr != None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    # Checking Queue Empty or Not
    def isempty(self):
        return self.front == None

    # Size of the queue
    def size(self):
        return self.n

    # Front Element
    def front_item(self):
        if self.front == None:
            return "Empty Queue"
        else:
            return self.front.data

    # Last Element
    def rear_item(self):
        if self.front == None:
            return "Empty Queue"
        else:
            return self.rear.data


queue = Queue()

# enqueue
queue.enqueue(10)
queue.enqueue(9)
queue.enqueue(8)

# traverse
queue.traverse()

# front_item
print(queue.front_item())

# rear_item
print(queue.rear_item())

# dequeue
queue.dequeue()

queue.dequeue()

# size
print(queue.size())

# is empty or not
print(queue.isempty())

queue.dequeue()

print(queue.isempty())

queue.traverse()
