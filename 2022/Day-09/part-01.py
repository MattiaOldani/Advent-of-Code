# Solution: 6339

with open("input.txt", "r") as f:
    moves = list(map(lambda x : x.strip().split(" "), f.readlines()))

DIRECTIONS = {
    "U" : [0,1],
    "D" : [0,-1],
    "R" : [1,0],
    "L" : [-1,0]
}

visited = { (0,0) : 0 }

tail_x,tail_y = 0,0
head_x,head_y = 0,0
for move in moves:
    step = DIRECTIONS[move[0]]
    count = int(move[1])

    for i in range(count):
        head_x += step[0]
        head_y += step[1]

        if not (abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1):
            if head_x == tail_x or head_y == tail_y:
                tail_x += step[0]
                tail_y += step[1]
            else:
                tail_x += (1 if head_x > tail_x else -1)
                tail_y += (1 if head_y > tail_y else -1)
            
            visited[(tail_x,tail_y)] = 0
    
print(len(visited))
