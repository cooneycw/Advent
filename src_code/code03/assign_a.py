def solver(inp_dict, data_file):
    print(f'type of data: {type(data_file)}  length of data: {len(data_file)}')
    value_objs = parser_nums(data_file)
    symbol_objs = parser_symbs(data_file)

    for obj in value_objs:
        for symb_obj in symbol_objs:
            obj.adj_test(symb_obj.row, symb_obj.col)

    valid_vals = [obj.value for obj in value_objs if obj.adj == 1]

    print(f'the sum is: {sum(valid_vals)}')
    return


class Value:
    def __init__(self, row, start_pos, end_pos, value):
        self.row = row
        self.col_start = start_pos
        self.col_end = end_pos
        self.value = value
        self.adj = 0

    def adj_test(self, row, col):
        i = self.col_start
        while i < self.col_start + self.col_end:
            if (abs(row - self.row) + abs(col - i)) == 1 or (abs(row - self.row) == 1 and abs(col - i) == 1):
                self.adj = 1
                break

            i += 1


class Symb:
    def __init__(self, row, start_pos, symb):
        self.row = row
        self.col = start_pos
        self.symb = symb


def parser_nums(data_file):
    valid_list = [ord(x) for x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']]
    val_objs = []
    sym_objs = []
    row = 0
    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        ords = [ord(x) for x in list(line)]
        i = 0
        while i < len(ords):
            ord_val = ords[i]
            if 48 <= ord_val <= 57:
                j = 1
                while j < len(ords[i:]):
                    jord_val = ords[i+j]
                    if jord_val < 48 or jord_val > 57:
                        val_objs.append(Value(row, i, j, int(line[i:i+j])))
                        i = i + j
                        break
                    else:
                        j = j + 1
                        if (i+j) == len(line):
                            val_objs.append(Value(row, i, j, int(line[i:i + j])))
                            i = i + j
                            break
            else:
                i += 1
        data_file = data_file[line_end+1:]
        row += 1

    return val_objs


def parser_symbs(data_file):
    valid_list = [ord(x) for x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']]
    sym_objs = []
    row = 0
    while True:
        line_end = data_file.find('\n')
        if line_end == -1:
            break
        line = data_file[0:line_end]
        ords = [ord(x) for x in list(line)]
        i = 0
        while i < len(ords):
            ord_val = ords[i]
            if ord_val not in valid_list:
                sym_objs.append(Symb(row, i, line[i:i+1]))
            i += 1
        data_file = data_file[line_end+1:]
        row += 1

    return sym_objs

