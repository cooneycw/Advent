def solver(inp_dict, data_file):
    print(f'type of data: {type(data_file)}  length of data: {len(data_file)}')
    parser(data_file)

    valid_vals = []

    print(f'the sum is: {sum(valid_vals)}')
    return


def parser(data_file):
    row = 0
    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        # insert line processing code
        data_file = data_file[line_end+1:]
        row += 1

    return

