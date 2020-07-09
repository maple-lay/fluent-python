"""
支持函数式编程的包

"""
from functools import reduce
from operator import mul, itemgetter, attrgetter
from collections import namedtuple


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


def fact_mul(n):
    return reduce(mul, range(1, n + 1))


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.13333)),
    ('New York-Newark', 'US', 20.10, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

if __name__ == '__main__':
    # itemgetter(index), 获取一个序列中的第index个元素
    # 如果把多个参数传给itemgetter， 它构建的函数会返回提取的值构成的元组
    # itemgetter使用[]运算符，因此它不仅支持序列，还支持映射和任何实现_getitem_方法的类
    for city in sorted(metro_data, key=itemgetter(2)):
        print(city)

    cc_name = itemgetter(1, 0)  # 把从一个列表中提取第1个元素和第0个元素，封装成一个函数
    for city in metro_data:
        print(cc_name(city))

    LatLong = namedtuple("LatLong", "lat long")
    Metropolis = namedtuple("Metropolis", "name cc pop coord")

    metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
                   for name, cc, pop, (lat, long) in metro_data]
    '''
    metro_areas2 = []
    for name, cc, pop, (lat, long) in metro_data:
        metro_areas2.append(Metropolis(name, cc, pop, (lat, long)))
    # print(metro_areas2[0])
    # print(metro_areas2[1])
    '''

    print("-----------------------------\n")
    print(metro_areas[0])
    print(metro_areas[1])

    print("-----------------------------\n")
    name_lat = attrgetter("name", "coord.lat")  # 获取城市的名称， 纬度  配合nametuple使用。
    # print(metro_areas[0].coord.long)
    for city in sorted(metro_areas, key=attrgetter("coord.lat")):
        print(name_lat(city))
