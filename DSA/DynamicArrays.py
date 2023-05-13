import ctypes


class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.createArray(self.size)

    # Array Creation
    def createArray(self, capacity):
        return (capacity*ctypes.py_object)()

    # Length
    def __len__(self):
        return self.n

    # Append
    def append(self, item):
        if self.n == self.size:
            self.resize(2*self.size)
        self.A[self.n] = item
        self.n += 1

    # Resize Array
    def resize(self, new_capacity):
        B = self.createArray(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity

    # Print List Items
    def __str__(self):
        result = ""
        for i in range(self.n):
            result += str(self.A[i])+","
        return "["+result[:-1]+"]"

    # Indexing
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return "Enter a valid Index"

    # pop
    def pop(self):
        if self.n > 0:
            temp = self.A[self.n-1]
            self.n = self.n-1
            return temp
        else:
            return "Empty List"

    # clear
    def clear(self):
        self.size = 1
        self.n = 0

    # find
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "Not Found"

    # insert
    def insert(self, position, item):
        if 0 <= position < self.n:
            if self.n == self.size:
                self.resize(self.size*2)
            for i in range(self.n, position, -1):
                self.A[i] = self.A[i-1]
            self.A[position] = item
            self.n += 1
        else:
            return "Enter valid index"

    # delete item
    def __delitem__(self, index):
        if 0 <= index < self.n:
            for i in range(index, self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1
        else:
            "Enter valid index"

    # remove item
    def remove(self, item):
        removeItem = self.find(item)
        if type(removeItem) == int:
            self.__delitem__(removeItem)
        else:
            return removeItem

    # sum of integers in the list
    def sum(self):
        sum = 0
        if self.n > 0:
            for i in range(self.n):
                if type(self.A[i]) == int or type(self.A[i]) == float:
                    sum += self.A[i]
        return sum

    # sort
    def sort(self):
        integerCount = 0
        stringCount = 0
        for i in range(self.n):
            if type(self.A[i]) == int or type(self.A[i]) == float:
                integerCount += 1
            elif type(self.A[i]) == str:
                stringCount += 1
        if integerCount == self.n or stringCount == self.n:
            return self.sortLogic()
        else:
            return "Unable to sort data with different data types"

    # Sorting Logic
    def sortLogic(self):
        iterationCount = self.n
        while iterationCount > 0:
            count = 0
            for i in range(self.n-1):
                if self.A[i] > self.A[i+1]:
                    temp = self.A[i]
                    self.A[i] = self.A[i+1]
                    self.A[i+1] = temp
                    count += 1
            if count == 0:
                break
            else:
                iterationCount -= 1
        return self.A

    # Min
    def min(self):
        minEl = self.sort()
        if type(minEl) == str:
            return "unable to find min element of list containing different data types"
        return minEl[0]

    # Max
    def max(self):
        maxEl = self.sort()
        if type(maxEl) == str:
            return "unable to find max element of list containing different data types"
        return maxEl[self.n-1]

    # Extend
    def extend(self, array):
        for i in range(len(array)):
            self.append(array[i])
        # return self.A

    # Merge
    def __add__(self, list2):
        self.extend(list2)
        return self


# object creation
list = MyList()

# Adding of Data
list.append("Madhu")
list.append(1)
list.append(10.0)
list.append("Vasanth")

# Length
print(len(list))

# Print List
print(list)

# Indexing
print(list[0])
print(list[1])
print(list[2])
print(list[3])

# find
print(list.find(10.0))
print(list.find("Hello"))
print(list.find("Madhu"))

# insert
print(list.insert(0, "Hello"))
print(list)

# delete item
del list[0]
print(list)

# remove
list.remove(10.0)
print(list)


# pop
print(list.pop())
print(list.pop())
print(list)

# clear
list.clear()
print(list)

# sum
list.append(89)
list.append(21)
list.append(10)


print(list)
print(list.sum())

# sort
list.clear()
list.append("D")
list.append("B")
list.append("C")
list.append("A")

list.clear()
list.append(1000)
list.append(1.9)
list.append(1)
list.sort()
print(list)


# min and max
print(list)
print(list.min())
print(list.max())

list.clear()

list.append("hello")
list.append("cello")
list.append("Bello")

print(list)
print(list.min())
print(list.max())


# extend
print(list)
list2 = MyList()
list2.append("Madhu")
list2.append("Vadhu")
list2.append("Chadhu")

list.extend(list2)
print(list)
print(list2)

# Merge
list3 = list+list2
print(list3)
