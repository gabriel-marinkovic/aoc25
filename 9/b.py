import collections


data = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

with open("in.txt", "r") as f:
    data = f.read()

data = data.strip()

points = list(map(lambda x: tuple(map(int, x.split(","))), data.split()))

def compress(coordinate_idx):
    orig_to_compressed = {}
    compressed_to_orig = {}
    xs = sorted(set(map(lambda x: x[coordinate_idx], points)))
    for i, x in enumerate(xs):
        compressed = 1 + 2 * i
        orig_to_compressed[x] = compressed
        compressed_to_orig[compressed] = x
    return orig_to_compressed, compressed_to_orig

x_orig_to_compressed, x_compressed_to_orig = compress(0)
y_orig_to_compressed, y_compressed_to_orig = compress(1)

points_compressed = []
for x, y in points:
    points_compressed.append(
        (x_orig_to_compressed[x], y_orig_to_compressed[y]))

xmax = max(map(lambda x: x[0], points_compressed)) + 1
ymax = max(map(lambda x: x[1], points_compressed)) + 1
grid = [["." for _ in range(xmax + 1)] for _ in range(ymax + 1)]

for (xa, ya), (xb, yb) in zip(
        points_compressed, points_compressed[1:] + [points_compressed[0]]):
    assert xa == xb or ya == yb
    xbegin, xend = (xa, xb) if xa < xb else (xb, xa)
    ybegin, yend = (ya, yb) if ya < yb else (yb, ya)
    while xbegin < xend:
        grid[ya][xbegin] = "x"
        xbegin += 1
    while ybegin < yend:
        grid[ybegin][xa] = "x"
        ybegin += 1
    grid[ya][xa] = "O"
    grid[yb][xb] = "O"

q = collections.deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    try:
        if grid[y][x] != ".":
            continue
        grid[y][x] = "@"
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                q.append((x + dx, y + dy))
    except IndexError:
        pass

def is_rect_ok(grid, xa, ya, xb, yb):
    xmin = min(xa, xb)
    xmax = max(xa, xb)
    ymin = min(ya, yb)
    ymax = max(ya, yb)
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            if grid[y][x] == "@":
                return False
    return True


def is_rect_ok_debug(grid, xa, ya, xb, yb):
    xmin = min(xa, xb)
    xmax = max(xa, xb)
    ymin = min(ya, yb)
    ymax = max(ya, yb)
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print(x, y)
            if grid[y][x] == "@":
                return False
            grid[y][x] = "!"
    return True


max_area = 0
for a in range(len(points_compressed)):
    xa, ya = points_compressed[a]
    for b in range(a + 1, len(points_compressed)):
        xb, yb = points_compressed[b]
        if not is_rect_ok(grid, xa, ya, xb, yb):
            continue

        oxa = x_compressed_to_orig[xa]
        oya = y_compressed_to_orig[ya]
        oxb = x_compressed_to_orig[xb]
        oyb = y_compressed_to_orig[yb]
        area = (abs(oxa - oxb) + 1) * (abs(oya - oyb) + 1)
        max_area = max(max_area, area)

print(max_area)
