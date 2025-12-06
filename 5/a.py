with open("in.txt", "r") as f:
    data = f.read()

# data = """
# 3-5
# 10-14
# 16-20
# 12-18
#
# 1
# 5
# 8
# 11
# 17
# 32
# """.strip()

data_intervals, data_ids = data.split("\n\n")

intervals = []
for line in data_intervals.split():
	intervals.append(tuple(map(int, line.split("-"))))

fresh = 0
for idd in map(int, data_ids.split()):
	for a, b in intervals:
		if a <= idd <= b:
			fresh += 1
			break

print(fresh)
