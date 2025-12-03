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
    digits = []
    digit_idx = -1
    for remaining in range(12, 0, -1):
        digit_idx = max_idx_in_range(
            bank, digit_idx + 1, len(bank) - remaining + 1)
        digits.append(bank[digit_idx])
    joltage = int("".join(digits))
    result += joltage
    print(bank, "->", joltage)
print(result)
