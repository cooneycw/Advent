import copy
import math


def solver(inp_dict, data_file):

    data = parser(data_file)
    instructions = data['instructions']
    directions = data['directions']

    start = [key for key in directions.keys() if key[2] == 'A']
    last = 'Z'

    lcm_vals = len(start) * [None]
    for lcm_iter in range(len(start)):
        steps = 1
        curr = None
        while True:
            instruction = instructions[(steps - 1) % len(instructions)]
            if curr is None:
                curr = start
            new_curr = [None] * len(curr)
            stop_test = len(start) * [False]
            for j, curr_val in enumerate(curr):
                if instruction == 'L':
                    new_curr[j] = directions[curr_val][0]
                elif instruction == 'R':
                    new_curr[j] = directions[curr_val][1]
                if new_curr[j][2] == last:
                    stop_test[j] = True

            if stop_test[lcm_iter]:
                lcm_vals[lcm_iter] = steps
            # if steps == 18113 * 15043:
                print(f'instruction: {instruction}  curr: {curr}  new_curr:{new_curr}  steps: {steps}  stop_test: {stop_test}')
                break
            curr = copy.deepcopy(new_curr)
            steps += 1

    print(lcm_vals)

    answer = math.lcm(*lcm_vals)
    print(f'steps: {answer}')

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

