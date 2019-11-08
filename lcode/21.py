#mergeTwoSortedLists

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None	
		
class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""	
		total = ListNode(0)
		head = ListNode(0)
		head.next = total
		if (l1 is None or l2 is None):
			return None
		elif (l1.val == l2.val):
			total.val = l1.val
			l1 = l1.next
			self.appendNode(self, total, l2.val)
			total = total.next
			l2 = l2.next
		elif (l1.val < l2.val):
			total.val = l1.val
			l1 = l1.next
		else:
			total.val = l2.val
			l2 = l2.next
		while (l1 is not None or l2 is not None):			
			print("L1")
			self.printLists(self, l1)
			print("/L1")
			print("L2")
			self.printLists(self, l2)
			print("/L2")
			if(l1 == None):
				self.appendNode(self, total, l2.val)
				total = total.next
				l2 = l2.next
			elif(l2 == None):
				self.appendNode(self, total, l1.val)
				total = total.next
				l1 = l1.next
			elif(l1.val == l2.val):
				self.appendNode(self, total, l1.val)
				total = total.next
				l1 = l1.next
				self.appendNode(self, total, l2.val)
				total = total.next
				l2 = l2.next
			elif(l1.val < l2.val):
				self.appendNode(self, total, l1.val)
				total = total.next
				l1 = l1.next
			else:
				self.appendNode(self, total, l2.val)
				total = total.next
				l2 = l2.next
		return head.next
	def printLists(self, node):
		while(node is not None):
			print(node.val)
			node = node.next
	def appendNode(self, list, value):
		append = ListNode(value)
		list.next = append
		return list
l11 = ListNode(1)
l12 = ListNode(1)
l13 = ListNode(4)
l21 = ListNode(1)
l22 = ListNode(2)
l23 = ListNode(2)

l11.next = l12
l12.next = l13
l21.next = l22
l22.next = l23

Solution.printLists(Solution, Solution.mergeTwoLists(Solution, l11, l21))