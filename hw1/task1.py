"""1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

if __name__ == '__main__':
    user_number = input("Введите положительное трехзначное число: ")
    a, b, c = [int(number.split()[0]) for number in user_number]
    print("Сумма цифр = {0}. Их произведение = {1}".format(a+b+c, a*b*c))