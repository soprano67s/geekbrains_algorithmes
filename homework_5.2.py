# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

from collections import defaultdict

number_list = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
number_dict = defaultdict(list, {value: keys for keys, value in enumerate(number_list)})
number_dict_rev = defaultdict(list, {f"{keys}": value for keys, value in enumerate(number_list)})

first_num = input('Введите первое число: ').upper()
second_num = input('Введите второе число: ').upper()

def summary_num(first_num, second_num):
    result_list = []
    first_num = first_num[::-1]
    second_num = second_num[::-1]
    if len(first_num) > len(second_num):
        second_num = second_num + '0' * (len(first_num) - len(second_num))
    else:
        first_num = first_num + '0' * (len(second_num) - len(first_num))
    x = 0
    for index, digit in enumerate(first_num):
        result = number_dict[digit] + number_dict[second_num[index]] + x
        if result > 16:
            x = result // 16
        else:
            x = 0
        current_result = result - 16 * x
        result = number_dict_rev[str(current_result)]
        result_list.append(result)

    return list(reversed(result_list))



def product_num(first_num, second_num):
    first_num = first_num[::-1]
    second_num = second_num[::-1]
    result_list = []
    for index, digit_2 in enumerate(second_num):
        result_middle_list = []
        x = 0
        for digit in first_num:
            result_middle = number_dict[digit] * number_dict[digit_2] + x
            if result_middle > 16:
                x = result_middle // 16
            else:
                x = 0
            current_result = result_middle - 16 * x
            result = number_dict_rev[str(current_result)]
            result_middle_list.append(result)
        if x != 0:
            result_middle_list.append(str(x))
        var_1 = list(reversed(result_middle_list))
        for j in range(index):
            var_1.append('0')
        result_list.append(var_1)
    for var_2 in range(0, len(result_list)-1, 1):
        number_first = ''.join(result_list[var_2])
        number_second = ''.join(result_list[var_2+1])
        calculation_result = summary_num(number_first, number_second)
        result_list[var_2+1] = calculation_result
    return result_list[len(result_list)-1]


print('Сумма чисел:', summary_num(first_num, second_num))
print('Произведение чисел:', product_num(first_num, second_num))