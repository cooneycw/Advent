import copy


def solver(inp_dict, data_file):

    data = parser(data_file)
    instructions = data['instructions']
    directions = data['directions']
    steps = None
    start = 'AAA'
    last = 'ZZZ'
    curr = None
    steps = 0
    while True:
        instruction = instructions[steps % len(instructions)]
        if curr is None:
            curr = start
            steps = 0
        if instruction == 'L':
            curr = directions[curr][0]
            steps += 1
        elif instruction == 'R':
            curr = directions[curr][1]
            steps += 1
        if curr == last:
            break

    print(f'steps: {steps}')

    return


def parser(data_file):
    row = 0
    ret_data = dict()
    directions = dict()

    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        if row == 0:
            instructions = list(line)
            ret_data['instructions'] = instructions
        if row == 1:
            pass
        if row > 1:
            left = line[line.find('(') + 1:line.find('(') + 1 + 3]
            right = line[line.find(')') - 3:line.find(')')]
            directions[line[0:3]] = (left, right)

        data_file = data_file[line_end+1:]
        row += 1
    ret_data['directions'] = directions
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


