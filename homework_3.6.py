# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random


massive = [random.randint(10, 20) for i in range(10)]
print(massive, '\n', '-'*30)
min_ = 0
max_ = 0
result = 0
for i in range(1, len(massive)):
    if massive[max_] < massive[i]:
            max_ = i
    elif massive[min_] > massive[i]:
            min_ = i
if min_ > max_:
    min_, max_ = max_, min_
for i in range(min_+1, max_):
    result += massive[i]
print(f' Минимальное число в массиве: {massive[min_]}\n',
      f'Максимальное число в массиве: {massive[max_]}\n',
      f'Сумма чисел между ними: {result}')