import puzzle
from datetime import datetime


def main(input):
    print('### day 22 ###')
    start1 = datetime.now()
    p1res = part1(input)
    stop1 = datetime.now()
    print(f'p1: {p1res}')

    start2 = datetime.now()
    p2res = part2(input)
    stop2 = datetime.now()
    print(f'p2: {p2res}')

    print(f'p1 took: {stop1 - start1}\np2 took: {stop2 - start2}')


def part1(input: str) -> int:
    decks = get_input(input)

    p1 = decks[0]
    p2 = decks[1]

    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        elif c2 > c1:
            p2.append(c2)
            p2.append(c1)
        else:
            raise Exception('duplicated card', c1)

    winner = p1 if p1 else p2
    return calc_score(winner)


def part2(input: str) -> int:
    decks = get_input(input)
    winner, winner_hand = recursive_combat(1, tuple(decks[0]), tuple(decks[1]))
    return calc_score(winner_hand)


def calc_score(winner):
    score = 0
    multiplier = len(winner)
    for i in range(len(winner)):
        score += multiplier * winner[i]
        multiplier -= 1
    return score


P1_NAME = 'p1'
P2_NAME = 'p2'


def recursive_combat(game: int,
                     p1: tuple[int],
                     p2: tuple[int]) -> (str, tuple[int]):
    round = 0
    p1_played_hands = set()
    p2_played_hands = set()

    while p1 and p2:
        round += 1
        if p1 in p1_played_hands or p2 in p2_played_hands:
            return P1_NAME, p1

        p1_played_hands.add(p1)
        p2_played_hands.add(p2)

        c1 = p1[0]
        p1_next_hand = p1[1:]
        c2 = p2[0]
        p2_next_hand = p2[1:]
        if c1 <= len(p1_next_hand) and c2 <= len(p2_next_hand):
            winner, _ = recursive_combat(game + 1, p1_next_hand[:c1], p2_next_hand[:c2])
            if winner == P1_NAME:
                p1 = p1_next_hand + (c1, c2)
                p2 = p2_next_hand
            elif winner == P2_NAME:
                p2 = p2_next_hand + (c2, c1)
                p1 = p1_next_hand
            else:
                raise Exception('No Winner', winner)
        else:
            if c1 > c2:
                p1 = p1_next_hand + (c1, c2)
                p2 = p2_next_hand
            elif c2 > c1:
                p2 = p2_next_hand + (c2, c1)
                p1 = p1_next_hand
            else:
                raise Exception('duplicated card', c1)

    return (P1_NAME, p1) if p1 else (P2_NAME, p2)


def get_input(input: str) -> list[list[int]]:
    deck_strings = input.split('\n\n')
    decks = []
    for deck_string in deck_strings:
        deck = []
        lines = deck_string.split('\n')
        for line_index in range(1, len(lines)):
            deck.append(int(lines[line_index]))
        decks.append(deck)
    return decks


def mod_input(match):
    w1, w2 = match
    return w2, w1


if __name__ == "__main__":
    main(puzzle.input)
