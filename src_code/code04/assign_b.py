def solver(inp_dict, data_file):
    print(f'type of data: {type(data_file)}  length of data: {len(data_file)}')
    game_list, winning_list, elf_list = parser(data_file)
    win_multiplier = len(winning_list) * [1]

    winning_points = []
    i = 0
    for i, lottery in enumerate(winning_list):
        winning_set = set(lottery)
        elf_set = set(elf_list[i])
        winning_numbs = winning_set.intersection(elf_set)
        points = len(winning_numbs)

        card_dupl = [j for j in range(i + 1, 1 + i + points)]
        for q in range(win_multiplier[i]):
            for j in card_dupl:
                #print(f'i: {i} j: {j} q: {q} points: {points} win_multiplier: {win_multiplier} card_dupl: {card_dupl}')
                win_multiplier[j] = win_multiplier[j] + 1

    print(f'win_multiplier: {win_multiplier}')
    print(f'the sum is: {sum(win_multiplier)}')
    return


def parser(data_file):
    row = 0
    game_list = []
    winning_list = []
    elf_list = []
    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break

        first_pos = data_file.find(':')
        winning_pos = data_file.find('|')
        game_list.append([int(w) for w in data_file[4:first_pos].split(' ') if w != ''])
        winning_list.append([int(x) for x in data_file[first_pos + 1:winning_pos].split(' ') if x != ''])
        elf_list.append([int(y) for y in data_file[winning_pos+1:line_end].split(' ') if y != ''])

        data_file = data_file[line_end+1:]
        row += 1

    return game_list, winning_list, elf_list

