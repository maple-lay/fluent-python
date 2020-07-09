"""
collections.abc模块中有Mapping和MutableMapping这两个抽象基类，
    它们的作用是为dict和其他类似的类型定义形式接口
标准库里的所有映射类型都是利用dict来实现的
    只有可散列的数据类型才能用作这些映射里的键
可散列的数据类型：
    这个对象的生命周期中，它的散列值是不变的
    而且这个对象需要实现__hash__（　）方法
    可散列对象还要有__eq__（　）方法，这样才能跟其他键做比较
    原子不可变数据类型（str、bytes和数值类型）都是可散列类型，
    frozenset也是可散列的，因为根据其定义，frozenset里只能容纳可散列类型
    元组的话，只有当一个元组包含的所有元素都是可散列类型的情况下，它才是可散列的
    一般来讲用户自定义的类型的对象都是可散列的，散列值就是它们的id（　）函数的返回值
"""

"""
字典推导
"""

if __name__ == '__main__':
    DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, "United States"),
        (61, 'Indonesia'),
    ]

    my_dict = {code: country for code, country in DIAL_CODES}
    print(my_dict)
    my_dict2 = {country.upper(): code for code, country in DIAL_CODES}
    print(my_dict2)