"""
map、 filter和reduce的现代替代品
"""
from functools import reduce
from operator import add

def factorial(n):
    """
    阶乘计算
    :param n: 要计算的数字
    :return: n的阶乘
    """
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    fact = factorial
    print(list(map(fact, range(6))))
    print([fact(n) for n in range(6)])

    print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
    print([factorial(n) for n in range(6) if n % 2])

    # reduce多用于加法计算

    print(reduce(add, range(100)))
    print(sum(range(100)))