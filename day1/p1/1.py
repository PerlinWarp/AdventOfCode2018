path = "input.txt"

file = open(path, "r")

freq = 0
for line in file:
	freq += int(line)

print(freq)