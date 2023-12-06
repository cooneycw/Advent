from src_code.code06.assign_b import solver


def control():
    # Use a breakpoint in the code line below to debug your script.
    while True:
        cwc = input('Run development or prod:\n')
        if cwc == 'dev':
            main('dev')
        elif cwc == 'prod':
            main('prod')
        print('\n')
        break


def main(code):
    input_dict_dev_a = {
        'Time': [7, 15, 30],
        'Distance': [9, 40, 200],
    }
    input_dict_dev_b = {
        'Time': 71530,
        'Distance': 940200,
    }
    input_dict_prod_a = {
        'Time': [49, 78, 79, 80],
        'Distance': [298, 1185, 1066, 1181],
    }
    input_dict_prod_b = {
        'Time': 49787980,
        'Distance': 298118510661181,
    }

    if code == 'dev':
        input_dict = input_dict_dev_b
        # file_name = 'src_code/input/06/dev_a.txt'
    elif code == 'prod':
        input_dict = input_dict_prod_b
        #file_name = 'src_code/input/06/prod.txt'

    # with open(file_name, 'r') as file:
    #    text = file.read()
    text = dict()

    solver(input_dict, text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    control()

