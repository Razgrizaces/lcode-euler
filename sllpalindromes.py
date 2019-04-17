#sllPalindromes.py

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None	

tailNode = ListNode(-129)
midNode1 = ListNode(1)
midNode2 = ListNode(2)
midNode3 = ListNode(1)
head = ListNode(-129)
head.next = tailNode
midNode1.next = midNode2
midNode2.next = tailNode
#midNode3.next = tailNode

#if list is empty:
if head.val == 0:
	print( False)

#get last node
lastGap = -1
lastNode = head
while not lastNode.next is None:
	print(lastNode.next)
	lastNode = lastNode.next
	lastGap = lastGap + 1
if lastNode is None: #only two values
	print( True)

firstNode = head
while firstNode is not lastNode and firstNode.next is not None: 
	if not (firstNode.val == lastNode.val):
		print(False)
	firstNode = firstNode.next
	lastNode = head
	prevLastGap = 0
	while(prevLastGap is not lastGap and lastNode.next is not None):
		lastNode = lastNode.next
		prevLastGap = prevLastGap +1
	lastGap = prevLastGap-1
	print(firstNode.val, lastNode.val)
print(True)
		