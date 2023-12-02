# Solution: 2400

with open("input.txt", "r") as f:
    adapter = list(map(lambda x : int(x.strip()), f.readlines()))

adapter.sort()
adapter.insert(0, 0)
adapter.append(max(adapter) + 3)

diff_one = 0
diff_three = 0
for i in range(len(adapter)-1):
    match adapter[i+1] - adapter[i]:
        case 1:
            diff_one += 1
        case 2:
            ...
        case 3:
            diff_three += 1
        case _:
            ...

print(diff_one * diff_three)
