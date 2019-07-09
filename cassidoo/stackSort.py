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

#prints bottom->top of a stack
def printStack(stackToPrint):
	tempStack = Stack()
	array = []
	while not(stackToPrint.isEmpty()):
		tempStack.push(stackToPrint.pop())
	while not(tempStack.isEmpty()):
		popped = tempStack.pop()
		array.append(popped)
		stackToPrint.push(popped)
	print(array)
	
def sortStackMax(inputStack, popStack):
	while not inputStack.isEmpty():
		#init popStack/ push if it's the max
		if popStack.isEmpty() or inputStack.peek() > popStack.peek():
			popStack.push(inputStack.pop())
		#if it isn't, we push it to a temp stack 
		else:
			#use a temp stack to push to
			tempStack = Stack()
			printStack(inputStack)
			printStack(popStack)
			while (not(popStack.isEmpty()) and inputStack.peek() < popStack.peek()):
				tempStack.push(popStack.pop())
			#fit the element in the right spot
			popStack.push(inputStack.pop())
			printStack(tempStack)
			#reset the stack
			while not tempStack.isEmpty():
				popStack.push(tempStack.pop())
	return popStack

def sortStackMin(inputStack, popStack):
	while not inputStack.isEmpty():
		#init popStack/ push if it's the max
		if popStack.isEmpty() or inputStack.peek() < popStack.peek():
			popStack.push(inputStack.pop())
		#if it isn't, we push it to a temp stack 
		else:
			#use a temp stack to push to
			tempStack = Stack()
			printStack(inputStack)
			printStack(popStack)
			while (not(popStack.isEmpty()) and inputStack.peek() > popStack.peek()):
				tempStack.push(popStack.pop())
			#fit the element in the right spot
			popStack.push(inputStack.pop())
			printStack(tempStack)
			#reset the stack
			while not tempStack.isEmpty():
				popStack.push(tempStack.pop())
	return popStack
	
print("sortMaxStack")
inputS = Stack()
popS = Stack()

inputS.push(10)
inputS.push(3)
inputS.push(8)
inputS.push(9)
inputS.push(4)
inputS.push(2)
inputS.push(6)

printStack(inputS)
sortStackMax(inputS, popS)
printStack(popS)

print("sortMinStack")
popS = Stack()

inputS.push(10)
inputS.push(3)
inputS.push(8)
inputS.push(9)
inputS.push(4)
inputS.push(2)
inputS.push(6)

printStack(inputS)
sortStackMin(inputS, popS)
printStack(popS)
