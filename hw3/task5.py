"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random


if __name__ == '__main__':
    SIZE_LIST = 10
    values_list = [random.randint(-30, 30) for _ in range(SIZE_LIST)]
    print("Исходный список: ", values_list)

    value_index = -1
    i = 0
    while i < SIZE_LIST:
        if values_list[i] < 0 and value_index == -1:  # нахождение первого попавшегося отрицательного элемента
            value_index = i
        elif 0 > values_list[i] > values_list[value_index]:  # нахождение максимального отрицательного элемента
            value_index = i
        i += 1
    if value_index == -1:
        print("Не найдено отрицательных элементов!")
        exit(-1)

    print("Элемент: {0}. Его индекс в списке: {1}".format(values_list[value_index], value_index))

