import importlib
DAY = '07'
RUN_GET_DATA = True  # True = create dev and prod files
ROUTINE_TYPE = 1  # 0 = dev; 1 = prod

YEAR = 2023
ROUTINE = ['dev', 'prod']

if ROUTINE[ROUTINE_TYPE] == 'dev':
    module_name = 'src_code.code' + DAY + '.assign_a'
elif ROUTINE[ROUTINE_TYPE] == 'prod':
    module_name = 'src_code.code' + DAY + '.assign_b'

src_code = importlib.import_module(module_name)
get_data = importlib.import_module('get_data')


def main():
    print(f'\nExecuting day {DAY} routine in {ROUTINE[ROUTINE_TYPE]}.. \n')

    input_dict = {}
    if ROUTINE[ROUTINE_TYPE] == 'dev':
        if RUN_GET_DATA:
            get_data.get_data(DAY, YEAR, ROUTINE[ROUTINE_TYPE])
        file_name = 'src_code/input/' + DAY + '/dev.txt'
    elif ROUTINE[ROUTINE_TYPE] == 'prod':
        if RUN_GET_DATA:
            get_data.get_data(DAY, YEAR, ROUTINE[ROUTINE_TYPE])
        file_name = 'src_code/input/' + DAY + '/prod.txt'

    with open(file_name, 'r') as file:
        text_data = file.read()

    src_code.solver(input_dict, text_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

