"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9
"""


if __name__ == '__main__':
    for digit in range(2, 10):
        counter = 0
        print(str(digit) + ': ', end=" ")
        for number in range(2, 100):
            if number % digit == 0:
                counter += 1
                print(number, end=" ")
        print("| всего - {0} \n".format(counter))
