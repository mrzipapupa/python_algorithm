"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 – если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""


import random
import memory_counter as mc

if __name__ == '__main__':
    values_list = random.sample(range(1, 150), 20)
    indexes_list = [values_list.index(i) for i in values_list if i % 2 == 0]
    print(values_list)
    print(indexes_list)
    print(mc.memory_summ(locals()))

"""
20 элементов в values_list - суммарно 634 байт памяти.
python 3.7.1
Windows 10 x64
"""

