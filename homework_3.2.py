# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random

massive = []
index_massive = []

for i in range(10):
    massive.append(random.randint(0, 100))
    if massive[i] % 2 == 0:
        index_massive.append(i)
print(massive)
print(index_massive)