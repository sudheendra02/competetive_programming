def method(listt):
	listt.sort()
	listt=listt[::-1]
	# print(listt)
	for i in range(len(listt)-1):
		if(listt[i][0]==listt[i+1][0]) and (listt[i][1] > listt[i+1][1]):
			temp = listt[i+1]
			listt[i+1]=listt[i]
			listt[i]=temp
	out = []
	for i in listt:
		out.insert(i[1], i)
		
	
	return print(out)

# Input:

method([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]])

# Output:

# [[12,0],[11,1],[9,2],[6,3],[3,4],[1,5]]

method([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])

# Test case 3:

# Input:

method([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])

# Output:

# [[6,0], [5,1], [4,2], [3,3], [2,4], [1,5]]


