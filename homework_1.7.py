
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

print('-'*20,
      '\nВведите любой год и программа определит является ли он высокосным.\n',
      '-'*20)

year = int(input('Введите год: '))

if year % 100 == 0 and year % 400 != 0 or year % 4 != 0:
    print("Обычный")
else:
    print("Високосный")


