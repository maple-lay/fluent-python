"""
集合 set frozenset
    集合中的元素必须是可散列的，set类型本身是不可散列的，但是frozenset可以。因此可以创建一个包含不同frozenset的set。

"""
# Demo_3-10, Demo_3-11, Demo_3-12
# 使用集合计算交集
from dis import dis
if __name__ == '__main__':
    set_A = {1, 2, 3}
    set_B = {1, 2, 4, 5, 6, 7}
    print(len(set_A & set_B))
    print(len(set_A.intersection(set_B)))

    # 不适用集合的写法
    found = 0
    for item in set_B:
        if item in set_A:
            found += 1

    print(found)

    # 反汇编
    print(dis("{1}"))
    print(dis("set([1])"))


