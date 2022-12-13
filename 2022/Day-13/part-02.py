# Solution: 23049

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
    couples = list(map(lambda x : x.strip(), f.readlines()))

couples = list(filter(lambda x : x != "", couples))
couples = list(map(eval, couples))
couples.append([[2]])
couples.append([[6]])

for i in range(len(couples)-1):
    min_ = i
    for j in range(i+1, len(couples)):
        if compare(couples[j], couples[min_]) < 0:
            min_ = j
    couples[i],couples[min_] = couples[min_],couples[i]

first = couples.index([[2]]) + 1
second = couples.index([[6]]) + 1
print(first * second)
