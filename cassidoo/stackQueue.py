class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class StackQueue:
	stack1 = Stack()
	stack2 = Stack()
	def __init__(self):
		print("initialized")
	def enqueue(self, item):
		self.stack1.push(item)
	def dequeue(self): #rets popped item
		while(not(self.stack1.isEmpty())):
			self.stack2.push(self.stack1.pop())
		output = self.stack2.pop() #pop item
		while(not(self.stack1.isEmpty())):
			self.stack1.push((self.stack2.pop()))
		return output

#I took the 
q = StackQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())