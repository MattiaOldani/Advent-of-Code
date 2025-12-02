# Solution: 21139440284

with open("input.txt", "r") as f:
    ranges = [x.strip().split("-") for x in f.read().strip().split(",")]

count = 0
for first, second in ranges:
    half = len(first) // 2
    first_half = int(first[:half]) if half > 0 else 1

    first = int(first)
    second = int(second)

    while True:
        current = int(2 * str(first_half))
        if first <= current <= second:
            count += int(2 * str(first_half))
        elif current > second:
            break

        first_half += 1

print(count)
