import copy
import math


def solver(inp_dict, data_file):

    input_data = parser(data_file)
    input_data = input_data[0]

    data_line = [int(x) for x in input_data.split()]

    subs = {}
    sub_count = {}

    for val in data_line:
        if val in subs:
            sub_count[val] += 1
        else:
            subs[val] = process_val(val)
            sub_count[val] = 1

    i = 1
    while i <= 75:
        print(i)
        static_key_list = list(sub_count.keys())
        new_subs = {}
        new_sub_count = {}
        for j, sub_key in enumerate(static_key_list):
            for sub_val in subs[sub_key]:
                if sub_val in new_subs:
                    new_sub_count[sub_val] = new_sub_count[sub_val] + sub_count[sub_key]
                else:
                    new_subs[sub_val] = process_val(sub_val)
                    new_sub_count[sub_val] = sub_count[sub_key]

        subs = copy.copy(new_subs)
        sub_count = copy.copy(new_sub_count)
        i += 1

    static_key_list = list(subs.keys())
    count = 0
    for key in static_key_list:
        count += sub_count[key]
    print(count)

def process_val(val):
    if val == 0:
        return [1]
    digits = len(str(val))  # using string length for simplicity
    if digits % 2 == 0:
        half = digits // 2
        divisor = 10 ** half
        return [val // divisor, val % divisor]
    else:
        return [2024 * val]

def parser(data_file):
    input_data = []

    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        input_data.append(line)
        data_file = data_file[line_end+1:]

    return input_data