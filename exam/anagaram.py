def func(s,t):
	s=s.lower()
	t=t.lower()
	dict={}
	for i in s:
		if i not in dict and i!=' ':
			dict[i]=1
	# print(dict)
	for i in t:
		# print(i)
		if i not in dict and i!=' ':
			return print(False)
	return print(True)

func('anagram', 'nagaram')
func('Keep', 'Peek')
func('Mother In Law', 'Hitler Woman')
func('School Master', 'The Classroom')
func('ASTRONOMERS', 'NO MORE STARS')
func('Toss', 'Shot')
