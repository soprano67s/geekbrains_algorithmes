
import random
import sys
from collections import namedtuple


def all_size(x):
    z = 0
    for i in range(len(x)):
        z += sys.getsizeof(x[i])
    return f'Размер всех переменных: {z} байт'


# **********************************       ЗАДАЧА 1       **************************************
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

print('Введите количество чисел и цифру которую хотите найти в этих числах. \n'
      'Программа посчитает сколько раз встречается определенная цифра в введенной последовательности чисел.\n', '-'*20)

count = int(input('Введите количество чисел: '))
digit = int(input('Введите цифру:'))

full_num = ''
result = 0
i = 0
num_digit = 1

while i != count:
    num = int(input(f'Введите {num_digit} число: '))
    full_num += str(num)
    i += 1
    num_digit += 1

i = len(str(full_num))

while i != 0:
    x = int(full_num) % 10
    full_num = int(full_num) // 10
    if x == digit:
        result += 1
    i -= 1

print(f'Цифра {digit} встретилась {result} раз.')




print('='*20)
task_1 = []*8
task_1.append(count)
task_1.append(digit)
task_1.append(full_num)
task_1.append(result)
task_1.append(i)
task_1.append(num_digit)
task_1.append(num)
task_1.append(x)
print(all_size(task_1))
print('='*20, '\n')

# ==============   --------- Задача 1 -------------   ===============
# ==============   OS Win10 x64                       ===============
# ==============   Python 3.7.1(32bit)                ===============
# ==============   Размер всех переменных: 108 байт   ===============
# ==============   count: 14 байт                     ===============
# ==============   digit: 14 байт                     ===============
# ==============   full_num: 12 байт                  ===============
# ==============   result: 14 байт                    ===============
# ==============   i: 12 байт                         ===============
# ==============   num_digit: 14 байт                 ===============
# ==============   num: 18 байт                       ===============
# ==============   x: 14 байт                         ===============
# ==============   --------------------------------   ===============



# **********************************       ЗАДАЧА 2       **************************************
# Определить, какое число в массиве встречается чаще всего



massive = [random.randint(10, 20) for i in range(20)]
print(massive)
first_count = 1

for i in range(len(massive)):
    second_count = 1
    for x in range(i + 1, len(massive)):
        if massive[i] == massive[x]:
            second_count += 1
    if second_count > first_count:
        first_count = second_count
        result = massive[i]


if first_count > 1:
    print(f'Число встречающееся чаще всех: {result} \n'
          f'Сколько раз: {first_count}')
else:
    print('Нет повторяющихся чисел.')

print('='*20)
task_2 = []
task_2.append(massive)
task_2.append(first_count)
task_2.append(second_count)
task_2.append(result)
print(all_size(task_2))
print('='*20, '\n')

# ==============   --------- Задача 2 -------------   ===============
# ==============   OS Win10 x64                       ===============
# ==============   Python 3.7.1(32bit)                ===============
# ==============   Размер всех переменных: 178 байт   ===============
# ==============   massive: 136 байт                  ===============
# ==============   first_count: 14 байт               ===============
# ==============   second_count: 14 байт              ===============
# ==============   result: 14 байт                    ===============
# ==============   --------------------------------   ===============


# **********************************       ЗАДАЧА 3       **************************************
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.



company = namedtuple('company', ['name', 'sum_profit'])
quantity = int(input('Введите количество предприятий: '))
profile = set()
all_profit = 0
more = ''
less = ''
equally = ''

for i in range(quantity):
    name = input(f'Введите название {i+1} предприятия: ')
    sum_profit = 0
    profit = []
    for x in range(4):
        profit.append(int(input(f'Введите прибыль предприятия "{name}" за {x+1} квартал: ')))
        sum_profit += profit[x]
    base_company = company(name=name, sum_profit=sum_profit)
    sum_ = 0
    profile.add(base_company)
    all_profit += sum_profit
    print('='*20)
mean = all_profit / quantity
print(f'Средняя прибыль: {mean}')

for z in profile:
    if z.sum_profit > mean:
        more += z.name + f'(Прибыль: {z.sum_profit}), '
    elif z.sum_profit < mean:
        less += z.name + f'(Прибыль: {z.sum_profit}), '
    else:
        equally += z.name + f'(Прибыль: {z.sum_profit}), '

if more:
    print(f'Компании получившие прибыль больше средней: {more[0:-2]}')
if less:
    print(f'Компании получившие прибыль меньше средней: {less[0:-2]}')
if equally:
    print(f'Компании получившие прибыль равную средней: {equally[0:-2]}')



print('='*20)
task_3 = []
task_3.append(company)
task_3.append(quantity)
task_3.append(profile)
task_3.append(all_profit)
task_3.append(more)
task_3.append(less)
task_3.append(equally)
task_3.append(name)
task_3.append(sum_profit)
task_3.append(profit)
task_3.append(base_company)
task_3.append(sum_)
task_3.append(mean)
task_3.append(z)
task_3.append(x)
print(all_size(task_3))
print('='*20, '\n')


# ==============   --------- Задача 3 -------------   ===============
# ==============   OS Win10 x64                       ===============
# ==============   Python 3.7.1(32bit)                ===============
# ==============   Размер всех переменных: 1015 байт  ===============
# ==============   company: 448 байт                  ===============
# ==============   quantity: 14 байт                  ===============
# ==============   profile: 116 байт                  ===============
# ==============   all_profit: 14 байт                ===============
# ==============   more: 72 байта                     =============== (зависит от количества компаний с прибылью больше средней)
# ==============   less: 72 байта                     =============== (зависит от количества компаний с прибылью меньше средней)
# ==============   equally: 72 байта                  =============== (зависит от количества компаний с прибылью равной средней)
# ==============   name: 27 байт                      ===============
# ==============   sum_profit: 14 байт                ===============
# ==============   profit: 52 байта                   ===============
# ==============   base_company: 36 байт              ===============
# ==============   sum_: 12 байт                      ===============
# ==============   mean: 16 байт                      ===============
# ==============   z: 36 байт                         ===============
# ==============   x: 14 байт                         ===============
# ==============   --------------------------------   ===============
