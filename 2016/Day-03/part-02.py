# Solution: 1836

with open("input.txt", "r") as f:
    triangles = f.readlines()

counter = 0
for i in range(0, len(triangles), 3):
    current = triangles[i:i+3]
    for j in range(3):
        current[j] = [x for x in current[j].strip().split(" ") if x != ""]
        current[j] = list(map(lambda x : int(x), current[j]))
    for j in range(3):
        triangle = [current[0][j], current[1][j], current[2][j]]
        triangle.sort()
        counter += 1 if triangle[0]+triangle[1] > triangle[2] else 0

print(counter)
