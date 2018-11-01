"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

if __name__ == '__main__':
    line_breaker = 0
    for counter in range(32, 128):
        print('"{0} - {1}"'.format(counter, chr(counter)), end=' ')
        line_breaker += 1
        if line_breaker % 10 == 0:
            print()