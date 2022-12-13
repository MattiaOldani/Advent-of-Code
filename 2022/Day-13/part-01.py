# Solution: 6623

def compare(left, right):
    if type(left) == int and type(right) == list:
        left = [left]
    elif type(left) == list and type(right) == int:
        right = [right]

    if type(left) == list and type(right) == list:
        for i in range(len(left)):
            try:
                l,r = left[i],right[i]
            except:
                return 1
            
            cmp = compare(l,r)
            if cmp != 0:
                return cmp
        
        return len(left) - len(right)
    else:
        return left - right


with open("input.txt", "r") as f:
    couples = list(map(lambda x : x.strip().split("\n"), f.read().split("\n\n")))

couples = list(map(lambda x : [eval(x[0]), eval(x[1])], couples))

in_order = 0
for i in range(len(couples)):
    left = couples[i][0]
    right = couples[i][1]
    in_order += (i+1) if compare(left, right) < 0 else 0

print(in_order)
