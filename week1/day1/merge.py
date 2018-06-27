a=[(5, 8), (1, 4), (6, 8)]
meeting = sorted(a)
# print(meeting)
merge = [meeting[0]]
# print(merge)
for start,end in meeting[1:]:
	i,j=merge[-1]
	if (start <= j):
		merge[-1]= i,max(end,j)
	else:
		merge.append((start,end))
print( merge)

