def solver(limits, data_file):
    print(f'type of data: {type(data_file)}  length of data: {len(data_file)}')
    parsed_data = parser(limits, data_file)
    game_ids = []
    for row in parsed_data:
        game_ids.append(row['Game'])
    game_ids = set(game_ids)
    game_data = {}
    for game in game_ids:
        game_data[game] = [0, 0, 0]

    for row in parsed_data:
        game_data[row['Game']][0] = max(game_data[row['Game']][0], row['blue'])
        game_data[row['Game']][1] = max(game_data[row['Game']][1], row['green'])
        game_data[row['Game']][2] = max(game_data[row['Game']][2], row['red'])

    powers = [game_data[key][0] * game_data[key][1] * game_data[key][2] for key in game_data.keys()]
    print(powers)
    print(f'the sum is: {sum(powers)}')
    return


def parser(limits, data_file):
    data = []
    categs = limits.keys()
    while True:
        game_id = None
        delimiter_pos = data_file.find('\n')
        if delimiter_pos == -1:
            break
        line = data_file[0:delimiter_pos] + ';'
        game_id = int(line[4:line.find(':')])
        line = line[line.find(':')+1:]

        while True:
            draw_delimiter = line.find(';')
            if draw_delimiter == -1:
                break
            else:
                set_line = line[0: draw_delimiter] + ','
                counts = [0 for key in limits.keys()]
                set_data = dict()
                set_data['Game'] = game_id
                for key in limits.keys():
                    set_data[key] = 0
                while True:
                    for i, categ in enumerate(limits.keys()):
                        ball_delimiter = set_line.find(',')
                        if ball_delimiter == 0:
                            break
                        if set_line[0:ball_delimiter].find(categ) == -1:
                            set_data[categ] = set_data[categ] + 0
                        else:
                            set_data[categ] = set_data[categ] + int(set_line[0:set_line[0:ball_delimiter].find(categ)])
                            set_line = set_line[ball_delimiter+1:]

                    if len(set_line) == 0:
                        break

                data.append(set_data)
                line = line[draw_delimiter+1:]

        data_file = data_file[delimiter_pos+1:]

    return data



def process(line):
    return 10 * line[0] + line[-1]

