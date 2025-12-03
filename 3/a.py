import math


with open("in.txt", "r") as f:
    data = f.read()

# data = """
# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """.strip()

def max_idx_in_range(xs, a, b):
    return max(range(a, b), key=lambda i: xs[i])

result = 0
for bank in data.strip().split():
    first_idx = max_idx_in_range(bank, 0, len(bank) - 1)
    second_idx = max_idx_in_range(bank, first_idx + 1, len(bank))
    joltage = int(bank[first_idx] + bank[second_idx])
    result += joltage
    print(bank, "->", joltage)
print(result)


