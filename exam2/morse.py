def transform(words):
	code = {
	"A" :".-",
	"B" :"-...",
	"C" :"-.-.",
	"D" :"-..",
	"E" :".",
	"F" :"..-.",
	"G" :"--.",
	"H" :"....",
	"I" :"..",
	"J" :".---",
	"K" :"-.-",
	"L" :".-..",
	"M" :"--",	
	"N" :"-.",
	"O" :"---",
	"P" :".--.",
	"Q" :"--.-",
	"R" :".-.",
	"S" :"...",
	"T" :"-",
	"U" :"..-",
	"V" :"...-",
	"W" :".--",
	"X" :"-..-",
	"Y" :"-.--",
	"Z" :"--.."	}
	
	out = {}
	for i in words:
		i=i.upper()
		string = ""
		for j in range(len(i)):
			string = string + code[i[j]]
		if string not in out:
			out[string] = 1
	return print(len(out.keys()))

words = ["gin", "zen", "gig", "msg"]
# Output: 2
transform(words)
# Test case 2:
words = ["a", "z", "g", "m"]
# Output: 4
transform(words)

# Test case 3:
words = ["bhi", "vsv", "sgh", "vbi"]  
# Output: 3
transform(words)
# Test case 4:
words = ["a", "b", "c", "d"]  
# Output: 4
transform(words)
# Test case 5:
words = ["hig", "sip", "pot"]  
# Output: 2
transform(words)
