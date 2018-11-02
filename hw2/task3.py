'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
'''


if __name__ == '__main__':
    reverse_number = ""
    number = int(input("Введите НАТУРАЛЬНОЕ число: "))
    while number > 0:
        digit = number % 10
        number //= 10
        reverse_number += str(digit)
    print("Перевернутое число '{0}'.".format(reverse_number))
