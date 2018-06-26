global a,minimum,maximum,mean,count
minimum,maximum,mean=-99999,-9999,0.0
count=0
a = {}
def insert(temp):
	global a,minimum,maximum,mean,count
	if temp not in a:
		a[temp]= 1
	else:
		a[temp]=a[temp]+1

	if (temp<minimum):
		minimum=temp
	elif (temp>maximum):
		maximum=temp
	mean = mean+temp
	count=count+1

def max1():
	global a
	return max(a)
def min1():
	global a
	return min(a)

def mean1():
	global mean,count
	return mean/count
def mode():
	return list(a.keys())[list(a.values()).index(max(a.values()))]

if __name__ == '__main__':
	
	insert(50)
	insert(80)
	insert(80)
	insert(30)

	print(max1(),min1(),mean1(),mode())
		