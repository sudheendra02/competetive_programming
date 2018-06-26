a=[1,2,3,4,5]
left=[]
right=[]
for i in a:
	left.append(i)
	right.append(i)
left[0]=1
right[len(a)-1]=1
for i in range(1,len(a)):
	left[i]=a[i-1]*left[i-1]
for x in range(len(a)-2,-1,-1):
	right[x]=right[x+1]*a[x+1]
for x in range(len(a)):
	right[x]=right[x]*left[x]
print(right)