"""В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число.
Если за 10 попыток число не отгадано, то вывести его.
"""
import random

if __name__ == '__main__':
    random_number = random.randint(0, 100)
    for counter in range(10):
        result = int(input("Введите целое число, которое загадал компьютер: "))
        if result == random_number:
            print("Вы угадали! Поздравляю!")
            exit(0)
        elif result < random_number:
            print("Ваше число меньше")
        elif result > random_number:
            print("Ваше число больше")
    print("Увы! Вы не угадали. Правильный ответ был ", random_number)