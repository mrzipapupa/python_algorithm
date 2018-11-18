"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше ее.
"""

import random


def get_middle(array):
    counter = 0
    for item in array:
        less_counter, more_counter = 0, 0
        for i in range(0, len(array)):
            if counter == i:
                continue
            if item > array[i]:
                more_counter += 1
            elif item < array[i]:
                less_counter += 1
        counter += 1
        if more_counter == less_counter:
            return item


if __name__ == '__main__':
    array = random.sample(range(0, 100), 5)
    print(f'Исходный массив: {array}')
    print(f'Медиана: {get_middle(array)}')

"""
Способ получился не быстрый - n^2.
Идея в следующем: для каждого элемента считаем количество элементов массива, которые больше него, и меньше него.
Если это количество совпадает - элемент медиана, иначе переходим к следующему элементу.
"""