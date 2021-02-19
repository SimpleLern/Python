# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Срезы

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.

# Справвка
# Оператор получения среза имеет три формы записи: 
# seq[start]
# seq[start:end]
# seq[start:end:step]
# Шаг может быть отрицательным, в этом случае элементы последовательности
# вернутся в обратном порядке.


# A. Четные
# Дана строка, состоящая из символов и/или последовательностей символов, 
# разделенных пробелами.
# Нужно вернуть строку, содержащую только четные элементы из исходной строки.
# Например, из 'a b c d e f' получится 'b d f'
# Решите задачу в одну строчку используя срезы.
def even(s):
    
    return ' '.join(s.split()[1::2])


# B. Наоборот
# Дана строка, состоящая из символов и/или последовательностей символов,
# разделенных пробелами.
# Нужно вернуть строку, содержащую элементы исходной строки в обратном порядке.
# Например, из 'a b c d e' получится 'e d c b a'
# Решите задачу в одну строчку используя срезы.
def reverse(s):

    return ' '.join(s.split()[::-1])


# C. Сдвиг
# Дана строка, состоящая из символов и/или последовательностей символов, 
# разделенных пробелами.
# Нужно вернуть строку, в которой последний элемент находится на первом месте.
# Например, из 'a b c d e f' получится 'f a b c d e'
# Решите задачу в две строки используя срезы.
def shift(s):
    return ' '.join(s.split()[-1:] + s.split()[:-1])


# D. Палиндром
# Дано число.
# Нужно определить является ли оно палиндромом.
# Число является палиндромом если оно одинаково читающееся в обоих направлениях.
# Решите задачу в одну строку используя срезы.
def palindrome(d):    
    
    return str(d) == str(d)[::-1]


# E. Внутри
# Дана строка, состоящая из четного количества символов и/или последовательностей символов,
# разделенных пробелами.
# Верните строку, в которой первый и последний элементы поставлены в середину 
# исходной строки. Например, из 'a b c d e f' получится 'b c a f d e'.
# Решите задачу в три строки используя срезы.
def inside(s):
    s_list = s.split()
    m = len(s_list) / 2
    return ' '.join(s_list[1:m] + [s_list[0]] + [s_list[-1]] + s_list[m:-1])



# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('Четные')
    test(even('a b c d e f'), 'b d f')
    test(even('w ee rt fff xyz'), 'ee fff')

    print()
    print('Наоборот')
    test(reverse('a b c d e f'), 'f e d c b a')
    test(reverse('w ee rt fff xyz'), 'xyz fff rt ee w')

    print()
    print('Сдвиг')
    test(shift('a b c d e f'), 'f a b c d e')
    test(shift('w ee rt fff xyz'), 'xyz w ee rt fff')

    print()
    print('Палиндром')
    test(palindrome(12321), True)
    test(palindrome(12345), False)

    print()
    print('Внутри')
    test(inside('a b c d e f'), 'b c a f d e')
    test(inside('w ee rt fff'), 'ee w fff rt')


if __name__ == '__main__':
    main()
