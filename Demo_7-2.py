"""
python装饰器执行时间：
    在被装饰的函数定义之后立即执行
    通常是在导入模块的时候
"""

registry = []


def register(func):
    registry.append(func)
    print('running register {}.'.format(func))
    return func


@register
def fun_1():
    print('running func_1')


@register
def fun_2():
    print('running func_2')


def fun_3():
    print('running func_3')


if __name__ == '__main__':
    print('running main')
    print('registrt -> {}'.format(registry))
    fun_1()
    fun_2()
    fun_3()