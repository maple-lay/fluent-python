"""
可调用对象
    调用运算符“（）”
    判断对象是否可以调用，callable()
    用户定义的可调用类型
        类实现实例方法__call__
"""
import random
class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == "__main__":

    bingo = BingoCage(range(10))
    for i in range(5):
        print(bingo())
