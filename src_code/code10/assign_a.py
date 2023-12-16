import copy


class Map():
    def __init__(self, x, y, label, piece):
        self.x = x
        self.y = y
        self.label = label
        self.piece = piece
        self.possible_neighbours = set()
        self.confirmed_neighbours = set()
        self.confirmed_start_paths = []
        self.loop = False
        self.start = False
        self.start_loop_complete = False

    def create_valid_neighbours(self, neighbours):
        neighbours_set = set()
        for neighbour in neighbours:
            if neighbour is not None:
                neighbours_set.add((neighbour.x, neighbour.y))
        test_set = set()
        if self.piece['piece_type'] != 'start':
            # print(self.x, self.y)
            for vector in self.piece['add_vectors']:
                x = self.x + vector[0]
                y = self.y + vector[1]
                test_set.add((x, y))
        common = test_set.intersection(neighbours_set)
        if len(common) > 0:
            for locale in common:
                self.possible_neighbours.add(locale)

    def create_confirmed_neighbours(self, neighbours):
        if len(self.possible_neighbours) == 0:
            return
        else:
            for neighbour in neighbours:
                if neighbour is not None:
                    #print(self.x, self.y, self.label, self.possible_neighbours, neighbour.x, neighbour.y, neighbour.label, neighbour.possible_neighbours)
                    if (neighbour.x, neighbour.y) in self.possible_neighbours and (self.x, self.y) in neighbour.possible_neighbours:
                        self.confirmed_neighbours.add((neighbour.x, neighbour.y))

        if len(self.confirmed_neighbours) > 0:
            self.loop = True

    def create_possible_start_paths(self, map_obj):
        neighbours = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x, y) != (0, 0) and (x, y) != (-1, -1) and (x, y) != (1, 1) and (x, y) != (1, -1) and (x, y) != (-1, 1):
                    neighbours.append(get_x_y_obj(self.x + x, self.y + y, map_obj))
        for neighbour in neighbours:
            if neighbour is not None:
                for possible in neighbour.possible_neighbours:
                    if (self.x, self.y) == possible:
                        self.confirmed_neighbours.add((neighbour.x, neighbour.y))
                        neighbour.confirmed_neighbours.add((self.x, self.y))

    def create_confirmed_start_paths(self, map_obj, start):
        next_obj = get_x_y_obj(start.x, start.y, map_obj)
        back_to_start = False
        while back_to_start is False:
            for neighbour in next_obj.confirmed_neighbours:
                if (neighbour[0], neighbour[1]) not in start.confirmed_start_paths:
                    start.confirmed_start_paths.append((neighbour[0], neighbour[1]))
                    break

            next_obj = get_x_y_obj(start.confirmed_start_paths[-1][0], start.confirmed_start_paths[-1][1], map_obj)
            if next_obj.start is True:
                back_to_start = True


def solver(inp_dict, data_file):

    map_obj = parser(data_file)

    for i in [0, 1]:
        for obj in map_obj:
            if obj.piece['piece_type'] != 'ignore':
                neighbours = []
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (x, y) != (0, 0) and (x, y) != (-1, -1) and (x, y) != (1, 1) and (x, y) != (1, -1) and (x, y) != (-1, 1):
                            # print(obj.x + x, obj.y + y)
                            neighbours.append(get_x_y_obj(obj.x + x, obj.y + y, map_obj))
                if i == 0:
                    obj.create_valid_neighbours(neighbours)
                elif i == 1:
                    obj.create_confirmed_neighbours(neighbours)

    start = get_s_obj(map_obj)
    start.create_possible_start_paths(map_obj)
    start.create_confirmed_start_paths(map_obj, start)
    print(f'furthest path: {int(len(start.confirmed_start_paths)/2)}')
    # print_map(map_obj)
    return


def print_map(map_obj):
    dims = get_minxy(map_obj)
    out_val = ''
    for y in range(0, dims[1] -1, -1):
        for x in range(0, dims[0] + 1):

            # print(x, y)
            obj = get_x_y_obj(x, y, map_obj)
            if obj is None:
                out_val += '.'
            elif obj.loop == False:
                print(x, y, obj.x, obj.y, obj.label, obj.possible_neighbours, obj.confirmed_neighbours)
                out_val += '.'
            else:
                print(x, y, obj.x, obj.y, obj.label, obj.possible_neighbours, obj.confirmed_neighbours)
                out_val += obj.label
        out_val += '\n'
    print(out_val)


def get_x_y_obj(x, y, map_obj):
    for obj in map_obj:
        if obj.x == x and obj.y == y:
            return obj


def get_s_obj(map_obj):
    for obj in map_obj:
        if obj.label == 'S':
            obj.start = True
            return obj


def get_minxy(map_obj):
    max_x = 0
    min_y = 0
    for obj in map_obj:
        max_x = max(max_x, obj.x)
        min_y = min(min_y, obj.y)
    return max_x, min_y


def parser(data_file):
    y = 0
    mapObj= []
    dir_dict = {
        'S': {'piece_type': 'start'},
        '.': {'piece_type': 'ignore'},
        'F': {'piece_type': 'corner',
              'add_vectors': [(1, 0), (0, -1)]},
        '|': {'piece_type': 'vertical',
              'add_vectors': [(0, -1), (0, 1)]},
        'L': {'piece_type': 'corner',
              'add_vectors': [(0, 1), (1, 0)]},
        '7': {'piece_type': 'corner',
              'add_vectors': [(-1, 0), (0, -1)]},
        'J': {'piece_type': 'corner',
              'add_vectors': [(-1, 0), (0, 1)]},
        '-': {'piece_type': 'horizontal',
              'add_vectors': [(-1, 0), (1, 0)]},
    }

    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        for x in range(0, len(line)):
            piece = line[x]
            obj = (Map(x, y, piece, dir_dict[piece]))
            if obj.piece['piece_type'] != 'ignore':
                mapObj.append(obj)
        y -= 1
        data_file = data_file[line_end+1:]

    return mapObj
