import copy

def solver(inp_dict, data_file):
    total_time = inp_dict['Time']
    total_distance = inp_dict['Distance']

    interval_size = int(total_time**0.5)
    test_vals = [x for x in range(0, total_time, interval_size)]
    winning_int, win_det, lose_det = winning_combos_test(test_vals, interval_size, total_distance, total_time)
    ind = winning_int.index(1)
    if ind != 0:
        min_val_range = [test_vals[ind-1], test_vals[ind]]
    rev_winning = copy.deepcopy(winning_int)
    rev_test_vals = copy.deepcopy(test_vals)
    rev_winning.reverse()
    rev_test_vals.reverse()
    rev_ind = rev_winning.index(1)
    if rev_ind == 0:
        max_val_range = [rev_test_vals[rev_ind], total_time]
    else:
        max_val_range = [rev_test_vals[rev_ind], rev_test_vals[rev_ind - 1]]
    min_test_vals = range(min_val_range[0], min_val_range[1])
    win_min, _, _ = winning_combos_test(min_test_vals, 1, total_distance, total_time)
    max_test_vals = range(max_val_range[0], max_val_range[1])
    win_max, _, _ = winning_combos_test(max_test_vals, 1, total_distance, total_time)
    total_winners = sum(win_min) + sum(win_max) + interval_size * (sum(winning_int) - 1)
    print(f'total winners: {total_winners}')
    return


def winning_combos_test(test_vals, interval_size, total_distance, total_time):
    winning_combos = len(test_vals) * [0]
    losing_combos_det = ''
    winning_combos_det = ''
    print(f'commencing with {len(test_vals)} intervals of size: {interval_size}')
    for i, time_held in enumerate(test_vals):
        record = total_distance
        speed = time_held * 1
        time_remaining = total_time - time_held
        distance = time_remaining * speed
        combo = f'total_time: {total_time} time_held: {time_held} speed: {speed} distance: {distance} record: {record}\n'
        # print(f'time_held: {time_held} complete: {100 * time_held / total_time:.1f}%\ncombo: {combo}')
        if distance > record:
            winning_combos[i] += 1
            winning_combos_det += combo
        else:
            losing_combos_det += combo

    return winning_combos, winning_combos_det, losing_combos_det