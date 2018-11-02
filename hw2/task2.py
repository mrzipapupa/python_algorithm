"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def digits_from_number(number):
    while number > 0:
        b = number % 10
        number //= 10
        yield b


if __name__ == '__main__':
    even_counter = 0
    not_even_counter = 0
    number = int(input("Введите НАТУРАЛЬНОЕ число: "))
    for digit in digits_from_number(number):
        if int(digit) % 2 == 0:
            even_counter += 1
        else:
            not_even_counter += 1
    print("В вашем числе {0} содержится {1} четных цифр(ы) и "
          "{2} нечетных".format(number, even_counter, not_even_counter))
