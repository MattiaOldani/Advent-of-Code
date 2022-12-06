# Solution: 1275

with open("input.txt", "r") as f:
    signal = f.readline().strip()

for i in range(3,len(signal)):
    marker = [signal[t] for t in range(i-3,i+1)]
    no_dup = set(marker)
    if len(marker) == len(no_dup):
        print(i+1)
        break
