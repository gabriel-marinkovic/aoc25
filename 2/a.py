import math


with open("in.txt", "r") as f:
	data = f.read()

# data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

result = 0
for begin_end in data.split(","):
	begin_str, end_str = begin_end.split("-")
	begin, end = int(begin_str), int(end_str)

	for x in range(begin, end + 1):
		xstr = str(x)
		if len(xstr) % 2 != 0:
			continue
		half = len(xstr) // 2
		if xstr[:half] != xstr[half:]:
			continue
		result += x

print(result)
