import functools
import collections


data = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

with open("in.txt", "r") as f:
    data = f.read()

data = data.strip()

in_to_out = collections.defaultdict(list)
for line in data.split("\n"):
    inn, rest = line.split(": ")
    outs = rest.split()
    in_to_out[inn].extend(outs)

@functools.cache
def dfs(node):
    if node == "out":
        return 1, 0, 0, 0

    node_paths_none = 0
    node_paths_dac = 0
    node_paths_fft = 0
    node_paths_both = 0
    for next_node in in_to_out[node]:
        paths_none, paths_dac, paths_fft, paths_both = dfs(next_node)
        node_paths_none += paths_none
        node_paths_dac += paths_dac
        node_paths_fft += paths_fft
        node_paths_both += paths_both

    if node == "dac":
        return 0, node_paths_none, 0, node_paths_fft
    elif node == "fft":
        return 0, 0, node_paths_none, node_paths_dac

    return node_paths_none, node_paths_dac, node_paths_fft, node_paths_both

print(dfs("svr"))


@functools.cache
def dfs2(node, found_dac, found_fft):
    if node == "out":
        return int(found_dac and found_fft)
    found_dac = found_dac or node == "dac"
    found_fft = found_fft or node == "fft"
    paths = 0
    for next_node in in_to_out[node]:
        paths += dfs2(next_node, found_dac, found_fft)
    return paths

print(dfs2("svr", False, False))
