class Stack:
     def __init__(self) :
         self.data = []

     def isEmpty(self) :
         return self.data == []

     def push(self, data) :
         self.data.append(data)

     def pop(self) :
         return self.data.pop()

     def peek(self) :
         return self.data[len(self.data) - 1]

     def size(self) :
         return len(self.data)


mystack = Stack()

print mystack.isEmpty()

mystack.push(18)
mystack.push(16)
mystack.push(30)
mystack.push(29)

print mystack.size()

print mystack.pop()

print mystack.size()

print mystack.peek()
