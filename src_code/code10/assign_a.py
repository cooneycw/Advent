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
