import datetime


def add_log(value: str):
    with open('calc_v2_output.txt', 'a', encoding='UTF-8') as data:
        now = datetime.datetime.now()
        data.write(f'{now.strftime("%Y-%m-%d %H.%M.%S")}: {value}\n')
