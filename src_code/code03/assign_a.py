def solver(inp_dict, data_file):
    print(f'type of data: {type(data_file)}  length of data: {len(data_file)}')
    parsed_data = parser(data_file)
    game_ids = []
    for row in parsed_data:
        game_ids.append(row['Game'])
    game_ids = set(game_ids)
    game_data = {}
    for game in game_ids:
        game_data[game] = [0, 0]

    for row in parsed_data:
        game_data[row['Game']][0] += 1
        valid_row = True
        for key in limits.keys():
            if limits[key] < row[key]:
                valid_row = False
                break
        if valid_row is True:
            game_data[row['Game']][1] += 1

    valid_game_ids = [key for key in game_data.keys() if game_data[key][0] == game_data[key][1]]
    print(valid_game_ids)
    print(f'the sum is: {sum(valid_game_ids)}')
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


