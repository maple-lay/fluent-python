"""
    collections.OrderedDict:
        这个类型在添加键的时候会保持顺序，因此键的迭代次序总是一致的
    collections.ChainMap:
        该类型可以容纳数个不同的映射对象，然后在进行键查找操作的时候，这些对象会被当作一个整体被逐个查找，直到键被找到为止
    collections.Counter:
        这个映射类型会给键准备一个整数计数器。每次更新一个键的时候都会增加这个计数器。所以这个类型可以用来给可散列表对象计数，或者是当成多重集来用——多重集合就是集合里的元素可以出现不止一次。
    collections.UserDict:
        这个类其实就是把标准dict用纯Python又实现了一遍。跟OrderedDict、ChainMap和Counter这些开箱即用的类型不同，UserDict是让用户继承写子类的

        MutableMapping.update
        Mapping.get
"""
# Demo_3-8 UserDict
import collections


class StrKetDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data  # UserDict有一个叫作data的属性，是dict的实例，这个属性实际上是UserDict最终存储数据的地方

    def __setitem__(self, key, value):
        self.data[str(key)] = value

