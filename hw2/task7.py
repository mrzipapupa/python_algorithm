"""
Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n – любое натуральное число.
"""

if __name__ == '__main__':
    sequence_len = int(input("Введите натуральное число, определеяющее длину ряда: "))
    left_sum, right_sum = 0, 0
    for element in range(sequence_len + 1):
        left_sum += element
    right_sum = sequence_len * (sequence_len + 1) / 2
    if left_sum == right_sum:
        print("Левая и правая части действительно равны!")
    else:
        print("Предположение оказалось неверным!")
