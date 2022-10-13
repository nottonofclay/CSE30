from multiprocessing.resource_sharer import stop
import time
from tracemalloc import start
'''
def calculate_time(func):
    def wrap():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrap
'''

def calculate_time(func):
    # This function shows the execution time of
    # the function object passed
    def wrap(*args):
        start = time.time()
        result = func(*args)
        stop = time.time()
        print(f'It took {(stop-start)} sec.')
        return result
    return wrap

@calculate_time
def sum1(n):
   result = 0
   for i in range(1, n + 1):
      result += i
   return result


if __name__ == '__main__':
    n = 1000000
    s = sum1(100000)
    print(f'The sum of numbers from 1 to {n} is {s}.')