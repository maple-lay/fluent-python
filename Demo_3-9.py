"""
不可变映射类型
    MappingProxyType
"""
from types import MappingProxyType

if __name__ == '__main__':
    d = {1: "A"}
    d_proxy = MappingProxyType(d)
    print(d, "\n", d_proxy)
    try:
        d_proxy[2] = "B"  # d_proxy不能做任何修改
    except TypeError:
        print("d_proxy 不能修改")
    d[2] = "B"
    print(d, "\n", d_proxy)  # 会跟踪d的修改

