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

max_len = max(map(len, number_lines))
for i in range(len(number_lines)):
    number_lines[i] += " " * (max_len - len(number_lines[i]))

number_groups = [[]]
for row in zip(*number_lines):
    line = "".join(row).strip()
    if line:
        number_groups[-1].append(int(line))
    else:
        number_groups.append([])

operators = op_line.split()

result = 0
for operator, operands in zip(operators, number_groups):
    if operator == "+":
        f = lambda x, y: x + y
    else:
        f = lambda x, y: x * y
    result += functools.reduce(f, operands)

print(result)
