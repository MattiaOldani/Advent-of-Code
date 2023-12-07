# Solution: 254024898

import functools


@functools.total_ordering
class CamelHand:
    LABEL_ORDER = "AKQJT98765432"

    def __init__(self, hand: str, bid: int) -> None:
        self.hand = hand
        self.bid = bid
    
    def get_type(self) -> int:
        hand = self.hand
        cards = dict([[hand[i], hand.count(hand[i])] for i in range(len(hand))])
        
        values = sorted(cards.values())
        match len(cards):
            case 1:
                return 1
            case 2:
                return 2 if values == [1,4] else 3
            case 3:
                return 4 if values == [1,1,3] else 5
            case 4:
                return 6
            case _:
                return 7

    def __lt__(self, other) -> bool:
        self_type = self.get_type()
        other_type = other.get_type()
        if self_type != other_type:
            return other_type < self_type
        
        for self_label, other_label in zip(self.hand, other.hand):
            if self_label == other_label:
                continue
            
            self_label = CamelHand.LABEL_ORDER.find(self_label)
            other_label = CamelHand.LABEL_ORDER.find(other_label)
            return other_label < self_label
        
        return False

    def __eq__(self, other) -> bool:
        self_type = self.get_type()
        other_type = other.get_type()
        return self_type == other_type and self.hand == other.hand


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

hands = sorted([CamelHand(line[0], int(line[1])) for line in data])

print(sum(hands[i-1].bid * i for i in range(1, len(hands)+1)))
