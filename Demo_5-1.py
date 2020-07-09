"""
    函数是对象

"""


def factorial(n):
    """
    阶乘计算
    :param n: 要计算的数字
    :return: n的阶乘
    """
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(3))
    print(factorial.__doc__)
    print(type(factorial))

    fact = factorial
    print(fact)
    print(fact(5))
    print(list(map(fact, range(7))))
    
