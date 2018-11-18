"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и
разрядность вашей ОС.
"""

import sys


def get_size(x, memory_list, level=0):
    memory_list.append(sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                get_size(key, memory_list, level + 1)
                get_size(value, memory_list, level + 1)
        elif not isinstance(x, str):
            for item in x:
                get_size(item, memory_list, level + 1)


def memory_summ(user_objects):
    sum_mem = 0
    for obj in user_objects:
        mem_list = []
        if obj.startswith('__'):
            continue
        elif hasattr(user_objects[obj], '__call__'):
            continue
        elif hasattr(user_objects[obj], '__loader__'):
            continue
        else:
            get_size(user_objects[obj], mem_list)
            for item in mem_list:
                sum_mem += item
    return f'Общее количество затраченной памяти: {sum_mem} байт'