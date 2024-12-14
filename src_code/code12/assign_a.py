import copy
import math


def solver(inp_dict, data_file):
    regions = []
    map = parser(data_file)
    dims = (len(map), len(map[0]))


    veggies = sorted(list({value for row in map for value in row}))
    visited = [[False for i in range(dims[0])] for j in range(dims[1])]
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for i in range(dims[0]):
        for j in range(dims[1]):
            if not visited[i][j]:
                veggie = map[i][j]
                region = dict()
                region['name'] = veggie
                region['id'] = f'{str(i).zfill(2)}_{str(j).zfill(2)}'
                region['to_explore'] = list()
                region['contiguous'] = list()

                visited[i][j] = True
                region['to_explore'].append(tuple((i, j)))
                while region['to_explore']:
                    pos = region['to_explore'].pop(0)
                    region['contiguous'].append(pos)
                    for dir in dirs:
                        new_i = pos[0] + dir[0]
                        new_j = pos[1] + dir[1]
                        if 0 <= new_i < dims[0] and 0 <= new_j < dims[1]:
                            if visited[new_i][new_j] == False and map[new_i][new_j] == veggie:
                                visited[new_i][new_j] = True
                                region['to_explore'].append(tuple((new_i, new_j)))

                regions.append(region)

    cross_mult = 0
    for region in regions:
        print(f'processing: {region["name"]} {region["id"]}')
        area = len(region['contiguous'])
        perim = 0

        for space in region['contiguous']:
            compare_region = copy.deepcopy(region['contiguous'])
            compare_region.remove(space)
            for dir in dirs:
                new_i = space[0] + dir[0]
                new_j = space[1] + dir[1]
                if space[0] == -1:
                    cwc = 0
                if ((0 <= new_i < dims[0]) and (0 <= new_j < dims[1])) and (tuple((new_i, new_j)) in compare_region):
                    print(f'{space, new_i, new_j} no perimeter required')
                else:
                    print(f'{space, new_i, new_j} perimeter required')
                    perim = perim + 1
        print(f'area: {area} perim: {perim} ')
        cross_mult = cross_mult + (area * perim)

    print(cross_mult)


def parser(data_file):
    rows = []

    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        cols = []
        for i in range(len(line)):
            cols.append(line[i])
        rows.append(cols)
        data_file = data_file[line_end+1:]

    return rows
