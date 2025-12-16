import functools
import collections


data = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

data = """
you: a b
a: c
b: c
c: d e
d: out
e: out
"""

with open("in.txt", "r") as f:
    data = f.read()

data = data.strip()

in_to_out = collections.defaultdict(set)
for line in data.split("\n"):
    inn, rest = line.split(": ")
    outs = rest.split()
    in_to_out[inn].update(outs)

@functools.cache
def dfs(node):
    if node == "out":
        return 1
    paths = 0
    for next_node in in_to_out[node]:
        paths += dfs(next_node)
    return paths

print(dfs("you"))
