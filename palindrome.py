#palindrome.py

 
x=-11011 

strx = str(x)
lenx = (int)(len(strx))-1
i = 0
while not lenx == i and lenx > 0:
	if not(strx[lenx] == strx[i]):
		print("false")
	i = i+1
	lenx = lenx-1
print("true")