"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего
задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
from datetime import datetime

"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры
"""

def time_it(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        res_time = datetime.now() - start
        print(f"Время выполнения: {res_time}")
        return result
    return wrapper

@time_it
def counting_sequence_sum(count):
    element = 1
    sequence_sum = element
    for counter in range(1, count):
        element /= -2
        sequence_sum += element
    return sequence_sum


@time_it
def geometry_sum(count):
    """На основе геометрической прогрессии с шагом -0.5"""
    """b₁(1-qⁿ)/(1-q), q ≠ 1"""
    return (1 - (-0.5)**count) / 1.5



if __name__ == '__main__':
    count_elements = int(input("Введите натуральное число членов для подсчета суммы: "))
    sequence_sum_1 = counting_sequence_sum(count_elements)
    sequence_sum_2 = geometry_sum(count_elements)
    if sequence_sum_1 == sequence_sum_2:
        print("Сумма ряда из {0} элементов равна {1}.".format(count_elements, sequence_sum_1))

"""Время выполненния первого алгоритма (через цикл) (средее по трем замерам)
Сложность: О(n) - однократное прохождение массива длины n с выполнением простой операции над каждым элементом
Линейный рост времени выполнения в зависимости от объема входных данных
5000000 - 0:00:01.074463
10000000 - 0:00:02.220514
15000000 - 0:00:03.254346667
20000000 - 0:00:04.358783667
25000000 - 0:00:05.454048667
"""

"""Время выполнения второго алгоритма (через сумму геометрической прогрессии)
Сложность: О(q^n) (из теории)
Для данного случая: O(-1/2^n)
Время слишком мало для того, чтобы адекватно его оценивать. Модуль datetime выдает всегда нули, за редким исключением,
которое списывается на погрешность
"""

