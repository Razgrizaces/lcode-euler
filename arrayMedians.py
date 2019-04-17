#median of two sorted arrays

#merge sort algo
def mergeSort(m):
	if len(m) <= 1:
		return m
	left = []
	right = []
	i = 0
	for x in m:
		if i < (len(m)/2):
			left.append(x)
		else:
			right.append(x)
		i = i+1
	left = mergeSort(left)
	right = mergeSort(right)
	
	return merge(left,right)
	
def merge(left, right):
	result = []
	while not left == [] and not right == []:
		leftN = left[0]
		rightN = right[0]
		if(leftN <= rightN):
			result.append(leftN)
			left = left[1:] 
		else:
			result.append(rightN)
			right = right[1:]

	while not left == []:
		result.append(left[0])
		left = left[1:]
	while not right == []:
		result.append(right[0])
		right = right[1:]
	return result
	
nums1 = [1 , 3]
nums2 = [2]
nums = nums1+nums2
nums = mergeSort(nums)
mid = (int)(len(nums)/2)
print(mid)

if(len(nums) == 0):
	print(0)
elif(len(nums) == 1):
	print(nums[0])
elif(len(nums) % 2 == 1):
	print(nums[mid])
else:
	print((nums[mid] + nums[mid-1])/2)