# Solution: 5037841

from collections import defaultdict


with open("input.txt", "r") as f:
    cards = list(map(lambda x : x.strip().split(" | "), f.readlines()))

scratchcards_counter = defaultdict(lambda: 0)
for i in range(len(cards)):
    scratchcards_counter[i+1] = 1

for card in cards:
    card_number = int(card[0])
    copies = scratchcards_counter[card_number]

    winning_numbers = set(map(int, card[1].split(" ")))
    personal_numbers = set(map(int, card[2].split(" ")))
    
    match_ = len(winning_numbers.intersection(personal_numbers))
    for i in range(match_):
        scratchcards_counter[card_number+i+1] += copies

print(sum(x[1] for x in filter(lambda y : 1 <= y[0] <= len(cards), scratchcards_counter.items())))
