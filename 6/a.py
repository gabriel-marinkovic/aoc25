import functools


with open("in.txt", "r") as f:
    data = f.read()

# data = """
# 123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +
# """

lines = list(filter(None, data.split("\n")))
number_lines, op_line = lines[:-1], lines[-1]

m = []
for line in number_lines:
	numbers = list(map(int, line.split()))
	m.append(numbers)

operators = op_line.split()

result = 0
for operator, operands in zip(operators, zip(*m)):
	if operator == "+":
		f = lambda x, y: x + y
	else:
		f = lambda x, y: x * y
	result += functools.reduce(f, operands)

print(result)
