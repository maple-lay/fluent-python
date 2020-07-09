"""
collections.namedtuple是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类
"""
from collections import namedtuple

if __name__ == '__main__':
    # 创建一个具名元组需要两个参数
    # 类名： 'City'
    # 类的各个字段的名字： 'name country population coordinates'
    # 字段名可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名
    City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
    # City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)
    print(tokyo.population)
    print(tokyo.coordinates)

    # Demo 2-10
    # 具名元组的其他属性和方法
    # _fields属性是一个包含这个类所有字段名称的元组
    print(City._fields)

    # 用_make()通过接受一个可迭代对象来生成这个类的一个实例。
    LatLong = namedtuple("LatLong", 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data)

    # _asdict()把具名元组以collections.OrderedDict的形式返回，
    print(delhi._asdict())

    for key, value in delhi._asdict().items():
        print(key + ':', value)
