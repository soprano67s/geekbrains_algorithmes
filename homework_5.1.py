# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

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


