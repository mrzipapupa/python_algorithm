"""
Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""


def get_substrings(string):
    len_str = len(string)
    alph_count = 31

    alph_pow = [None] * len_str
    alph_pow[0] = 1
    for num_pow in range(1, len(alph_pow)):
        alph_pow[num_pow] = alph_pow[num_pow-1] * alph_count

    hashes = [None] * len_str
    for symbol_index in range(0, len_str):
        hashes[symbol_index] = (ord(string[symbol_index]) - ord('a') + 1) * alph_pow[symbol_index]
        if symbol_index:
            hashes[symbol_index] += hashes[symbol_index - 1]

    result = 0

    for symbol_index in range(1, len_str + 1): # либо до len_str, если не считать строку собственной подстрокой
        sub_hashes = [None] * (len_str - symbol_index + 1)
        # перебор всех подстрок с получением их хеша
        for sub_index in range(0, len_str - symbol_index + 1):
            cur_hash = hashes[sub_index + symbol_index - 1]
            if symbol_index:
                cur_hash -= hashes[sub_index - 1]
            # приведение всех хешей к одной степени
            cur_hash *= alph_pow[len_str - sub_index - 1]
            sub_hashes[sub_index] = cur_hash

        # получение уникальных хешей
        sub_hashes = set(sub_hashes)
        result += len(sub_hashes)

    return result



def get_substrings_2(string):
    str_len = len(string)
    result = set()
    for i in range(str_len):
        for j in range(i, str_len):
            result.add(hash(string[i:j + 1]))
    return len(result)


if __name__ == '__main__':
    print(get_substrings('token'))
    print(get_substrings_2('token'))

    """Первый алгоритм - не мой, взят с интернета, конкретно способ поиска всех подстрок через хеширование.
    Он был в псевдокоде, я его переделал и чуть-чуть дописал получше. Однако, победить НЕуникальность символов мне
    так и не удалось... Не нашел ошибку там, но не хочет он учитывать совпадающие значения.
    Второй алгоритм - пародия метода 'грубой силы', по факту - ничем от него не отличается. Для чего делать так -
    не знаю, но при этом не понимаю и задание в этом плане.
    Была еще идея с хеш-функцией с модулями больших простых чисел, где хеш-значение являлось бы индексом
    списка/массива, а коллизии разрешать методом связных цепочек, но в этом я тоже смысла особого не вижу, поэтому
    реализовывать не стал. Дабы компенсировать эту дыру решил сделать и второе заданиие."""