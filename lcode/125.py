class Solution:
	def isPalindrome(self, s: str) -> bool:
		#lowercase everything
		#alphanumeric only = ascii value btwn 65->91
		i = 0
		j = 0
		s = s.upper()
		if(len(s) == 1):
			return True
		if(len(s) == 2):
			if(self.isAscii(self, s[0]) != self.isAscii(self, s[1])):
				return True
			elif not (self.isAscii(self, s[0]) and self.isAscii(self, s[1])):
				return True
			else:
				if(s[0] == s[1]):
					return True
				else:
					return False
		while i < len(s)/2:
			if(self.isAscii(self, s[i])):
				if(self.isAscii(self, s[::-1][j])):
					if (s[i] != s[::-1][j]):
						return False
					else:
						j = j+1
						i = i+1
				else:
					j = j+1
			else:
				i = i +1
		return True
		
	def isAscii(self, s: str) -> bool:
		c = ord(s)
		if ((c>=65 and c<=90) or (c>=48 and c<57)):
			return True
		else:
			return False
			
print(Solution.isPalindrome(Solution, ".,"))