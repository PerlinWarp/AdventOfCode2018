#Day 2 - Problem 1
twos = 0
threes = 0

path = "input.txt"

file = open(path, "r")

for line in file:
	dico = {}
	s = set(line)
	three = False 
	two = False
	for char in s:
		dico[char] = 0
	for char in line:
		dico[char] += 1
	for key in dico:
		if(two and three):
			break
		if(dico[key] == 2 and two == False):
			twos += 1
			two = True
		elif(dico[key] == 3 and three == False):
			threes +=1
			three = True
print("Threes*Twos:", threes * twos)
	