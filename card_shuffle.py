#card suffle

import random
from collections import Counter

def shuffle(cards):

    shuffled_cards = []

    for i in range(len(cards)):
        card = random.choice(cards)
        shuffled_cards.append(card)
        cards.remove(card)

    return shuffled_cards

def testing():

    result_cards = []

    for i in range(1000):
        testing_cards = cards.copy()
        result_cards.append(''.join(shuffle(testing_cards)))

    print(dict(Counter(result_cards)))

def main():

    cards = [str(x)+'D' for x in range(1,11)]
    cards.extend(['JD','QD','KD'])
    cards.extend([str(x)+'C' for x in range(1,11)])
    cards.extend(['JC','QC','KC'])
    cards.extend([str(x)+'H' for x in range(1,11)])
    cards.extend(['JH','QH','KH'])
    cards.extend([str(x)+'S' for x in range(1,11)])
    cards.extend(['JS','QS','KS'])

    print(shuffle(cards))

if __name__ == '__main__':
    main()
