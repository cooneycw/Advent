from src_code.code02.assign_b import solver


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
    limits = dict()
    limits['blue'] = 14
    limits['green'] = 13
    limits['red'] = 12
    if code == 'dev':
        file_name = 'src_code/input/02/dev_a.txt'
    elif code == 'prod':
        file_name = 'src_code/input/02/prod.txt'

    with open(file_name, 'r') as file:
        text = file.read()

    solver(limits, text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    control()

