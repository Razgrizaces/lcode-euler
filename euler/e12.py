prime = [ True for i in range(MAX + 1)] 
# Function to mark the primes 
def sieve(): 
    # mark the primes 
	k = int(sqrt(MAX)) 
	for p in range(2,k,1):
		if (prime[p] == True): 
            # mark the factors of prime as non prime 
			for i in range(p * 2,MAX,p): 
				prime[i] = False
  

def numFactors(n):
	i = 1
	factors = 0
	print(triangle)
	while i < n/2 + 1:
		if n % i == 0:
			factors = factors+1
		i = i + 1
	return factors
	
def triangleNumbers(n):
	return n*(n-1)/2
i = 1
factors = 0
while factors != 500:
	triangle = triangleNumbers(i)
	factors = numFactors(triangle)
	print(triangle)
	if(factors > 100): print(factors)
	i = i + 1