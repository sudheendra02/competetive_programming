def hamming(x,y):
	n=(x^y)
	# print(n)
	count=0
	while(n!=0):
		# print(n)
		if((n%2)==1):
			count=count+1
			# print(count)
		n=n//2
	return print(count)

# Test case: 1
x = 25
y = 30
hamming(x,y)
	# Output:	3
# Test case: 2
x = 1
y = 4
	# Output:	2
hamming(x,y)
# Test case: 3
x = 25
y = 30
	# Output:	3
hamming(x,y) 
# Test case: 4
x = 100
y = 250
	# Output:	5
hamming(x,y)
# Test case: 5
x = 1
y = 30
	# Output:	5
hamming(x,y)
# Test case: 6
x = 0
y = 255
	# Output:	8
hamming(x,y)
