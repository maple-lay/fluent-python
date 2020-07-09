"""
functools 库
reduce 方法
partial 方法

"""
from functools import partial, reduce
from operator import mul
from unicodedata import normalize


if __name__ == '__main__':

    triple = partial(mul, 3)
    list_a = list(map(triple, range(1, 10)))
    # acd = reduce(mul, range(1, 10))   reduce 调用triple 会出错
    # acd = reduce(triple, range(1, 10))
    print(list_a)
    # print(acd)

    nfc_normalize = partial(normalize, "NFC")
    s_1 = "cafe\u0301"
    s_2 = "cafe\u0302"
    print(s_1)
    print(nfc_normalize(s_1))


