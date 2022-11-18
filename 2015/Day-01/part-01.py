# Solution: 74

with open('input.txt', 'r') as f:
    movements = f.readline()
    print(movements.count('(') - movements.count(')'))
