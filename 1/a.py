with open("in.txt", "r") as f:
	data = f.read()

password = 0
dial = 50
for line in data.split("\n"):
	if not line:
		continue
	direction, count = line[0], int(line[1:])
	if direction == "R":
		dial += count
	else:
		dial -= count
	dial %= 100
	if dial == 0:
		password += 1

print(password)
