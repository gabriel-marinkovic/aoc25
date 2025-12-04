import copy

with open("in.txt", "r") as f:
    data = f.read()

# data = """
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """.strip()

grid = list(map(list, data.split()))
grid2 = copy.deepcopy(grid)

result = 0
while True:
	one_result = 0
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] != "@":
				continue
			rolls = 0
			for dy in (-1, 0, 1):
				for dx in (-1, 0, 1):
					yy = y + dy
					xx = x + dx
					if 0 <= yy < len(grid) and 0 <= xx < len(grid[y]) and \
							grid[yy][xx] == "@":
						rolls += 1
			if rolls < 4 + 1:
				one_result += 1
				grid2[y][x] = "."
	if one_result == 0:
		break
	grid, grid2 = grid2, copy.deepcopy(grid2)
	result += one_result

print(result)

