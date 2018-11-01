"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

if __name__ == '__main__':
    count_elements = int(input("Введите натуральное число членов для подсчета суммы: "))
    element = 1
    sequence_sum = element
    for counter in range(1, count_elements):
        element /= -2
        sequence_sum += element
    print("Сумма ряда из {0} элементов равна {1}.".format(count_elements, sequence_sum))
