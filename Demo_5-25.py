"""
operator 库
methodcaller方法
methodcaller创建的函数会在对象上调用参数指定的方法
"""

from operator import methodcaller


if __name__ == '__main__':
    # print(help(methodcaller))
    str_s = "this is a test"
    func_upper_case = methodcaller("upper")
    print(func_upper_case(str_s))
    hiphenate = methodcaller("replace", " ", "-")
    print(hiphenate(str_s))