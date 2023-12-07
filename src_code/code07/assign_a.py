import copy

def solver(inp_dict, data_file):

    data = parser(data_file)
    hands = []
    for row in data:
        hand = Hands(row[1], int(row[2]))
        hand.id_hand()
        hands.append((hand.hand_value, hand.bid))

    hands.sort(key=lambda x: x[0])
    answer = 0
    for i, hand in enumerate(hands):
        answer += hand[1] * (i+1)

    print(f'sum product: {answer}')
    #print(f'winning: \n{winning_combos_det}')
    #print(f'losing: \n{losing_combos_det}')

    return


def parser(data_file):
    row = 0
    ret_data = []

    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        item_01 = line[0:5]
        item_02 = line[6:line_end]
        ret_data.append((row,item_01, item_02))
        data_file = data_file[line_end+1:]
        row += 1

    return ret_data


class Hands:
    def __init__(self, hand, bid):
        self.hand = list(hand)
        self.bid = bid
        self.hand_value = 0
        self.hand_type = None
        self.pairs = 0
        self.triples = 0
        self.hand_rank = dict()
        self.hand_rank['five_of_a_kind'] = 7
        self.hand_rank['four_of_a_kind'] = 6
        self.hand_rank['full_house'] = 5
        self.hand_rank['three_of_a_kind'] = 4
        self.hand_rank['two_pairs'] = 3
        self.hand_rank['one_pair'] = 2
        self.hand_rank['one_of_a_kind'] = 1
        self.card_rank = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}

    def id_hand(self):
        hand_rev = copy.deepcopy(self.hand)
        hand_rev.reverse()
        for i, card in enumerate(hand_rev):
            self.hand_value += (100 ** i) * self.card_rank[card]
        cards = set(self.hand)
        card_cnts = len(cards) * [0]
        for j, face in enumerate(cards):
            for k, card in enumerate(self.hand):
                if face == card:
                    card_cnts[j] += 1
        self.pairs = sum([1 if cnt == 2 else 0 for cnt in card_cnts])
        self.triples = sum([1 if cnt == 3 else 0 for cnt in card_cnts])
        self.fours = sum([1 if cnt == 4 else 0 for cnt in card_cnts])
        if len(cards) == 1:
            self.hand_type = 'five_of_a_kind'
        elif len(cards) == 2:
            if self.fours == 1:
                self.hand_type = 'four_of_a_kind'
            else:
                self.hand_type = 'full_house'
        elif len(cards) == 3:
            if self.triples == 1 and self.pairs == 0:
                self.hand_type = 'three_of_a_kind'
            else:
                self.hand_type = 'two_pairs'
        elif len(cards) == 4:
            if self.pairs == 1:
                self.hand_type = 'one_pair'
        else:
            self.hand_type = 'one_of_a_kind'

        self.hand_value += (100 ** 5) * self.hand_rank[self.hand_type]


