# Solution: 105

def tls(ip):
    for i in range(len(ip)-3):
        sub = ip[i:i+4]
        if sub[0] == sub[3] and sub[1] == sub[2] and sub[0] != sub[1]:
            return True
    
    return False


with open("input.txt", "r") as f:
    ips = list(map(lambda x : x.strip().split(" "), f.readlines()))

valid = 0
for ip in ips:
    square = False
    for i in range(1,len(ip),2):
        if tls(ip[i]):
            square = True
            break
    if square:
        continue

    for i in range(0,len(ip),2):
        if tls(ip[i]):
            valid += 1
            break
    
print(valid)
