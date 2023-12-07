import os
import requests


def get_data(day, year, dev_or_prod):
    path = os.getcwd()
    session_id = os.getenv('SESSION')  # add SESSION () to PyCharm environment list in "edit configurations..."

    session = requests.Session()
    session.cookies.update({'session': session_id})

    example_id = ['<pre><code>', '</code></pre>']  # html tags to search for in web context for example...

    if dev_or_prod == 'dev':
        url = 'http://adventofcode.com/' + str(int(year)) + '/day/' + str(int(day))
        print(url)
    elif dev_or_prod == 'prod':
        url = 'https://adventofcode.com/' + str(int(year)) + '/day/' + str(int(day)) + '/input'
        print(url)

    success = False
    web_data = None
    try:
        web_data = session.get(url)
        web_data.raise_for_status()
        success = True
    except:
        raise ValueError('Web data not available.')

    if dev_or_prod == 'dev':
        save_data = web_data.text[web_data.text.find(example_id[0]) + len(example_id[0]):web_data.text.find(example_id[1])]
    elif dev_or_prod == 'prod':
        save_data = web_data.text
    folder_name = path + '/src_code/input/' + f'{int(day):02d}' + '/'
    if dev_or_prod == 'dev':
        file_name = 'dev.txt'
    elif dev_or_prod == 'prod':
        file_name = 'prod.txt'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    with open(folder_name + file_name, 'w') as file:
        file.write(save_data)


