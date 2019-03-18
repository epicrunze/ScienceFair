a = open('Group2.csv', "r")
b = open("copy.csv", "w")
for line in a:
	print(line, file = b, end = "")
 
input()