""""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
number = input("Введите число n")
# проверка на издиджит - доделать
print(type(number))
result = int(number)+int(number*3)+int(number*3)
print(result)
