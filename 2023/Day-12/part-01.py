# Solution: 7407

def arrangements(springs: str, sizes: tuple[int]) -> int:
    if springs == "":
        return 1 if sizes == () else 0

    if sizes == ():
        return 1 if "#" not in springs else 0

    count = 0

    if springs[0] in ".?":
        count += arrangements(springs[1:], sizes)
    
    if springs[0] in "#?":
        if sizes[0] <= len(springs) and "." not in springs[:sizes[0]] and (len(springs) == sizes[0] or not springs[sizes[0]] == "#"):
            count += arrangements(springs[sizes[0]+1:], sizes[1:])
    
    return count


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(), f.readlines()))

count = 0
for line in data:
    springs, *sizes = line
    sizes = tuple([int(s) for s in sizes])
    
    count += arrangements(springs, sizes)

print(count)
