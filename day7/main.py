from collections import Counter
from dataclasses import dataclass
from enum import Enum
from typing import List


def count_duplicates(iterable):
    # Use Counter to count occurrences of each element
    element_counts = Counter(iterable)

    # Filter elements with count greater than 1 (duplicates)
    duplicates = {
        element: count
        for element, count in element_counts.items() if count > 1
    }

    return duplicates


def count_duplicates2(iterable):
    # Use Counter to count occurrences of each element
    element_counts = Counter(iterable)
    duplicates = {}
    j = 0
    for element, count in element_counts.items():
        if (element == 'J'):
            j = count
        else:
            duplicates[element] = count

    duplicates = {key: value + j for key, value in duplicates.items()}
    return duplicates


def get_type(card):
    card_deduplicate = set(card)
    if len(card_deduplicate) == 1:
        type = Type.FiveKind
    elif len(card_deduplicate) == 2:  # quad or fullhouse
        dupl = count_duplicates(card)
        if (len(dupl) == 1):
            type = Type.FourKind
        else:
            type = Type.FullHouse
    elif len(card_deduplicate) == 3:  # brelan or two pair
        dupl = count_duplicates(card)
        if (len(dupl) == 2):
            type = Type.TwoPair
        else:
            type = Type.ThreeKind
    elif len(card_deduplicate) == 4:
        type = Type.OnePair
    elif len(card_deduplicate) == 5:
        type = Type.HighCard
    return type


def get_type2(card):
    dupl = count_duplicates2(card)
    card = card.replace('J', '')
    card_deduplicate = set(card)
    if len(card_deduplicate) <= 1:
        type = Type.FiveKind
    elif len(card_deduplicate) == 2:  # quad or fullhouse
        if any(value == 4 for value in dupl.values()):
            type = Type.FourKind
        else:
            type = Type.FullHouse
    elif len(card_deduplicate) == 3:  # brelan or two pair
        if any(value == 3 for value in dupl.values()):
            type = Type.ThreeKind
        else:
            type = Type.TwoPair
    elif len(card_deduplicate) == 4:
        type = Type.OnePair
    elif len(card_deduplicate) == 5:
        type = Type.HighCard
    return type


def get_score(card, Joker=False):
    if (Joker):
        if (int(card.first_card) == 11):
            card.first_card = CardType.zero
        if (int(card.second_card) == 11):
            card.second_card = CardType.zero
        if (int(card.third_card) == 11):
            card.third_card = CardType.zero
        if (int(card.fourth_card) == 11):
            card.fourth_card = CardType.zero
        if (int(card.fifth_card) == 11):
            card.fifth_card = CardType.zero

    return ''.join([
        str(int(card.first_card)).zfill(2),
        str(int(card.second_card)).zfill(2),
        str(int(card.third_card)).zfill(2),
        str(int(card.fourth_card)).zfill(2),
        str(int(card.fifth_card)).zfill(2)
    ])


class Type(Enum):
    FiveKind = 7
    FourKind = 6
    FullHouse = 5
    ThreeKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1


class CardType(Enum):
    A = (14, 'A')
    K = (13, 'K')
    Q = (12, 'Q')
    J = (11, 'J')
    T = (10, 'T')
    Nine = (9, '9')
    Eight = (8, '8')
    Seven = (7, '7')
    Six = (6, '6')
    Five = (5, '5')
    Four = (4, '4')
    Three = (3, '3')
    two = (2, '2')
    zero = (0, '0')

    def __str__(self):
        return self.value[1]

    def __int__(self):
        return self.value[0]

    @classmethod
    def from_string(cls, s):
        for type in cls:
            if type.value[1] == s:
                return type
        raise ValueError(cls.__name__ + ' has no value matching "' + s + '"')


@dataclass
class Hand:
    card: str
    bid: int
    rank: int
    rank2: int
    type: Type
    type2: Type
    first_card: CardType
    second_card: CardType
    third_card: CardType
    fourth_card: CardType
    fifth_card: CardType
    score: int
    score_part2: int


@dataclass
class SetCard:
    list_hand: List[Hand]


setcard = SetCard([])
f = open('day7/input.txt')
lines = f.read().strip().splitlines()

for line in lines:
    card = line[0:5]
    first_card = CardType.from_string(line[0])
    second_card = CardType.from_string(line[1])
    third_card = CardType.from_string(line[2])
    fourth_card = CardType.from_string(line[3])
    fifth_card = CardType.from_string(line[4])
    bid = int(line[6:])
    type = get_type(card)
    type2 = get_type2(card)
    hand = Hand(card, bid, 0, 0, type, type2, first_card, second_card,
                third_card, fourth_card, fifth_card, 0, 0)
    hand.score = get_score(hand)
    hand.score_part2 = get_score(hand, True)
    setcard.list_hand.append(hand)

setcard.list_hand.sort(key=lambda x: x.type.value, reverse=True)
total_1star = 0
total_2star = 0

part1List: List[Hand] = []
part2List: List[Hand] = []
for i in Type:
    a = list(filter(lambda item: item.type == i, setcard.list_hand))
    a.sort(key=lambda x: x.score, reverse=True)

    b = list(filter(lambda item: item.type2 == i, setcard.list_hand))
    b.sort(key=lambda x: x.score_part2, reverse=True)
    part1List.extend(a)
    part2List.extend(b)

for i, hand in enumerate(part1List):
    hand.rank = 1000 - i

for i, hand in enumerate(part2List):
    hand.rank2 = 1000 - i

for i in part1List:
    total_1star = total_1star + i.rank * i.bid

for i in part2List:
    total_2star = total_2star + i.rank2 * i.bid

print(f"star 1: total {total_1star}")
print(f"star 2: total {total_2star}")
