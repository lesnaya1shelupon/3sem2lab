#!/usr/bin/env  python3

from json.tool import main

if __name__ == '__main__':
    def decorator(func, start = 5):


        def inner(*args, **kwargs):
            f = func(*args, **kwargs)
            print('Cумма введенных чисел: {}.'.format(start + f))
        return inner


    @decorator
    def out(s):
        str_numb = list(map(int, s.split()))
        summa = sum(str_numb)
        return summa

    str_text = \
        input('Введите числа через пробел: ')
    out(str_text)
