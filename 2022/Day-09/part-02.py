# Solution: 2541

with open("input.txt", "r") as f:
    moves = list(map(lambda x : x.strip().split(" "), f.readlines()))

DIRECTIONS = {
    "U" : [0,1],
    "D" : [0,-1],
    "R" : [1,0],
    "L" : [-1,0]
}

visited = { (0,0) : 0 }

rope = [[0,0] for i in range(10)]

for move in moves:
    step = DIRECTIONS[move[0]]
    count = int(move[1])

    for i in range(count):
        rope[0][0] += step[0]
        rope[0][1] += step[1]

        for i in range(1,10):
            head_x,head_y = rope[i-1][0],rope[i-1][1]
            tail_x,tail_y = rope[i][0],rope[i][1]

            if not(abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1):
                if head_x == tail_x or head_y == tail_y:
                    tail_x = (head_x + tail_x) // 2
                    tail_y = (head_y + tail_y) // 2
                else:
                    tail_x += (1 if head_x > tail_x else -1)
                    tail_y += (1 if head_y > tail_y else -1)

            rope[i][0] = tail_x
            rope[i][1] = tail_y

        visited[(rope[9][0],rope[9][1])] = 0
        
print(len(visited))
