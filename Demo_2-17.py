"""
    list.sort 和 sorted
        list.sort方法会就地排序列表，也就是说不会把原列表复制一份，返回值是None
        如果一个函数或者方法对对象进行的是就地改动，那它就应该返回None
        sorted会新建一个列表作为返回值。这个方法可以接受任何形式的可迭代对象作为参数，甚至包括不可变序列或生成器
        reverse：如果被设定为True，被排序的序列里的元素会以降序输出
        key：个函数会被用在序列里的每一个元素上，所产生的结果将是排序算法依赖的对比关键字
            这个参数的默认值是恒等函数（identity function），也就是默认用元素自己的值来排序
"""

"""
    用bisect来管理已排序的序列
        bisect模块包含两个主要函数，bisect和insort，两个函数都利用二分查找算法来在有序序列中查找或插入元素。
        bisect(haystack, needle)在haystack（干草垛）里搜索needle（针）的位置，该位置满足的条件是，把needle插入这个位置之后，haystack还能保持升序
        bisect_left返回的插入位置是原序列中跟被插入元素相等的元素的位置，也就是新元素会被放置于它相等的元素的前面;
        bisect_right返回的则是跟它相等的元素之后的位置
"""

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}   {2}{0:<2d}'


def demo(bisect_fun):
    for needle in reversed(NEEDLES):
        position = bisect_fun(HAYSTACK, needle)
        offset = position * "  |"
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_func = bisect.bisect_left
    else:
        bisect_func = bisect.bisect_right

    print("DEMO:", bisect_func.__name__)
    print("haystack->", " ".join("%2d" % n for n in HAYSTACK))
    demo(bisect_func)
