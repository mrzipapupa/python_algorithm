"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random


def my_min(my_list):
    min_elem = my_list[0]
    for i in my_list:
        if i < min_elem:
            min_elem = i
    return min_elem


def my_max(my_list):
    max_elem = my_list[0]
    for i in my_list:
        if i > max_elem:
            max_elem = i
    return max_elem


if __name__ == '__main__':
    SIZE_LIST = 5
    matrix = [[random.randint(1, 20) for _ in range(SIZE_LIST)] for _ in range(SIZE_LIST)]
    print(*matrix, sep="\n")

    min_elements = []
    for column in range(SIZE_LIST):
        tmp_list = []
        for line in range(SIZE_LIST):
            tmp_list.append(matrix[line][column])
        min_elements.append(my_min(tmp_list))
    print("Минимальные элементы столбцов матрицы: ", min_elements)
    print("Максимальный из них: ", my_max(min_elements))
