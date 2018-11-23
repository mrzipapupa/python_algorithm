"""Закодируйте любую строку из трех слов по алгоритму Хаффмана."""
"""
Код может отличаться от предложенного в уроке, т.к. при одинаковой частотной характеристике нескольких символов код
Хаффмана может варьировать свои значения. Касательно программирования - будет зависеть от порядка составления кода.
Однако мощность кода должна сохраняться. Для строки, предложенной в уроке - мощность 40 бит. Здесь - аналогично.
"""

from collections import Counter

def help_function(f):
    return lambda args: f(*args)


def leaf_pair(p):
    assert(len(p) >= 2)
    sorted_p = sorted(p.items(), key=help_function(lambda i, pi:pi))
    return sorted_p[0][0], sorted_p[1][0]


def huffman_code(dict_stat):
    if len(dict_stat) == 2:
        return dict(zip(dict_stat.keys(), ['0', '1']))
    dict_stat_prime = dict_stat.copy()
    a1, a2 = leaf_pair(dict_stat)
    p1, p2 = dict_stat_prime.pop(a1), dict_stat_prime.pop(a2)
    dict_stat_prime[a1 + a2] = p1 + p2
    code = huffman_code(dict_stat_prime)
    lead_code = code.pop(a1 + a2)
    code[a1], code[a2] = lead_code + '0', lead_code + '1'
    return code


def get_statistics(string):
    dict_counter = dict(Counter(string))
    count_letters = sum(dict_counter.values())
    stat_res = {i: j/count_letters for i, j in zip(dict_counter.keys(), dict_counter.values())}
    return stat_res


def huffman_string(code, string):
    res = ''
    for symbol in string:
        if symbol in code.keys():
            res += code.get(symbol)
    return res


if __name__ == '__main__':
    message = 'beep boop beer!'
    statistics_dict = get_statistics(message)
    code = huffman_code(statistics_dict)
    res_huffman = huffman_string(code, message)
    res_ascii = ''.join(format(ord(x), 'b') for x in message)


    print('Разница между стандартным представлением и кодом Хаффмана:')
    print(f'Исходная строка: {message}')
    print(f'Без кода Хаффмана: {res_ascii}. Количество бит: {len(res_ascii)}')
    print(f'C кодом Хаффмана: {res_huffman}. Количество бит: {len(res_huffman)}')