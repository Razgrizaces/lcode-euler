#**Write a function where given a pattern string like "ABCCA" and an input string like "redyellowbluebluered", return true if and only if there's a one to one mapping of letters in the pattern to substrings of the input.**

#    > patternMatch('ABA', 'keyboardkey')
#    true
#    > patternMatch('AA', 'fishyfish')
#    false

#ABCCA - ending/front same, middle diff
#ABBC

def patternMatch(pattern, input):
	#A_A/like
	while pattern is not "":
		leftSubstring = [] 
		rightSubstring = []
		counter = 1
		print(input)
		while leftSubstring != input:
			leftSubstring = input[:counter] 
			rightSubstring = input[len(input)-counter:]
			print(leftSubstring, rightSubstring)
			if (leftSubstring == rightSubstring): #true, so break, remove the input and the pattern
				if(pattern[0] == pattern[-1]): 
					pattern = pattern[1:-1]
					input = input[counter:len(input)-counter]
					print(input)
					break
				else:
					return 0
			counter = counter +1
		if not(leftSubstring == rightSubstring) and pattern is not ""):
			return 0
			
		
	if pattern is "":
		return 1
	return 0

print(patternMatch("ABCCA", 'redyellowbluebluered'))

