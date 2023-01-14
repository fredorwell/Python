# Доработать уже готового телеграм-бота или создать новое приложение (любое) с использованием сторонних библиотек

from currency_converter import CurrencyConverter


def avail_curr():
    print('Список доступных валют: \n'
          'USD - Доллары США\n'
          'EUR - Евро\n'
          'RUB - Рубли\n'
          'TRL - Турецкая лира\n'
          'CNY - Китайский юань\n'
          'ILS - Шеккель\n'
          'CAD - Каннадский доллар\n')


c = CurrencyConverter()
cur_list = c.currencies
print('Добро пожаловать в конвертер валют, для вызова списка валют введите help.')

while True:
    input_data = input('Введите сумму валюты которые есть у вас, например "100 usd": ')
    input_data = input_data.split()
    if len(input_data) == 2:
        if input_data[0].isdigit() and input_data[1].upper() in cur_list:
            value = int(input_data[0])
            сur_in = input_data[1].upper()
            break
        else:
            print('Вы ввели сумму не корректно попробуйте еще раз!')
    elif input_data == ['help']:
        avail_curr()

while True:
    cur_out = input("Для вызова списка валют введите help.\nКакую валюту вы хотите получить: ").upper()
    if cur_out == 'help':
        avail_curr()
    elif cur_out in cur_list:
        result = float(c.convert(value, сur_in, cur_out))
        print(f'Вы получите {round(result)} {cur_out} за {value} {сur_in}')
        break
    else:
        print('Вы ввели не корректную валюту, попробуйте еще раз')
