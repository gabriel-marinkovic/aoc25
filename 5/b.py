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

data_intervals, _ = data.split("\n\n")

intervals = []
for line in data_intervals.split():
	intervals.append(tuple(map(int, line.split("-"))))

events = []
for a, b in intervals:
	events.append((a, False))
	events.append((b, True))
events.sort()

result = 0
curr_start = 0
curr_open_count = 0
for n, is_end in events:
	if curr_open_count == 0:
		assert not is_end
		curr_start = n
	curr_open_count += (-1 if is_end else 1)
	if curr_open_count == 0:
		assert is_end
		result += n - curr_start + 1

print(result)
