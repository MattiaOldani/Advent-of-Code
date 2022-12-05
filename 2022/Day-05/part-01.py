# Solution: QMBMJDFTD
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
    for j in range(count):
        dst.append(src.pop())

msg = str()
for stack in stacks:
    msg += str(stack.pop())

print(msg)
