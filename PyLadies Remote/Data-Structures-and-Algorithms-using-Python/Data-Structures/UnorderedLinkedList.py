class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newext):
        self.next = newext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        size = 0
        while current != None:
            size = size + 1
            current = current.getNext()

        return size

    def printList(self):
        current = self.head
        while current != None:
            print current.getData(),
            current = current.getNext()

    def search(self, data):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()

        else:
            previous.setNext(current.getNext())


mylist = UnorderedList()

mylist.add(18)
mylist.add(16)
mylist.add(30)
mylist.add(29)

print mylist.size()

print mylist.isEmpty()

print mylist.search(30)
print mylist.search(18163029)

mylist.remove(29)
print mylist.size()
print mylist.printList()
