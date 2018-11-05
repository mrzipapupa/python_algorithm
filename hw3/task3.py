"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

if __name__ == '__main__':
    values_list = [random.randint(1, 100) for _ in range(20)]
    print("Исходный массив: ", values_list)
    max_value = values_list[0]
    min_value = values_list[0]
    for element in values_list:
        if element > max_value:
            max_value = element
        elif element < min_value:
            min_value = element
    min_index = values_list.index(min_value)
    max_index = values_list.index(max_value)
    print("Минимальный элемент: {0}. Его индекс: {1}".format(min_value, min_index))
    print("Максимальный элемент: {0}. Его индекс: {1}".format(max_value, max_index))
    values_list[min_index], values_list[max_index] = values_list[max_index], values_list[min_index]
    print("Измененный массив: ", values_list)

