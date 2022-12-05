# Solution: NBTVTJNFJ
# Sono un pipone, ho modificato l'input

with open("input.txt", "r") as f:
    shit = list(map(lambda x : x.strip().split(" "), f.readlines()))

i = 0
stacks = list()
while shit[i] != [""]:
    stacks.append(shit[i])
    i += 1

for t in range(i+1,len(shit)):
    command = shit[t]
    count = int(command[0])
    src = int(command[1])-1
    dst = int(command[2])-1
    src = stacks[src]
    dst = stacks[dst]
    
    move = list()
    for x in range(count):
        move.append(src.pop())
    move.reverse()
    dst.extend(move)

msg = str()
for stack in stacks:
    msg += str(stack.pop())

print(msg)
