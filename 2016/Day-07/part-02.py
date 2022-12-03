# Solution: 258

def ssl(ip):
    res = list()
    for i in range(len(ip)-2):
        sub = ip[i:i+3]
        if sub[0] == sub[2] and sub[0] != sub[1]:
            res.append((sub[0], sub[1]))
    
    if len(res) == 0:
        return (False, None)
    else:
        return (True, res)


def check_ssl(ip,a,b):
    for i in range(len(ip)-2):
        sub = ip[i:i+3]
        if sub[0] == sub[2] and sub[0] == b and sub[1] == a:
            return True
    
    return False


with open("input.txt", "r") as f:
    ips = list(map(lambda x : x.strip().split(" "), f.readlines()))

valid = 0
for ip in ips:
    couples = list()
    for i in range(1,len(ip),2):
        ok,couple = ssl(ip[i])
        if ok:
            couples.extend(couple)
    if len(couples) == 0:
        continue

    couples = set(couples)
    for i in range(0,len(ip),2):
        exit_ = False
        for couple in couples:
            if check_ssl(ip[i],couple[0],couple[1]):
                valid += 1
                exit_ = True
                break
        if exit_:
            break
    
print(valid)
