with open("in.txt", "r") as f:
	data = f.read()


# 1 1 2 2 3 4 4 5 6
# data = """
# R50
# R50
# L50
# L50
# R75
# L50
# L25
# L75
# R50
# """
#
# data = """
# L50
# R101
# """

password = 0
dial = 50
for line in data.split("\n"):
	if not line:
		continue
	direction, count = line[0], int(line[1:])

	dial_before = dial
	if direction == "R":
		dial += count
	else:
		dial -= count

	password += abs(dial) // 100
	if dial_before > 0 and dial <= 0:
		password += 1

	dial %= 100
	print(line, password)

print("\n", password, sep="")
