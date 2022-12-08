# Solution: 479400

def scenic_score(line, p):
    right = line[p+1:]
    left = line[:p][::-1]

    score1 = 0
    for v in right:
        score1 += 1
        if v >= line[p]:
            break
    
    score2 = 0
    for v in left:
        score2 += 1
        if v >= line[p]:
            break
    
    return score1 * score2


with open("input.txt", "r") as f:
    trees = list(map(lambda x : [int(t) for t in x.strip()], f.readlines()))

scores = list()
for i in range(1,len(trees)-1):
    for j in range(1,len(trees[i])-1):
        score = scenic_score(trees[i], j)
        score *= scenic_score([trees[t][j] for t in range(len(trees))], i)
        scores.append(score)

print(max(scores))
