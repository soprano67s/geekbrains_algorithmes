# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.
print('-'*20,
      '\nВведите две буквы и программа определит \n'
      'на каких местах алфавита они стоят и \n'
      'сколько между ними находится букв.\n',
      '-'*20)
first = ord(input('Введите первую букву: '))
second = ord(input('Введите вторую букву: '))

first_place = first - 96
second_place = second - 96
if first_place >= second_place:
    difference = first_place - second_place
else:
    difference = second_place - first_place
print(f"Номер первой буквы: \t{first_place}\nНомер второй буквы: \t{second_place}\nРазница между буквами: \t{difference}")