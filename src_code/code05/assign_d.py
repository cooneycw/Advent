import multiprocessing


def parallel_process(args):
    data_file, seed_a, i = args
    seeds = process_seeds([seed_a[2*i], seed_a[2*i + 1]])
    sts_s, sts_d = process(parser('sts', data_file))
    stf_s, stf_d = process(parser('stf', data_file))
    ftw_s, ftw_d = process(parser('ftw', data_file))
    wtl_s, wtl_d = process(parser('wtl', data_file))
    ltt_s, ltt_d = process(parser('ltt', data_file))
    tth_s, tth_d = process(parser('tth', data_file))
    htl_s, htl_d = process(parser('htl', data_file))

    location = 10000000000
    llocation = location
    for q, seed in enumerate(seeds):
        soil = func_map(seed, sts_s, sts_d)
        fert = func_map(soil, stf_s, stf_d)
        watr = func_map(fert, ftw_s, ftw_d)
        lght = func_map(watr, wtl_s, wtl_d)
        temp = func_map(lght, ltt_s, ltt_d)
        humd = func_map(temp, tth_s, tth_d)
        locn = func_map(humd, htl_s, htl_d)
        location = min(locn, location)
        if location != llocation or q % 10000000 == 0:
            print(f'batch i:{i} seed: {seed} completion: {100 * q / len(seeds):.1f}% new location: {location}')
            llocation = location

    print(f'batch {i} completed. seeds evaluated: {len(seeds)} min location: {location}')
    return location


def solver(inp_dict, data_file):
    print(f'type of data: {type(data_file)}  length of data: {len(data_file)}')
    seed_a = parser('seeds', data_file)
    iters = int(len(seed_a)/2)

    pool = multiprocessing.Pool(3)
    tasks = [(data_file, seed_a, i) for i in range(iters)]
    results = pool.map(parallel_process, tasks)
    pool.close()
    pool.join()

    location = min(results)
    print(f'min location is: {location}')


def func_map(seed, _s, _d):
    map_val = None

    for i, source in enumerate(_s):
        if source[0] <= seed < source[1]:
            map_val = _d[i][0] + seed-source[0]

    if map_val is None:
        map_val = seed

    return map_val


def parser(seek_val, data_file):
    row = 0
    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        categ_end = line.find(':')
        test_val = line[0:categ_end]
        if test_val.find('seeds') != -1 and seek_val == 'seeds':
            seed_list = line[2 + categ_end:line_end].split(' ')
            seeds = [int(seed) for seed in seed_list]
            return seeds
        elif line.find('seed-to-soil map') != -1 and seek_val == 'sts':
            sts = []
            data_file = data_file[line_end + 1:]
            while True:
                end_test = data_file.find('\n')
                if end_test != 0:
                    line = data_file[0:end_test]
                    sts_list = line.split(' ')
                    sts.extend([int(st) for st in sts_list])
                    data_file = data_file[end_test + 1:]
                else:
                    break
            return sts
        elif line.find('soil-to-fertilizer map') != -1 and seek_val == 'stf':
            stf = []
            data_file = data_file[line_end + 1:]
            while True:
                end_test = data_file.find('\n')
                if end_test != 0:
                    line = data_file[0:end_test]
                    stf_list = line.split(' ')
                    stf.extend([int(st) for st in stf_list])
                    data_file = data_file[end_test + 1:]
                else:
                    break
            return stf
        elif line.find('fertilizer-to-water map') != -1 and seek_val == 'ftw':
            ftw = []
            data_file = data_file[line_end + 1:]
            while True:
                end_test = data_file.find('\n')
                if end_test != 0:
                    line = data_file[0:end_test]
                    ftw_list = line.split(' ')
                    ftw.extend([int(st) for st in ftw_list])
                    data_file = data_file[end_test + 1:]
                else:
                    break
            return ftw
        elif line.find('water-to-light map') != -1 and seek_val == 'wtl':
            ftw = []
            data_file = data_file[line_end + 1:]
            while True:
                end_test = data_file.find('\n')
                if end_test != 0:
                    line = data_file[0:end_test]
                    ftw_list = line.split(' ')
                    ftw.extend([int(st) for st in ftw_list])
                    data_file = data_file[end_test + 1:]
                else:
                    break
            return ftw
        elif line.find('light-to-temperature map') != -1 and seek_val == 'ltt':
            ftw = []
            data_file = data_file[line_end + 1:]
            while True:
                end_test = data_file.find('\n')
                if end_test != 0:
                    line = data_file[0:end_test]
                    ftw_list = line.split(' ')
                    ftw.extend([int(st) for st in ftw_list])
                    data_file = data_file[end_test + 1:]
                else:
                    break
            return ftw
        elif line.find('temperature-to-humidity map') != -1 and seek_val == 'tth':
            ftw = []
            data_file = data_file[line_end + 1:]
            while True:
                end_test = data_file.find('\n')
                if end_test != 0:
                    line = data_file[0:end_test]
                    ftw_list = line.split(' ')
                    ftw.extend([int(st) for st in ftw_list])
                    data_file = data_file[end_test + 1:]
                else:
                    break
            return ftw
        elif line.find('humidity-to-location map') != -1 and seek_val == 'htl':
            htl = []
            data_file = data_file[line_end + 1:]
            while True:
                end_test = data_file.find('\n')
                if end_test != 0:
                    line = data_file[0:end_test]
                    htl_list = line.split(' ')
                    htl.extend([int(st) for st in htl_list])
                    data_file = data_file[end_test + 1:]
                else:
                    break
            return htl

        data_file = data_file[line_end+1:]
        row += 1

    return


def process(val_list):
    source = []
    dest = []
    for i in [x for x in range(0, len(val_list), 3)]:
        source.append((val_list[i + 1], val_list[i+1] + val_list[i + 2]))
        dest.append((val_list[i + 0], val_list[i+0] + val_list[i + 2]))

    return source, dest


def process_seeds(seed_data):
    seeds = []
    for i in [x for x in range(0, len(seed_data), 2)]:
        seeds.extend([seed_data[i] + j for j in range(0, seed_data[i+1], 1)])
    return seeds