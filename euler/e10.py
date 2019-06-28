def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True  

def sieveOfEratosthenes(num):
	#enum 1:num
	numbers = range(2,num)
	numArray = []
	sieveNumbers = []
	sieve = 2
	while sieve < num**0.5:	
		if(is_prime(sieve)):
			sieveNumbers.append(sieve)
			for x in numbers:
				if not(x % sieve == 0) and x != sieve:
					numArray.append(x)
			numbers = numArray
		numArray = []
		if sieve ==2: sieve = 3
		else: sieve = sieve+2
	for x in sieveNumbers:
		numbers.append(x)
	#numbers.sort()
	return numbers

def sumArray(array):
	sum = 0
	for x in array:
		if x == 0: return 0
		sum += x
	return sum

output = sieveOfEratosthenes(2000000)

print(output, sumArray(output))
