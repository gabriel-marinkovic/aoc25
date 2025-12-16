#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "z3-solver",
# ]
# ///

import collections
import re

import z3


data = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

with open("in.txt", "r") as f:
    data = f.read()

data = data.strip()

machines = []

for line in data.split("\n"):
    m = re.match(r"\[(.*)\] (.*) \{(.*)\}", line)
    goal_str = m.group(1)
    buttons_str = m.group(2)
    joltages_str = m.group(3)

    goal = 0
    for i in range(len(goal_str)):
        if goal_str[len(goal_str) - i - 1] == "#":
            goal |= 1 << i

    buttons = []
    for m in re.finditer(r"\(([^\(\)]*)\)", buttons_str):
        buttons_list = list(map(int, m.group(1).split(",")))
        buttons.append(buttons_list)

    joltages = list(map(int, joltages_str.split(",")))

    machines.append((goal, buttons, joltages))

result = 0
for i, (_, buttons, joltages) in enumerate(machines):
    xs = [z3.Int(f"x{i}") for i in range(len(buttons))]
    opt = z3.Optimize()
    for x in xs:
        opt.add(x >= 0)
    for joltage_idx, joltage in enumerate(joltages):
        xs_for_joltage = [
            xs[i] for i in range(len(buttons))
            if joltage_idx in buttons[i]
        ]
        opt.add(sum(xs_for_joltage) == joltage)

    h = opt.minimize(sum(xs))
    assert opt.check() == z3.sat
    lb = opt.lower(h)
    assert z3.is_int_value(lb)
    result += lb.as_long()

print(result)
