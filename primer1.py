#!/usr/bin/env  python3

if __name__ == '__main__':
    def decorator_function(func):


        def wrapper():
            print('Функция-обёртка!')
            print('Оборачиваемая функция: {}'.format(func))
            print('Выполняем обёрнутую функцию...')
            func()
            print('Выходим из обёртки')
        return wrapper

    
    @decorator_function
    def hello_world():
        print('Hello world!')

    hello_world()
