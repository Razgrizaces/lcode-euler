#**Implement a function rotateArray(int arr, n) which rotates an array by n places.**
#Example: [1, 2, 3, 4, 5] rotated by 2 gives [4, 5, 1, 2, 3].

def rotateArray(array, n):
	if n == 0:	
		return array
	else:
		# easy solution 
		return (array[len(array)-n:] + array[:len(array)-n])
		
print(rotateArray([1,2,3,4,5], 1))
