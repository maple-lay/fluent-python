"""
高阶函数
    接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher-order function）
"""


def reverse(word):
    return word[::-1]


if __name__ == '__main__':
    fruits = ['strawberry', 'fig', 'apple', 'raspberry', 'banana']
    print(sorted(fruits, key=len))

    print(sorted(fruits, key=reverse))