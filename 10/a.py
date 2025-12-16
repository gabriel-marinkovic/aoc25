import collections
import re


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
        buttons_mask = 0
        for x in buttons_list:
            buttons_mask |= 1 << (len(goal_str) - x - 1)
        buttons.append(buttons_mask)

    joltages = list(map(int, joltages_str.split(",")))

    machines.append((goal, buttons, joltages))

result = 0
for i, (goal, buttons, _) in enumerate(machines):
    print("machine", i)
    visited = set()
    q = collections.deque()
    q.append((0, 0))
    while q:
        state, count = q.popleft()
        visited.add(state)
        if state == goal:
            result += count
            break
        for button in buttons:
            new_state = state ^ button
            if new_state not in visited:
                q.append((new_state, count + 1))

print(result)
