from copy import deepcopy


def solver(data_file):
    print(f'type of data: {type(data_file)}  length of data: {len(data_file)}')
    num_list = parser(data_file)
    final = sum(num_list)
    print(f'the sum is: {final}')
    return


def parser(data_file):
    num_list = []
    line = []
    for char_val in data_file:
        num_id = ord(char_val)
        if num_id != 10:
            line.append(char_val)
        elif num_id == 10:
            num_list.append(process(line))
            line = []

    return num_list


def process(line):
    last_line = deepcopy(line)
    line = ''.join(line)

    num_dict = dict()
    num_dict['zero'] = 0
    num_dict['one'] = 1
    num_dict['two'] = 2
    num_dict['three'] = 3
    num_dict['four'] = 4
    num_dict['five'] = 5
    num_dict['six'] = 6
    num_dict['seven'] = 7
    num_dict['eight'] = 8
    num_dict['nine'] = 9
    num_dict['0'] = 0
    num_dict['1'] = 1
    num_dict['2'] = 2
    num_dict['3'] = 3
    num_dict['4'] = 4
    num_dict['5'] = 5
    num_dict['6'] = 6
    num_dict['7'] = 7
    num_dict['8'] = 8
    num_dict['9'] = 9

    find_pos = [line.find(key) for key in num_dict.keys()]
    filtered_list_with_indices = [(index, value) for index, value in enumerate(find_pos) if value != -1]

    if filtered_list_with_indices:
        # Find the minimum and maximum values in the filtered list
        min_value = min(filtered_list_with_indices, key=lambda x: x[1])
        first_num = num_dict[list(num_dict)[min_value[0]]]

    last_line[min_value[1]] = ' '
    last_line = ''.join(last_line)
    find_pos = [last_line.rfind(key) for key in num_dict.keys()]
    filtered_list_with_indices = [(index, value) for index, value in enumerate(find_pos) if value != -1]
    if filtered_list_with_indices:
        # Find the minimum and maximum values in the filtered list
        max_value = max(filtered_list_with_indices, key=lambda x: x[1])
        last_num = num_dict[list(num_dict)[max_value[0]]]
    else:
        last_num = first_num

    print(first_num, last_num, line)
    return first_num * 10 + last_num
