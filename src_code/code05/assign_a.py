def solver(inp_dict, data_file):
    print(f'type of data: {type(data_file)}  length of data: {len(data_file)}')
    game_list, winning_list, elf_list = parser(data_file)

    winning_points = []
    for i, lottery in enumerate(winning_list):
        winning_set = set(lottery)
        elf_set = set(elf_list[i])
        winning_numbs = winning_set.intersection(elf_set)
        points = 2**(len(winning_numbs) - 1)
        if points == 0.5:
            points = 0
        winning_points.append(points)
    print(f'winning_points: {winning_points}')
    print(f'the sum is: {sum(winning_points)}')
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

