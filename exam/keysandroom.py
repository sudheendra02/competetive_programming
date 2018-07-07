def roomandkeys(keys):
	rooms = len(keys)
	unlock=[1]
	for i in range(rooms-1):
		unlock.append(0)
	for i in range(len(keys)):
		if(unlock[i] == 1):
			for j in keys[i]:
				if j < len(unlock):
					unlock[j] = 1
	flag = True
	for i in unlock:		
		if i == 0:
			flag = False
			break
	
	print(flag)
	# print("================")
		
roomandkeys([[1], [0,2], [3]])
roomandkeys([[1,3], [3,0,1], [2], [0]])
roomandkeys([[1,2,3], [0], [0], [0]])
roomandkeys([[1], [0,2,4], [1,3,4], [2], [1,2]])
roomandkeys([[1], [2,3], [1,2], [4], [1], [5]])
roomandkeys([[1], [2], [3], [4], [2]])
roomandkeys([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]])
