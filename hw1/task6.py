"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
"""Принцип аналогичен задаче №5. Те же операции перехода из ASCII в алфавит"""
if __name__ == '__main__':
    DIFF_SYSTEM = 96  # Переход от ASCII к английскому алфавиту
    num_letter = int(input("Введите номер буквы в английском алфавите: "))
    if num_letter < 1 or num_letter > 26:
        print("Вы ввели некорректную позицию!")
        exit(0)
    code_letter = DIFF_SYSTEM + num_letter
    print("Ваша буква: ", chr(code_letter))
