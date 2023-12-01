# Solution: 55816

with open("input.txt", "r") as f:
    data = list(map(lambda x : list(x.strip()), f.readlines()))

'''
One-line per il meme

sum(el[0]*10 + el[-1] for el in list(map(lambda x : [int(y) for y in x if y.isdigit()], open("input.txt").readlines())))

sum(
    el[0]*10 + el[-1] for el in list(
        map(
            lambda x : [int(y) for y in x if y.isdigit()],
            open("input.txt").readlines()
        )
    )
)
'''

count = 0
for line in data:
    line = [int(x) for x in line if x.isdigit()]
    count += line[0]*10 + line[-1]

print(count)
