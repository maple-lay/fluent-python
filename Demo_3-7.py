"""
    __missing__
    只会被__getitem__调用
    提供__missing__方法对get或者__contains__（in运算符会用到这个方法）这些方法的使用没有影响

"""

# Demo_3-7


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):  # 如果找不到的键本身就是字符串，那就抛出KeyError异常
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, defalut=None):  # get方法把查找工作用self[key]的形式委托给__getitem__，这样在宣布查找失败之前，还能通过__missing__再给某个键一个机会
        try:
            return self[key]
        except KeyError:
            return defalut

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

    # 使用“魔法方法”时注意避免“死循环”的出现。
    