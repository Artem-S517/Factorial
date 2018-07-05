import atexit
import os
# import math #Быстрое решение

while True:
    try:
        factor_value = (int(input('Введите целое число для вычисления факториала: ')))
        if factor_value > 0:
            break
        else:
            print('Введите положительное число')
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")
# fac= math.factorial(factor_value) #Быстрое решение
# print("факториал равен", fac) #Быстрое решение
fac = 1
i = 0
while i < factor_value:
    i += 1
    fac = fac * i
print("факториал равен", fac)


def press_any_key():
    if os.name == "nt":
        os.system("pause")


atexit.register(press_any_key)
