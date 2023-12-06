def solver(inp_dict, data_file):
    total_time = inp_dict['Time']
    total_distance = inp_dict['Distance']
    winning_combos = len(total_time) * [0]
    losing_combos_det = ''
    winning_combos_det = ''
    for race in range(0, len(total_time)):
        record = total_distance[race]
        for time_held in range(0, total_time[race]):
            speed = time_held * 1
            time_remaining = total_time[race] - time_held
            distance = time_remaining * speed
            if distance > record:
                winning_combos[race] += 1
                winning_combos_det += f'total_time: {total_time[race]} time_held: {time_held} speed: {speed} distance: {distance} record: {record}\n'
            else:
                losing_combos_det += f'total_time: {total_time[race]} time_held: {time_held} speed: {speed} distance: {distance} record: {record}\n'
    answer = 1
    for win in winning_combos:
        answer *= win

    print(f'winning combos: {winning_combos}')
    print(f'product: {answer}')
    #print(f'winning: \n{winning_combos_det}')
    #print(f'losing: \n{losing_combos_det}')

    return
