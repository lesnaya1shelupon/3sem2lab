#!/usr/bin/env  python3

if __name__ == '__main__':
    def benchmark(func):
        import time


        def wrapper():
            start = time.time()
            func()
            end = time.time()
            print('[*] Время выполнения: {} секунд.'.format(end-start))
        return wrapper

    
    @benchmark
    def fetch_webpage():
        import requests
        webpage = requests.get('https://google.com')

    fetch_webpage()
