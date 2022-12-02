# Solution: 848

with open("input.txt", "r") as f:
    seats = list(map(lambda x : x.strip(), f.readlines()))

id_ = list()
for seat in seats:
    rows = 128
    max_,min_ = 127,0
    for i in range(7):
        rows = int(rows / 2)
        if seat[i] == "F":
            max_ = min_ + rows - 1
        else:
            min_ = min_ + rows
    rows = max_

    columns = 8
    max_,min_ = 7,0
    for i in range(7,10):
        columns = int(columns / 2)
        if seat[i] == "L":
            max_ = min_ + columns - 1
        else:
            min_ = min_ + columns
    
    id_.append(8 * rows + max_)

print(max(id_))
