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

max_area = 0
for a in range(len(points)):
    xa, ya = points[a]
    for b in range(a + 1, len(points)):
        xb, yb = points[b]
        area = (abs(xa - xb) + 1) * (abs(ya - yb) + 1)
        max_area = max(max_area, area)

print(max_area)
