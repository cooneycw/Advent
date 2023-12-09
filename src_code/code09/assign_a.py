import copy


def solver(inp_dict, data_file):

    nested = parser(data_file)

    history = []
    for i, row in enumerate(nested):

        add_pos = 0
        new_row = [row]
        while True:
            diffs = [new_row[add_pos][j] - new_row[add_pos][j-1] for j, x in enumerate(new_row[add_pos]) if j > 0]
            new_row.append(diffs)
            if all(x == 0 for x in diffs):
                break
            add_pos += 1

        process_row = copy.deepcopy(new_row)
        for k in range(len(new_row)-1, -1, -1):
            if k == len(new_row) - 1:
                add_val = process_row[k][-1]
            else:
                add_val = l_extend_val
            extend_val = process_row[k][-1] + add_val
            process_row[k].append(extend_val)
            if k == 0:
                history.append(extend_val)
            l_extend_val = extend_val
        print(f'new_row: \n{new_row}')
        print(f'process_row: \n{process_row}')
        print(f'\n')

    print(f'len(nested): {len(nested)}  len(history): {len(history)}  history: {history}')
    print(f'Processed additions: {sum(history)}')
    return


def parser(data_file):
    row = 0
    nested = []

    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        nested.append([int(x) for x in line.split(' ')])
        data_file = data_file[line_end+1:]

    return nested


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


