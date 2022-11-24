# Solution: 983

with open("input.txt", "r") as f:
    triangles = f.readlines()

counter = 0
for triangle in triangles:
    triangle = [x for x in triangle.strip().split(" ") if x != ""]
    triangle = list(map(lambda x : int(x), triangle))
    triangle.sort()
    counter += 1 if triangle[0]+triangle[1] >  triangle[2] else 0

print(counter)
