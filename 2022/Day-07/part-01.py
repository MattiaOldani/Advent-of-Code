# Solution: 1390824

def search(filesystem, current, all_size):
    total = 0
    for f in filesystem[current]:
        if f[1] > 0:
            total += f[1]
        else:
            search(filesystem, f"{current}{f[0]}/", all_size)
            total += all_size[len(all_size)-1]
    
    all_size.append(total)
    return


with open("input.txt", "r") as f:
    commands = list(map(lambda x : x.strip().split(" "), f.readlines()))

current = str()
filesystem = dict()
for cmd in commands:
    if cmd[0] == "$" and cmd[1] == "cd":
        match cmd[2]:
            case "..":
                current = current[:len(current)-1]
                index = current[::-1].find("/")
                current = current[::-1][index:][::-1]
            case "/":
                current = "/"
            case _:
                current = current + cmd[2] + "/"
    elif cmd[1] != "ls":
        try:
            name,size = cmd[1],int(cmd[0])
        except:
            name,size = cmd[1],0
        try:
            filesystem[current].append((name,size))
        except:
            filesystem[current] = [(name,size)]

all_size = list()
search(filesystem, "/", all_size)
print(sum(list(filter(lambda x : x <= 100000, all_size))))
