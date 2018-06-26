a=[1,2,3,4,5]
if (len(a)>=3):
	x=max(a)
	y=x
	a.remove(x)
	x=x*max(a)
	a.remove(max(a))
	x=x*max(a)
	if (len(a)>=2):
		y=y*min(a)
		a.remove(min(a))
		y=y*min(a)
		a.remove(min(a))
		print(max(x,y))
	else:
		print(x)
else:
	print("not enough values")