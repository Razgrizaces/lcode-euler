def squareSumDiff(a):
	i = 0
	sumSquare = 0
	squareSum = 0
	while not (i == a+1):
		sumSquare += i**2
		squareSum += i
		i = i +1
	squareSum = squareSum**2
	return squareSum-sumSquare

print(squareSumDiff(100))