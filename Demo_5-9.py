"""
对比 函数专有，而用户定义的一般对象没有的属性
"""

if __name__ == '__main__':
    class C: pass
    obj_c = C()
    def func_c(): pass

    print(sorted(set(dir(func_c)) - set(dir(obj_c))), sep='\n')