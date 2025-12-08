import collections
import random


data = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

with open("in.txt", "r") as f:
    data = f.read()

data = data.strip()

points = list(map(lambda s: tuple(map(int, s.split(","))), data.split()))
count = len(points)

parent = list(range(count))
size = [1] * count


def find(idx):
    while idx != parent[idx]:
        parent[idx] = parent[parent[idx]]
        idx = parent[idx]
    return idx


def union(parent_idx, child_idx):
    pi = find(parent_idx)
    ci = find(child_idx)
    if pi == ci:
        print("already in same circuit:", points[parent_idx], points[child_idx])
        return
    if random.randint(0, 1) == 0:
        pi, ci = ci, pi

    size[pi] += size[ci]
    parent[ci] = pi
    print("connecting:", points[parent_idx], "<-", points[child_idx], "[new size:", size[pi])


distances_and_points = []
for a, (ax, ay, az) in enumerate(points):
    for b in range(a + 1, len(points)):
        (bx, by, bz) = points[b]
        distance = (ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2
        distances_and_points.append((distance, a, b))
distances_and_points.sort()

for distance, a, b in distances_and_points[:1000]:
    print(distance, a, b)
    union(a, b)

parent_to_count = {}
for point in range(count):
    parent_idx = find(point)
    parent_to_count[parent_idx] = size[parent_idx]

top3 = sorted(parent_to_count.values(), reverse=True)[:3]
print(top3)
print(top3[0] * top3[1] * top3[2])
