#Day 2 - Problem 2
path = "testinput.txt"

file = open(path, "r")
lines = list(file)
arr = []
for s1 in range(0,len(lines)):
	for s2 in range(0,len(lines)):
		if(s1 != s2):
			#For any pair of the inputs
			#They are always the same length
			count = 0
			arr = list(lines[s1])
			for i in range(len(lines[s1])):
				if(count > 1):
					break
				if(lines[s1][i] != lines[s2][i]):
					count =+ 1
					diff = i
			del arr[i]
		print(arr)



