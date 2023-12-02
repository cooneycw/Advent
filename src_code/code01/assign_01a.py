def solver(data_file):
    print(f'type of data: {type(data_file)}  length of data: {len(data_file)}')
    final = sum(parser(data_file))
    print(f'the sum is: {final}')
    return


def parser(data_file):
    num_list = []
    line = []
    for char_val in data_file:
        num_id = ord(char_val)
        if 48 <= num_id <= 57:
            line.append(num_id - 48)
        if num_id == 10:
            num_list.append(process(line))
            print(num_list)
            line = []

    return num_list


def process(line):
    return 10 * line[0] + line[-1]

