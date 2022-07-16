"""Счет в различных системах счисления, (c) Sayfullin Ruslan.
Отображает эквивалентные числа в десятичной, двоичной и шестнадцатеричной
системах счисления.
"""

print('''Numeral System Counters, by Sayfullin Ruslan
This program shows you equivalent numbers in decimal (base 10),
hexadecimal (base 16), and binary (base 2) numeral systems.
(Ctrl-C to quit.)
''')

while True:
    response = input('Enter the starting number (e.g. 0) > ')
    if response == '':
        response = '0' # По умолчанию начинаем с 0.
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)


while True:
    response = input('Enter how many numbers to display (e.g. 1000) > ')
    if response == '':
        response = '1000'   # По умолчанию выводим 1000 чисел.
        break
    if response.isdecimal():
        break
    print('Please enter a number.')
amount = int(response)

for number in range(start, start + amount):  # Основной цикл программы.
    # Преобразуем в шестнадцатеричное/двоичное и удаляем префикс:
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]
    print('DEC:', number, 'HEX:', hexNumber, 'BIN:', binNumber)
