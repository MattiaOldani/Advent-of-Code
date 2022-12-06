# Solution: 3633500

with open("input.txt", "r") as f:
    binary = list(map(lambda x : x.strip(), f.readlines()))

binary = [[binary[i][j] for i in range(len(binary))] for j in range(len(binary[0]))]

gamma,epsilon,exp = 0,0,len(binary)-1
for column in binary:
    most = 1 if column.count('1') > column.count('0') else 0
    gamma += (most * 2**exp)
    epsilon += ((1-most) * 2**exp)
    exp -= 1

print(epsilon * gamma)
