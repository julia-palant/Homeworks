"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

while True:
    number = input('Введите целое число')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('Введите целое число')
