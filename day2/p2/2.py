#Day 2 - Problem 2
twos = 0
threes = 0

path = "testinput.txt"

file = open(path, "r")
lines = list(file)

for s1 in range(0,len(lines)):
	for s2 in range(0,len(lines)):
		if(s1 != s2):
			string = list(lines[s1])
			set1 = set(lines[s1])
			set2 = set(lines[s2])
			non_shared = set1.difference(set2)
			if(len(non_shared) == 1):
				non_shared = non_shared.pop()
				string.remove(non_shared)
				out = ''.join(string)
				print(out)
				quit()
		