path = "input.txt"

freq = 0
arr = set()

#Test case
#file = [3,3,4,-2,-4]
#file = [-6, +3, +8, +5, -6]
#file = [+7, +7, -2, -7, -4]

while True:
	file = open(path, "r")
	for line in file:
		freq += int(line)
		if(freq in arr):
			print(freq,"has already been found!")
			file.close()
			quit()
		arr.add(freq)
