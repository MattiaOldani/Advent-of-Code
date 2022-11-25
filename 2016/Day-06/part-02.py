# Solution: cnvvtafc

with open("input.txt", "r") as f:
    words = f.readlines()

columns = [''.join([w[j].strip() for w in words]) for j in range(len(words[0])-1)]

psw = str()
for column in columns:
    char = column[0]
    counter = column.count(char)
    for i in range(1, len(column)):
        if column.count(column[i]) < counter:
            char = column[i]
            counter = column.count(char)
    
    psw += char

print(psw)
