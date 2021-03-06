"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""
from datetime import datetime


def eratosphen_primes(limit):
    limitn = limit + 1
    not_prime = [False] * limitn

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i * 2, limitn, i):
            not_prime[f] = True
        yield i


def primes(n = 1):
    while True:
        if isprime(n):
            yield n
        n += 1


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def find_prime_number(index_number, func):
    counter = 1
    start_time = datetime.now()
    for n in func:
        if counter == index_number:
            print("Затраченное время: ", datetime.now() - start_time)
            return n
        counter += 1
    return -1

if __name__ == '__main__':
    print(find_prime_number(5000, primes()))
    print(find_prime_number(5000, eratosphen_primes(49000)))


"""
Время работы алгоритмов (среднее по трем замерам)
        "Грубой" силы       Решето      Быстрее (раз)
1000      0,617642с       0,008025c       77
2000      2,687465с       0,017547c       153
3000      6,260159c       0,027072c       231
4000      12,417258c      0,036598c       339
5000      21,989743с      0,049599с       443

Из приведенной таблицы видно, что в результате практического эксперимента были получены следующие данные.
Анализируя их, можно сделать вывод, что алгоритм решета для поиска простых чисел работает в разы быстрее алгоритма
'грубой' силы. Более того, можно заметить, что при увеличении объема данных, отношение времени работы метода грубой силы
к времени работы решета стремительно растет. Таким образом, можно сделать вывод, что на значительных объемах данных
алгоритм решета работает гораздо быстрее.
P.S. так и не пришла идея в голову, как избавиться от излишних элементов решета (переменная limit в eratosphen_primes).
То есть алгоритм предполагает проход списка некоторой длины с последующим вычеркиванием элементов. В данном случае,
было бы здорово строить его на ходу, но это во первых сильно замедлит реализацию (могу постараться обосновать
теоретически), во вторых сильно усложнит реализацию. Поэтому было решено использование чуть большего решета (подбором),
чем порядковый номер простого числа. В среднем, для вычисления размера списка приходилось умножать порядковый номер на
6-9. Возможно, это сильно неправильно, однако, время работы его всё равно слишком сильно превосходит работу
стандартного алгоритма. Кроме того, целью является выявление зависимости времени от объема данных и расчет теоретической
сложности алгоритма. Реализованный момент там я учёл.

Что касается теоретической сложности:
Алгоритм "решета":
O(n * log(log n)) - информация из открытых источников. Обоснование лежит на википедии, не представляет собой
ничего сложного, но смысла копировать сюда не вижу. (Строго математическое). Практические результаты подтверждают
теорию (при построение графика получается логарифмическая кривая)
Существует реализация снижающая сложность до O(sqrt(n)) через корни (не учитывая половины перебора)
Алгоритм "грубой силы":
O(n) - перебор всех элементов по порядку до поиска нужного и проверка каждого
O(n) - для каждого элемента перебираем все делители от 2 до n
Суммарная теоретическая сложность: O(n^2)
Она слегка отличается от практических результатов, возмонжо из-за особенности языка или реализации.
"""