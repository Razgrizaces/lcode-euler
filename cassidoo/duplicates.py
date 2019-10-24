#**Write a function that takes in a string and returns the first duplicate character it finds.**
#Bonus points: write another function that takes in a string and removes all the duplicate characters.

def duplicateCharacter(string):
	characters = []
	for x in string:
		if x not in characters:
			characters.append(x)
		else:
			return 1
	return 0
	
print(duplicateCharacter("tes"))
