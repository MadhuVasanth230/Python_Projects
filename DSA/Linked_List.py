# Node Creation
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Linked List Creation
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    # length
    def __len__(self):
        return self.n

    # insert at head
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    # print magic method
    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result += str(curr.data)+"->"
            curr = curr.next
        return result[:-2]

    # insert at tail
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n += 1

    # insert at middle
    def insert_after(self, node_data, value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == node_data:
                break
            curr = curr.next
        if curr == None:
            return "Item Not Found"
        else:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1

    # clear/Emptying the Linked List
    def clear(self):
        self.head = None
        self.n = 0

    # delete at head
    def delete_head(self):
        if self.head == None:
            return "Empty Linked List"
        self.head = self.head.next
        self.n -= 1

    # delete at end
    def pop(self):
        if self.head == None:
            return "Empty Linked List"
        curr = self.head
        if curr.next == None:
            return self.delete_head()
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n -= 1

    # delete by value
    def remove(self, value):
        if self.head == None:
            return "Empty Linked List"
        if self.head.data == value:
            return self.delete_head()
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next == None:
            return "Item Not Found"
        else:
            curr.next = curr.next.next
            self.n -= 1

    # search by value
    def search(self, value):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == value:
                return pos
            curr = curr.next
            pos += 1
        return "Item Not Found"

    # search by index
    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        return "Index Error"


LL = LinkedList()

# insert at head
LL.insert_head(1)
LL.insert_head(2)
LL.insert_head(3)
LL.insert_head(4)

# insert at tail
LL.append(5)
LL.append(6)
LL.append(7)
LL.append(8)

# insert at middle
LL.insert_after("Madhu", 100)
LL.insert_after(6, 6.1)
LL.insert_after(8, 9)

# length
print(len(LL))

# pop
LL.pop()
LL.pop()
LL.pop()

# remove
LL.remove(1)
LL.remove(3)
LL.remove(100)

# search by Value
print(LL.search(6))

# search by index
print(LL[3])

# clear
LL.clear()


print(LL)
