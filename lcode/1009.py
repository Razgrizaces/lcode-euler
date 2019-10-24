class Solution(object):
	def bitwiseComplement(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		if(N = 0)
			return 1
		bitNum = 0
		nTemp = N
		while nTemp is not 0:
			nTemp = (int)(nTemp/2)
			bitNum = bitNum+1
		complementNum = 2**bitNum-1
		output = N^complementNum
		print(output)
		return output
	bitwiseComplement(object, 0)
	bitwiseComplement(object, 3)