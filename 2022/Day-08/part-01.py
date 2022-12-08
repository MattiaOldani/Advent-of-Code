# Solution: 1809

def check_direction(line, p):
    right = line[p+1:]
    left = line[:p]

    right = len(list(filter(lambda x : x < line[p], right))) == len(right)
    left = len(list(filter(lambda x : x < line[p], left))) == len(left)

    return right or left


with open("input.txt", "r") as f:
    trees = list(map(lambda x : [int(t) for t in x.strip()], f.readlines()))

visible = 2*len(trees) + 2*(len(trees[0])-2)
for i in range(1,len(trees)-1):
    for j in range(1,len(trees[i])-1):
        found = check_direction(trees[i], j)
        found = found or check_direction([trees[t][j] for t in range(len(trees))], i)

        visible += (1 if found else 0)

print(visible)
