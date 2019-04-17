import re

def myAtoi(str):
	"""
	:type str: str
	:rtype: int
	"""
	# trim off the spaces
	strings = str.split(" ")
	print(strings)
	plus = "+"
	minus = "-"
	number = 0
	positive = 0
	wordCounter = 0
	for x in strings:
		length = 0
		if x == '':
			continue
		elif (x[0] == plus or x[0] == minus):
			if x[0] == plus:
				positive = 1
			else: 
				positive = -1
			length = 1
			x=x[1:]
		query = re.search('\A[0-9]+', x) # will trim everything, but we got the +/- sign
		if not query:
			return 0
		else:
			testNum = query.group(0)
			length = len(testNum)-1
			for c in testNum:				
				try:
					if wordCounter == 0:
						if (positive == 0):
							positive = 1
						number = number + (ord(c)-48)*(10**length)
						length = length - 1
				except:
					wordCounter = wordCounter +1
					break			
		if number >= 2**31 :
			if positive == 1:
				return 2**31*positive-1
			if positive == -1:
				return 2**31*positive
		else:
			return number*positive
	return 0