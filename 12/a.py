with open("in.txt", "r") as f:
    data = f.read()

data = data.strip()

areas = data.split("\n\n")[-1]
result = 0
for i, area_and_presents_str in enumerate(areas.split("\n")):
    area_str, presents_str = area_and_presents_str.split(": ")
    a, b = map(int, area_str.split("x"))
    presents = list(map(int, presents_str.split(" ")))

    area = a * b
    if sum(presents) * 9 <= area:
        result += 1

print(result)
