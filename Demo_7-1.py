"""
装饰器的原理
"""


def deco(func):
    def inner():
        print('running inner()')

    return inner

@deco
def target():
    print('running target')


def main():
    target()


if __name__ == '__main__':
    main()