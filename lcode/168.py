class Solution:
	def convertToTitle(self, n: int) -> str:
		c = ""
		if (n == 0):
			return ""
		while(n > 26):
			if(n%26 > 0):
				ascii = int(64 + n%26)
				c += chr(int(ascii))
				n = int(n/26)
			else:
				c += chr(90)
				n = int(n/26)-1
		c += chr(int(n)+64)
		return c[::-1]
print(Solution.convertToTitle(Solution, 703))