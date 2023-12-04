# Solution: 32001

with open("input.txt", "r") as f:
    cards = list(map(lambda x : x.strip().split(" | "), f.readlines()))

count = 0
for card in cards:
    winning_numbers = set(map(int, card[1].split(" ")))
    personal_numbers = set(map(int, card[2].split(" ")))
    
    match_ = len(winning_numbers.intersection(personal_numbers))
    if match_ > 0:
        count += 2 ** (match_ - 1)

print(count)
