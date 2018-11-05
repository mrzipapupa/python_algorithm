"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random


if __name__ == '__main__':
    SIZE_LIST = 20
    values_list = [random.randint(1, 100) for _ in range(SIZE_LIST)]
    print("Исходный список: ", values_list)

    sum_elements = 0
    max_value = values_list[0]
    min_value = values_list[0]
    for element in values_list:
        if element > max_value:
            max_value = element
        elif element < min_value:
            min_value = element
    min_index = values_list.index(min_value)
    max_index = values_list.index(max_value)
    if max_index < min_index:
        min_index, max_index = max_index, min_index
    print("Минимальный элемент: {0}. Его индекс: {1}".format(min_value, min_index))
    print("Максимальный элемент: {0}. Его индекс: {1}".format(max_value, max_index))
    if abs(max_index - min_index) == 1:
        print("Сумма = ", sum_elements)
    for i in range(min_index + 1, max_index):
        sum_elements += values_list[i]
    print("Сумма = ", sum_elements)